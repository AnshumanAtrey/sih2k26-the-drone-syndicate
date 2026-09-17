#!/usr/bin/env python3
"""
Fly the Kestrel survey profile in PX4 SITL and leave a real ULog behind.

Mission profile is the one derived in DATA.md §21, not an invented one:
  30 m AGL, 4.0 m/s, lawnmower lanes at 30 m spacing (the thermal swath).
Includes a deliberate GPS-denied segment, because "GPS-enabled and GPS-denied
navigation" is the problem statement's own first Expected-Solution bullet and a
log that never loses GPS does not demonstrate it.
"""
import math, sys, time
from pymavlink import mavutil

ALT, SPEED, LANE_M, LANES, LANE_LEN = 30.0, 4.0, 30.0, 4, 220.0

def wait_hb(m):
    m.wait_heartbeat(); print(f"heartbeat sys={m.target_system} comp={m.target_component}", flush=True)

def offs(lat, lon, dn, de):
    return lat + (dn/6378137.0)*180/math.pi, lon + (de/(6378137.0*math.cos(lat*math.pi/180)))*180/math.pi

def upload(m, home):
    lat0, lon0 = home
    wps = [(lat0, lon0, ALT)]
    for i in range(LANES):
        e = i*LANE_M
        a, b = (0.0, LANE_LEN) if i % 2 == 0 else (LANE_LEN, 0.0)
        wps.append(offs(lat0, lon0, a, e) + (ALT,))
        wps.append(offs(lat0, lon0, b, e) + (ALT,))
    wps.append((lat0, lon0, ALT))
    print(f"uploading {len(wps)} waypoints: {LANES} lanes x {LANE_LEN:.0f} m at {LANE_M:.0f} m spacing", flush=True)
    m.mav.mission_count_send(m.target_system, m.target_component, len(wps))
    seq = 0
    t0 = time.time()
    while seq < len(wps) and time.time()-t0 < 90:
        msg = m.recv_match(type=['MISSION_REQUEST','MISSION_REQUEST_INT'], blocking=True, timeout=10)
        if not msg: break
        i = msg.seq; la, lo, al = wps[i]
        cmd = mavutil.mavlink.MAV_CMD_NAV_TAKEOFF if i == 0 else mavutil.mavlink.MAV_CMD_NAV_WAYPOINT
        m.mav.mission_item_int_send(m.target_system, m.target_component, i,
            mavutil.mavlink.MAV_FRAME_GLOBAL_RELATIVE_ALT, cmd, 0, 1, 0, 2, 0, 0,
            int(la*1e7), int(lo*1e7), al)
        seq = i+1
    ack = m.recv_match(type='MISSION_ACK', blocking=True, timeout=15)
    print("mission ack:", ack, flush=True)
    return len(wps)

def main():
    m = mavutil.mavlink_connection('udpin:0.0.0.0:14540')
    wait_hb(m)
    for _ in range(60):
        g = m.recv_match(type='GLOBAL_POSITION_INT', blocking=True, timeout=5)
        if g and g.lat != 0: break
    home = (g.lat/1e7, g.lon/1e7)
    print(f"home {home}", flush=True)

    m.mav.param_set_send(m.target_system, m.target_component, b'MPC_XY_CRUISE',
                         SPEED, mavutil.mavlink.MAV_PARAM_TYPE_REAL32)
    upload(m, home)

    m.set_mode_apm if False else None
    m.mav.command_long_send(m.target_system, m.target_component,
        mavutil.mavlink.MAV_CMD_DO_SET_MODE, 0, 1, 4, 4, 0, 0, 0, 0)   # AUTO.MISSION
    time.sleep(2)
    m.mav.command_long_send(m.target_system, m.target_component,
        mavutil.mavlink.MAV_CMD_COMPONENT_ARM_DISARM, 0, 1, 0, 0, 0, 0, 0, 0)
    print("armed, flying", flush=True)

    t0 = time.time(); gps_cut = False; last = 0
    while time.time()-t0 < 600:
        msg = m.recv_match(type=['GLOBAL_POSITION_INT','STATUSTEXT','HEARTBEAT'], blocking=True, timeout=5)
        el = time.time()-t0
        if msg and msg.get_type() == 'GLOBAL_POSITION_INT' and el-last > 20:
            last = el
            print(f"  t+{el:5.0f}s alt={msg.relative_alt/1000:5.1f} m  "
                  f"gs={math.hypot(msg.vx,msg.vy)/100:4.1f} m/s", flush=True)
        # GPS-denied window: 150-260 s, the 1-3 min excursion DATA.md §24 bounds
        if not gps_cut and el > 150:
            gps_cut = True
            m.mav.param_set_send(m.target_system, m.target_component, b'SIM_GPS_BLOCK',
                                 1, mavutil.mavlink.MAV_PARAM_TYPE_INT32)
            print("  >>> GPS BLOCKED (simulating canopy / urban canyon)", flush=True)
        if gps_cut and el > 260:
            m.mav.param_set_send(m.target_system, m.target_component, b'SIM_GPS_BLOCK',
                                 0, mavutil.mavlink.MAV_PARAM_TYPE_INT32)
            gps_cut = None
            print("  >>> GPS REACQUIRED", flush=True)
        if msg and msg.get_type() == 'HEARTBEAT' and el > 120:
            if not (msg.base_mode & mavutil.mavlink.MAV_MODE_FLAG_SAFETY_ARMED):
                print(f"disarmed at t+{el:.0f}s, mission complete", flush=True); break
    print("flight finished", flush=True)

if __name__ == '__main__':
    sys.exit(main())
