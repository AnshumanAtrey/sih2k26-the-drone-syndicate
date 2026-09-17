#!/usr/bin/env python3
"""Print what a ULog actually contains, so CI fails loudly on an empty flight."""
import sys, glob
from pyulog import ULog
ok = False
for f in sorted(glob.glob(sys.argv[1] if len(sys.argv) > 1 else "out/*.ulg")):
    u = ULog(f)
    dur = (u.last_timestamp - u.start_timestamp) / 1e6
    names = {d.name for d in u.data_list}
    print(f"=== {f}")
    print(f"    duration {dur:.1f} s · {len(u.data_list)} message types")
    need = ['vehicle_gps_position', 'vehicle_local_position', 'vehicle_status', 'vehicle_air_data']
    for k in need:
        print(f"    {k:28} {'present' if k in names else 'MISSING'}")
    try:
        lp = u.get_dataset('vehicle_local_position')
        import math
        z = lp.data.get('z', [])
        if len(z):
            print(f"    max altitude {abs(min(z)):.1f} m")
        vx, vy = lp.data.get('vx', []), lp.data.get('vy', [])
        if len(vx):
            sp = max(math.hypot(a, b) for a, b in zip(vx, vy))
            print(f"    max ground speed {sp:.1f} m/s")
    except Exception as e:
        print("    (local_position read failed:", e, ")")
    if dur > 30 and 'vehicle_local_position' in names:
        ok = True
print("USABLE FLIGHT LOG" if ok else "NO USABLE LOG")
sys.exit(0 if ok else 1)
