# Slide 3 — Technical Approach

**Official section:** "Technical Approach"
Template sub-bullets, verbatim: *technologies to be used (programming languages, frameworks,
hardware) · methodology and process for implementation (flow charts / images / working prototype)*

**Prompts: 3.** `P3.1` the pixel ladder · `P3.2` what reaches a buried person · `P3.3` the two airframes.

---

## The argument this page has to land

The template asks for two things — the stack, and the method. The trap is answering with a logo wall
and a box diagram, which is what most decks do and which proves nothing. Instead:

- **The stack is Qualcomm's**, because Qualcomm wrote this problem statement. QCS6490 with a 12 TOPS
  Hexagon NPU on the mothership, models compiled through Qualcomm AI Hub and QNN, Snapdragon Hexagon
  on every scout, PX4/ROS 2 on every airframe, an optional 5G modem for the *"optional 5G/Wi-Fi"*
  bullet the PS actually asks for. NVIDIA Jetson is named once, as the fallback, and that is all.
- **The method is the fusion architecture**, and its content is a principle, not a pipeline: *sensors
  that fail for the same reason add almost nothing.* Thermal and RGB are one vote in two coats — both
  die behind a concrete slab. So the streams that matter for a buried person are the ones with
  **independent failure modes**: phone RF through rubble, vital radar, CO2 plume, dropped acoustics.
  Combined by **Bayesian evidence accumulation**, not an AND-gate.
- **And we show one piece of arithmetic**, because the difference between a team that specified a
  thermal camera and a team that *computed* which thermal camera is the whole difference in this
  section. It also lets us admit, on the page, that we rejected our own first choice.

---

## Layout

```
┌───────────────────────────────────────────────────────────────┐
│  P3.1  WHY 30 METRES — the pixel ladder      (full width)     │
├──────────────────────────────┬────────────────────────────────┤
│  P3.2  WHAT REACHES A        │  P3.3  TWO AIRFRAMES           │
│  BURIED PERSON + fusion      │  exploded, real part numbers   │
├──────────────────────────────┴────────────────────────────────┤
│  native table: THE STACK  (4 rows, see below)                 │
└───────────────────────────────────────────────────────────────┘
```

---

## P3.1 — Why 30 metres: the pixel ladder `[DATA-EXACT — editorial infographic]`

Paste the STYLE.md global prefix first.

```
A full-width 16:9 editorial infographic on deep navy, laid out as three large panels in a horizontal row, separated by generous negative space and no dividing lines.

In every panel: the same top-down silhouette of a person lying prone on rubble, drawn identically at the identical size in all three panels, in warm amber. Over that silhouette, a square pixel grid is overlaid — and the grid is drastically coarser or finer from panel to panel. Where a grid cell overlaps the body, the cell is tinted; the tint strength reflects how much of that cell the body fills.

LEFT PANEL: an extremely coarse grid — the entire person sits inside a small fraction of ONE single enormous square, which is tinted a barely-perceptible dull grey-amber, almost invisible against the navy.
CENTRE PANEL: a medium grid — the person occupies roughly three quarters of one square, tinted a clear mid amber.
RIGHT PANEL: a fine grid — the person spans about eight cells tall and two cells wide, each tinted bright cyan, so the silhouette's shape and posture are legible from the pixels alone.

Below the three panels, a single thin horizontal cyan rule running the full width, with one short formula sitting on it.

Render style: precise flat technical infographic in the manner of a well-designed engineering figure. Not a chart. No axes, no bars, no legend.

Text labels (render exactly):
- above LEFT panel, slate grey, stacked three lines: "MLX90640 32x24" / "2.68 M PER PIXEL" / "10% OF ONE PIXEL"
- under LEFT panel, amber: "INVISIBLE"
- above CENTRE panel, slate grey, stacked three lines: "MLX90640 NARROW" / "0.98 M PER PIXEL" / "71% OF ONE PIXEL"
- under CENTRE panel, amber: "MARGINAL"
- above RIGHT panel, slate grey, stacked three lines: "FLIR LEPTON 3.5 160x120" / "0.20 M PER PIXEL" / "8 x 2 PIXELS"
- under RIGHT panel, cyan: "DETECTABLE — AND SHAPED"
- on the rule at the bottom, centred, small slate grey: "GSD = 2 H TAN(FOV/2) / PIXELS   AT H = 30 M"

Constraint tail: 16:9. Only the labels listed. The human silhouette must be exactly the same size in all three panels. No watermark, no border.
```

*The person is the same size in all three panels and only the grid changes — that is the entire
point, and it is the one thing to check on every generation. Verify each number against `DATA.md` §5
before accepting the image; this is a `[DATA-EXACT]` prompt.*

---

## P3.2 — What reaches the person under the rubble `[DATA-EXACT — cutaway + fusion]` · **v2**

> **Why v2, and this was a real hole in the design, not a rendering problem.** The v1 gate ran on
> thermal + RGB + a second scout's angle. **All three need line of sight.** A person under a slab has
> none — so the gate had a coverage hole over exactly the population the survival curve is about, and
> both of this deck's anchors sit in that hole: Wayanad's 206 and Nepal's 4,500 were not people lying
> visible on a surface. v2 shows the streams that *do* penetrate, and replaces the brittle AND-rule
> with a weighted posterior. v1's render is retired to the finale deck; its prompt is archived below.
>
> **The principle to state on the slide, because it is the actual intellectual content:** more sensors
> do not mean more confidence — sensors that fail for the *same reason* add almost nothing. Thermal
> and RGB are one vote in two coats; both die behind concrete. **Independence is what buys
> confidence**, and RF, chemical, radar and acoustic streams are independent of line of sight.

Paste the STYLE.md global prefix first.

```
A 16:9 technical illustration on deep navy, split into a LEFT REGION of about 65% width and a RIGHT REGION of about 30%, separated by generous negative space.

LEFT REGION — a geological-style vertical cutaway cross-section, seen from the side, of a collapsed-building rubble pile: broken concrete slabs, twisted rebar, splintered timber and mud, layered and interlocking, drawn in muted grey-brown. Deep inside the pile, roughly two thirds of the way down, one small void with a single human figure curled inside it, rendered in warm amber and clearly alive.

A small quadcopter hovers above the pile at the top of the frame. From it, four distinct sensing bands descend into the cross-section, each a different colour, each terminating at a visibly different depth, drawn as translucent downward cones or beams with a hard stop where they end:
- a WHITE band that stops dead at the very top surface of the rubble, penetrating nothing
- a THIN ORANGE band that also stops at the surface, alongside the white one
- a broad CYAN band that passes deep into the pile and reaches past the human figure
- a narrow GREEN band that also reaches the figure, drawn as a rising dotted plume travelling upward out of the void toward the drone, opposite in direction to the others

Separately, resting directly on the top of the rubble pile, one small dropped sensor pod with short spikes into the debris and faint concentric rings radiating downward from it.

A horizontal depth scale runs down the left edge of the cross-section with three tick marks.

RIGHT REGION — five small labelled input chips stacked vertically, each with a short arrow feeding right into a single tall vertical meter drawn like a thermometer or fuel gauge. The meter is filled from the bottom to about three-quarters. Two horizontal marker lines cross the meter: a lower amber line and an upper green line. At the top of the meter, a green survivor pin.

Render style: precise engineering cutaway, the visual language of a geological or civil-engineering section drawing. Thin linework, restrained translucency, no glow spill. Not a chart. No axes on the meter, no legend box.

Text labels (render exactly):
LEFT REGION:
- title above the left region, in #E2E8F0: "WHAT ACTUALLY REACHES A BURIED PERSON"
- on the WHITE band where it stops, slate grey: "RGB — SURFACE ONLY"
- on the THIN ORANGE band where it stops, amber: "THERMAL — SURFACE ONLY"
- on the broad CYAN band, cyan: "PHONE RF — THROUGH 3 M"
- second line under it, cyan, smaller: "WIFI + BLE, ZERO EXTRA COST"
- on the deep radar reach, cyan: "UWB VITAL RADAR — 9 M RUBBLE"
- on the rising GREEN plume, green: "CO2 PLUME — 3 PPB"
- at the dropped pod, slate grey: "ACOUSTIC POD — DROPPED"
- depth scale ticks, small slate grey, top to bottom: "0 M" then "3 M" then "9 M"
RIGHT REGION:
- title above the right region, in #E2E8F0: "WEIGHTED, NOT AND-GATED"
- the five input chips, top to bottom, small: "RGB POSE" / "THERMAL" / "PHONE RF" / "VITAL RADAR" / "CO2 + ACOUSTIC"
- at the lower amber marker line, amber: "RE-INSPECT"
- at the upper green marker line, green: "PUBLISH"
- beside the green pin at the top, green: "SURVIVOR + CONFIDENCE"
- one thin footnote line along the bottom of the frame, small slate grey: "Depths: NASA JPL FINDER; MDPI Sensors 18(3) 852; 10.3390/s22197502"

Constraint tail: 16:9. Only the labels listed. The two surface-only bands must visibly stop at the rubble surface and penetrate nothing — that contrast is the entire argument. No gore, no injury detail. No watermark, no border.
```

*Verify: **the white and orange bands must stop at the surface** while cyan and green reach the
figure. If the model lets thermal penetrate, the image argues the opposite of the truth and must be
regenerated. Depths trace to `DATA.md` §11a — `[DATA-EXACT]`.*

**The close this sets up, and it is the best line available to us.** The deep radar stream is
FINDER-class — NASA JPL / DHS, tested through 9 m of rubble, and it **found four men alive under 10 ft
of debris in Nepal in 2015.** It is also **the same class of sensor that reported three breath signals
at Wayanad where nothing was found.** So: *the only stream that reaches deep is also the only stream
that has already lied to us — which is precisely why it is one weighted vote and never the decision.*
That closes the loop the frog opened on Slide 2.

---

## Archived — P3.2 v1, the three-gate corroboration flow `[already rendered: images/P3.2-gate.png]`

Superseded by v2. Good render, and still useful in the finale deck as a detail view of the RGB +
thermal branch specifically. Not used in the idea submission.

```
A clean technical flow diagram on deep navy, 16:9, reading strictly left to right, with two visibly different outcome paths.

Left edge: two small input tiles stacked vertically — an upper tile showing a coarse thermal image of a warm blob, a lower tile showing a sharp RGB aerial image of a person lying on debris. Thin cyan arrows carry both rightward into a hexagonal node.

From that hexagon, arrows pass through three consecutive vertical gate bars, drawn as narrow upright slotted barriers. At each gate, one arrow continues rightward in cyan, and one arrow branches downward in red toward a small red bin icon at the bottom of the frame.

Beside the SECOND gate, floating just below the red reject arrow, a small photographic inset of a frog in a red-outlined circle.

Right edge: a single bright green marker pin with concentric rings, and next to it a small stack of three evidence thumbnail cards — a thermal crop, an RGB crop, and a small map crop.

Render style: crisp holographic technical schematic, thin strokes, restrained glow, engineering-diagram discipline. Generous space, nothing crowded.

Text labels (render exactly, each attached to its own element):
- on the upper input tile, slate grey: "THERMAL 8 HZ"
- on the lower input tile, slate grey: "RGB YOLO INT8"
- on the hexagon, cyan: "FUSE ON-DEVICE"
- on gate 1, #E2E8F0: "THERMAL BAND 30-40 C"
- on gate 2, #E2E8F0: "RGB POSE CONFIRMS"
- on gate 3, #E2E8F0: "SECOND SCOUT AGREES"
- beside the frog inset, red: "REJECTED HERE"
- at the red bin, red: "NO MARKER"
- at the green pin, green: "SURVIVOR + CONFIDENCE"
- above the evidence cards, slate grey: "EVIDENCE SHIPS WITH IT"

Constraint tail: 16:9. Only the labels listed. No watermark, no border.
```

*This one visual answers three PS bullets at once — *Multi-Sensor Fusion*, *On-Device AI Inference*
and *Emergency Alerting* — and it closes the loop opened by P2.1. The frog inset is not a joke; it is
the citation.*

---

## P3.3 — Two airframes `[isometric technical cutaway, real part numbers]`

```
An isometric technical illustration on deep navy, 16:9, showing two multirotor aircraft side by side at correct relative scale — a large hexacopter on the left occupying about 60% of the frame, a noticeably smaller quadcopter on the right.

Both are drawn as partial exploded views: the top shell lifted and floating slightly above the airframe, revealing the internal stack, with thin cyan leader lines running from each internal module out to a label in the surrounding negative space.

LEFT — the hexacopter, six arms, props faintly motion-blurred. Revealed inside: a single-board computer with a visible heatsink and camera ribbon connectors at the centre; a separate small flight-controller board behind it; a small square thermal sensor module and a larger RGB lens in a compact gimbal underneath; a whip antenna on top; two battery packs at the rear.

RIGHT — the quadcopter, four short arms with prop guards, minimal open frame. Revealed inside: a modern smartphone mounted flat and centrally as the aircraft's main compute, its camera facing down through the frame, clearly recognisable as a phone; a tiny flight-controller board; a small radio module; one battery pack.

Between the two aircraft, vertically centred in the gap, one large price chip for each.

Render style: premium aerospace exploded-view schematic, thin precise linework, cyan structure with selective amber highlights, matte materials.

Text labels (render exactly, on leader lines):
LEFT aircraft: "QUALCOMM RB3 GEN 2 — 12 TOPS" / "PIXHAWK 2.4.8 — PX4" / "FLIR LEPTON 3.5" / "LoRa SX1262 HUB" / "4S 5000 MAH x2"
RIGHT aircraft: "RECYCLED SNAPDRAGON PHONE" / "HEXAGON NPU — QNN" / "LoRa NODE"
Price chips in the centre gap: cyan chip reading "MOTHERSHIP 1.11 L", amber chip reading "SCOUT 25,600"

Constraint tail: 16:9. Only the labels listed. Both aircraft matte grey-black, no military markings, no weapons. No watermark, no border.
```

*The phone must be recognisably a phone. That is the memorable detail on this page and the one a
Qualcomm judge will repeat to the other judges.*

---

## Native table — the stack

| Layer | What we use | Why this and not the obvious alternative |
|---|---|---|
| **Mothership compute** | **Qualcomm RB3 Gen 2 / QCS6490** — 12 TOPS Hexagon NPU, 6 GB, Linux, ₹50,000. Production path: **ModalAI VOXL 2 / QRB5165**, 15 TOPS, PX4 on the sensor DSP, 5G-ready, 16 g | Qualcomm's robotics stack is the one this PS describes. **Detection runs INT8 on the Hexagon NPU; the language model runs on CPU/GPU — different engines, so report generation never steals frames from the detector.** Jetson Orin Nano is the named fallback, nothing more |
| **Scout compute** | Second-hand **Snapdragon 8-series handset**, ₹9,000 — Hexagon NPU + 4K camera + IMU + GNSS + LTE modem + battery + sealed shell, 190 g | One part instead of six. Models reach it through the *same* Qualcomm AI Hub → QNN path as the mothership, so we maintain one toolchain, not two |
| **Perception — line of sight** | YOLOv8n person + pose, INT8 via **Qualcomm AI Hub → QNN**; FLIR Lepton 3.5 radiometric thermal | YOLOv8 runs **65+ FPS on a Snapdragon NPU against 2 FPS on its CPU** — the NPU is not an optimisation, it is the difference between real-time and unusable |
| **Perception — through rubble** | **Passive WiFi probe-request + BLE advertisement sniffing on the scout's own phone radio** (₹0, 0 g) · FINDER-class UWB vital-signs radar · SCD41-class CO2 + NH3 · air-dropped acoustic/seismic pods on the six-servo release already in our PRD | The streams the PS's *"signs of human presence"* bullet actually needs. Chosen for **independent failure modes**, not for count: RF ignores line of sight, CO2 ignores darkness, radar ignores both, acoustics ignore depth. Peer-reviewed in this exact combination — *Sensors* 18(3) 852 tested CO2 + thermal + microphone and found CO2 usefully narrows the area and microphones add real benefit alongside other sensors |
| **Fusion** | **Bayesian evidence accumulation on a geospatial grid** — each stream contributes a likelihood ratio per cell; the posterior *is* the priority queue. Two thresholds: **re-inspect** and **publish** | Not a rule stack. An AND-gate is brittle and discards weak-but-real hits; a weighted posterior means **a weak independent stream can never make the estimate worse**. Same Bayesian search theory that found the USS Scorpion and AF447, and it sits alongside the sweep-width method in `DATA.md` §6a |
| **Flight & autonomy** | **PX4** + **ROS 2** + MAVROS; GPS nominal; **ORB-SLAM3 / VINS-Fusion** VIO published to PX4 as `GPS_INPUT` for GPS-denied flight (~0.5 m drift per 100 m); optical flow + LiDAR for altitude hold | Answers the PS's *GPS-enabled and GPS-denied navigation* bullet with an open stack we do not have to write |
| **Human + wide-area priors** | Mothership carries an **open SSID with a captive portal** — locals submit *"my mother was in the blue house behind the temple"*, geotagged by aircraft position and RSSI, no internet needed (the Kerala 2018 `keralarescue.in` model, built by IEEE Kerala student volunteers with Kerala IT Mission). Plus **SACHET cell broadcast** (P2.3), aggregate sector counts, Sentinel-1 SAR change detection and ISRO Bhuvan footprints | Crowd reports do not detect anyone — **they re-weight the search.** Locals know who is missing and where they were standing, which no sensor can produce. In Bayesian terms it is the prior, and a strong one |
| **Comms & reporting** | LoRa SX1262 mesh carrying **detections as JSON, never video**; optional LTE/5G; on-device **Llama 3.2 3B Q4 (2.0 GB)** writes the situation report and ranks the rescue queue | A survivor marker is a few hundred bytes. Designing for kilobits means the system degrades to *slower*, never to *offline*. Nothing in the mission path requires a network |

---

## 30-second script

> "The stack is Qualcomm's, because the problem is Qualcomm's. A QCS6490 with a twelve-TOPS Hexagon
> NPU is the mothership's brain, models compiled through Qualcomm AI Hub and QNN — YOLOv8 runs
> sixty-five frames a second on that NPU against two on the CPU. Every scout's brain is a recycled
> Snapdragon phone, same toolchain. PX4 and ROS 2 fly everything; ORB-SLAM3 feeds PX4 fake GPS when
> the real one is gone. We chose the thermal sensor with arithmetic, not a catalogue — and rejected
> our own first pick, because at thirty metres a thirty-two-by-twenty-four array puts a human inside
> a tenth of one pixel. And nothing becomes a survivor marker until three independent gates agree."
