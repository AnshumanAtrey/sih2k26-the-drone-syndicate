# PROMPTS — ROUND 2 · 11 Sep 2026

Nine more. Same rules as [`PROMPTS-TO-RUN.md`](PROMPTS-TO-RUN.md): **every block is complete and
self-contained**, style prefix already merged, copy the fence and paste.

These exist because an audit against the problem statement found three bullets we barely cover, and
because you asked about agency integration. **Nothing here is committed to a slide yet** — generate
first, decide after. Some are deliberately two takes on the same idea (one dark, one white) so you
can compare rather than pre-commit.

## What the PS audit found

| PS Expected-Solution bullet | Current coverage | Round 2 |
|---|---|---|
| 1. GPS-denied nav, SLAM, obstacle avoidance | **nothing visual** — a table row | **#3** tiles · **#4** cinematic |
| 3. Multi-sensor fusion + **localization** | fusion strong, localization absent | **#7** |
| 4. Hazard classification — PS names **8** types | we show **1** | **#5** |
| 8. Dashboard **to support disaster management agencies** | UI strong, agencies absent | **#1** white · **#2** dark |

Plus three that answer slide sub-bullets rather than PS bullets: **#6** blueprint (*technologies to be
used*), **#8** mission timeline (*practicability*), **#9** stat tiles (reusable furniture).

## New facts these are built on — all in `DATA.md`

- **ERSS-112 already accepts machine signals.** Its ten intake channels include **"IoT-based Signals"**
  and **"External Signals."** State **ERC** → district coordination centre → Emergency Response Vehicle.
- **CAP is the national format.** NDMA runs SACHET on the **Common Alerting Protocol**, ITU-recommended.
  We emit the schema the country already speaks rather than inventing one.
- **NDEM 5.0 / Bhuvan** — ISRO/NRSC under NDMA, reaches states over ISRO-DMS-VPN, feeds **ICR-ER** (MHA).
- **NDRF = 16 battalions** from **BSF 8 · CRPF 4 · CISF 2 · ITBP 2 · SSB 2**; each battalion is
  **18 self-sufficient SAR teams of 47** (structural engineers, technicians, electricians, canine,
  paramedics), **1,149 personnel** per battalion.

## Square tiles — the density unlock

A row of **five 1.9 in tiles** occupies the same slot as one 4:1 band but carries five facts instead
of one. Tile spec: **1:1, one icon, one number, one label of three words or fewer, white ground,
legible at 1.9 in and at thumbnail.** #3, #5 and #9 are built this way.

## Which chat to run these in

**Do not reuse the four round-1 chats** for the white ones — they are saturated with slide-specific
subjects (rubble, banknotes, pictogram people) and will bleed.

| Chat | Prompts | Why grouped |
|---|---|---|
| **New A** — white, systems | #1, #7, #8 | data-flow and measurement diagrams, shared visual logic |
| **New B** — white, tiles | #3, #5, #9 | all icon-grid work; a consistent icon style across them is a *benefit* |
| **New C** — white, drafting | #6 | blueprint is a distinct style, keep it clean |
| **Dark** — #2, #4 | reuse the original chat that produced `P2.2-hero.png` if it still exists — bleed from the hero is exactly what you want. If not, start fresh and **attach `images/P2.2-hero.png`**, then append to the prompt: *"match the lighting, palette, material finish and realism of the attached image."* |

---

## 1 · Handover — where our output goes  `WHITE`

Candidate for **Slide 5** (agencies half of PS bullet 8) or **Slide 4**
**Reject if:** the centre produces more than **one** message · "ERSS-112" or "CAP" missing · the four
consumers are not visibly fed by the same single message

```
Style: precise editorial-technical infographic for a printed report. PURE WHITE background, hex #FFFFFF, absolutely flat - no gradient, no vignette, no paper texture, no coloured wash, no drop shadow falling on the background, no rounded card or panel behind the artwork, pure white right to all four edges. Linework and primary text in deep navy #0B1220. Our system in teal #0E7490. External and legacy systems in slate #475569. Success and delivery in #15803D. Light tints in #E2E8F0. Clean geometric sans-serif; ALL text perfectly horizontal - never curved, never rotated. Generous white space, strong left-to-right reading order. No watermarks, no borders, no frames, no outer glow, no 3D bevel, no stock-illustration gloss. 16:9.

Composition: a three-stage flow reading strictly left to right - a narrow INPUT column on the left, one central node, and a fan of four OUTPUT destinations on the right.

LEFT COLUMN: three small slate-outlined chips stacked vertically, each with a tiny icon - a cell tower, a group of three people, and a satellite. Thin slate arrows run right from all three into the centre.

CENTRE: one hexagonal node in solid teal containing a small hexacopter glyph, sitting slightly above centre. Emerging from its right side, ONE single thick teal arrow - not several - which travels right a short distance and then splits at a clearly drawn fan point into four thinner arrows. At the split point, a small rectangular tag hangs on the single arrow before it divides.

RIGHT: four destination cards arranged in a vertical stack, each a slate-outlined rectangle with a small icon at its left edge and two lines of text. Top to bottom the icons are: a telephone handset, a government building, a rugged tablet, and a satellite dish. The topmost card is outlined in green instead of slate.

Render style: clean flat systems diagram, institutional-report discipline, thin precise linework, generous spacing. Not a boxes-and-arrows flowchart cliche - keep it airy. No legend box.

Text labels (render exactly, all horizontal):
- title top-left, navy, bold: "ONE MESSAGE, FOUR AGENCIES"
- the three input chips, small slate: "SACHET BROADCAST" / "LOCAL REPORTS" / "NDEM + BHUVAN PRIORS"
- on the teal hexagon, white text: "KESTREL"
- on the tag hanging from the single arrow, teal, bold: "ONE CAP MESSAGE"
- card 1, green, two lines: "ERSS-112" / "EXTERNAL SIGNAL CHANNEL"
- card 2, navy, two lines: "DISTRICT EOC" / "DDMA, INCIDENT RESPONSE SYSTEM"
- card 3, navy, two lines: "NDRF / SDRF TEAM" / "47 RESPONDERS, ON TABLET"
- card 4, navy, two lines: "NDEM 5.0 - ISRO" / "STATE RECORD VIA DMS-VPN"
- footnote along the bottom, small slate: "CAP is the protocol NDMA already runs. We emit it, we do not invent one."

Constraint: 16:9, pure white ground. Only the labels listed. Exactly ONE arrow leaves the centre node before it fans - that single shared message is the whole argument. Do not draw a map. Do not draw any real organisation's logo.
```

---

## 2 · Handover — the moment on the ground  `DARK, CINEMATIC`

Same idea as #1, told as a scene instead of a system. Candidate for **Slide 5**.
**Reject if:** the tablet screen is not legible · the scene reads as military rather than rescue

```
Style: premium defence-tech mission-control aesthetic. Deep navy-charcoal ground (#0B1220), cyan-teal primary accent (#22D3EE), warm amber-orange secondary accent (#F59E0B), restrained holographic HUD elements, cinematic lighting, photorealistic. No watermarks, no borders, no stock-photo gloss, no lens flare. All specified text renders in a clean geometric sans-serif, uppercase, small, in #E2E8F0 or #94A3B8. 16:9 widescreen.

Composition: dusk, at the edge of a landslide-hit Indian hillside settlement. In the near foreground, slightly left, an NDRF team leader in orange coveralls and a white helmet stands holding a rugged tablet at chest height, lit from below by its screen. The tablet display is angled toward the camera and clearly legible: a dark map with one pulsing green marker pin and a green dashed route running toward it.

Mid-ground, right: four rescuers in orange, seen from behind, moving away from the camera along that same route across broken ground, one carrying a folded stretcher, headlamps on.

Above and beyond them, a small quadcopter hovers low over the debris with a bright downward strobe illuminating the exact point the route leads to. High in the darkening sky behind it, the larger hexacopter is faintly visible with a soft cyan sensor glow.

Lighting: cold blue ambient dusk, warm amber from the team's headlamps and the drone strobe, cyan screen-light on the leader's face and chest. Photorealistic documentary realism. Hopeful, purposeful, not militaristic.

Text labels (render exactly, as small HUD tags with thin leader lines):
- on the tablet screen, cyan: "SURVIVOR 01 - CONF 0.94"
- second line on the tablet screen, in #94A3B8: "142 M - SAFE ROUTE"
- upper right of frame, cyan: "RECEIVED VIA ERSS-112"
- lower right of frame, amber: "TEAM ROUTED 00:58"

Constraint: 16:9. Exactly these four labels, nothing else. No weapons, no military insignia, no visible injuries, no bodies. Faces indistinct or turned away.
```

---

## 3 · Navigation fallback — four tiles  `WHITE · SQUARE`

Candidate for **Slide 3** as a tile strip. Answers PS bullet 1.
**Reject if:** the four tiles are not identical in size · any accuracy figure is wrong · the tiles
stop looking readable when shrunk to thumbnail

```
Style: precise editorial-technical infographic for a printed report. PURE WHITE background, hex #FFFFFF, absolutely flat - no gradient, no vignette, no paper texture, no drop shadow falling on the background, no rounded card behind the artwork, pure white right to all four edges. Linework and primary text in deep navy #0B1220. Our system and good values in teal #0E7490. Degraded states in burnt amber #B45309. Secondary text in slate #475569; light tints in #E2E8F0. Clean geometric sans-serif; ALL text perfectly horizontal. Generous white space. No watermarks, no borders, no outer glow, no 3D bevel. 16:9.

Composition: four perfectly square tiles in one horizontal row, all exactly the same size, evenly spaced with generous white gaps, each tile bounded by a thin slate hairline square. The row is centred in the frame with wide white margins above and below so the strip can be cropped out cleanly.

Each tile contains, arranged vertically and centred: a simple flat line icon at the top, one large numeral in the middle, and two short text lines at the bottom.
- TILE 1 icon: a satellite with signal arcs. Numeral and text in teal.
- TILE 2 icon: a stylised camera lens overlaid with three small tracked feature points. Numeral and text in teal.
- TILE 3 icon: a simple building cross-section with a drone inside it. Numeral and text in teal.
- TILE 4 icon: a drone with two of three signal bars struck out. Numeral and text in burnt amber.

Beneath the row of tiles, one thin horizontal slate rule spanning the full width of the strip, with a short caption centred on it.

Above the row, one title line.

Render style: flat editorial icon-tile figure, the discipline of a well-made spec sheet. Precise alignment, identical tile geometry, no perspective, no 3D, no glow. No legend box.

Text labels (render exactly, all horizontal):
- title above the row, navy, bold: "IT KEEPS ITS POSITION WHEN GPS DOES NOT"
- TILE 1: numeral "2 M", then two lines: "FULL GPS" / "M9N + COMPASS"
- TILE 2: numeral "0.5 M", then two lines: "VIO PRIMARY" / "PER 100 M, GPS JAMMED"
- TILE 3: numeral "0.3 M", then two lines: "INDOOR" / "FLOW + DEPTH + LIDAR"
- TILE 4: numeral "2 M", then two lines: "DEGRADED" / "PER 100 M, IMU ONLY"
- caption on the rule beneath, small slate: "ORB-SLAM3 / VINS-Fusion published to PX4 as GPS_INPUT"

Constraint: 16:9, pure white ground, the four tiles forming a horizontal strip with wide white margins above and below. Only the labels listed. All four tiles identical in size and internal layout.
```

---

## 4 · GPS-denied — inside the building  `DARK, CINEMATIC`

Same PS bullet as #3, told as a scene. Candidate for **Slide 3**.
**Reject if:** the HUD strings garble · the scene looks like a video game · the point cloud obscures
the corridor rather than overlaying it

```
Style: premium defence-tech mission-control aesthetic. Deep navy-charcoal ground (#0B1220), cyan-teal primary accent (#22D3EE), warm amber-orange secondary accent (#F59E0B), restrained holographic HUD elements, cinematic lighting, photorealistic with a technical overlay. No watermarks, no borders, no stock-photo gloss, no lens flare. All specified text renders in a clean geometric sans-serif, uppercase, small. 16:9 widescreen.

Composition: a first-person view from a small drone flying slowly down the interior of a partially collapsed concrete building. A dust-filled corridor recedes into darkness ahead, lit only by the drone's own light: fallen slabs leaning against one another, exposed bent rebar, a collapsed ceiling on the right, rubble underfoot, fine airborne dust catching the light.

Overlaid on this, as a translucent technical layer that sits on top of the scene without hiding it: a sparse cyan three-dimensional point cloud clinging to the surfaces, small square feature-tracking brackets pinned to high-contrast corners and slab edges, a dotted amber trajectory line threading forward through the gaps between obstacles, and two faint translucent depth planes hovering just in front of the nearest obstructions.

Lighting: a single hard forward light from the drone, deep shadow beyond it, cool cyan cast from the overlay, warm dust motes.

Text labels (render exactly, as flat HUD text, all horizontal):
- top centre, amber: "GPS: DENIED"
- directly beneath it, cyan: "VIO ACTIVE - DRIFT 0.5M/100M"
- beside the nearest depth plane, in #94A3B8: "OBSTACLE 4.2M"
- bottom left, in #94A3B8: "ORB-SLAM3 - 30 FPS"

Constraint: 16:9. Exactly these four labels, nothing else. No people, no bodies, no blood. The point cloud must read as an overlay on a real scene, not replace it.
```

---

## 5 · Hazard taxonomy — eight cells  `WHITE · SQUARE`

Candidate for **Slide 3**. Answers PS bullet 4 by quoting its own list back.
**Reject if:** fewer than eight cells · any hazard name differs from the PS wording · cells are not
uniform

```
Style: precise editorial-technical infographic for a printed report. PURE WHITE background, hex #FFFFFF, absolutely flat - no gradient, no vignette, no paper texture, no drop shadow falling on the background, no rounded card behind the artwork, pure white right to all four edges. Linework and primary text in deep navy #0B1220. Sensor labels in teal #0E7490. Hazard icons in burnt amber #B45309, with genuinely dangerous classes in #B91C1C. Secondary text in slate #475569; light tints in #E2E8F0. Clean geometric sans-serif; ALL text perfectly horizontal. Generous white space. No watermarks, no borders, no outer glow, no 3D bevel. 16:9.

Composition: eight identical square cells arranged in a grid of four columns by two rows, evenly spaced with generous white gaps, each bounded by a thin slate hairline square. The grid is centred with wide white margins above and below.

Each cell contains, arranged vertically and centred: a simple flat line icon at the top, one short hazard name beneath it in navy, and one shorter sensor line beneath that in teal.

The eight icons, in reading order: a flame; a rising smoke plume; a water level line over a rooftop; a scattered pile of broken slabs; a building leaning with a crack through it; a snapped utility pole with a hanging cable and a small spark; a hillside with a slumped scar running down it; a canister with three vapour wisps rising from it.

Icons 1, 6 and 8 are drawn in red; the remaining five in burnt amber.

Above the grid, one title line. Below the grid, one thin slate rule with a short caption on it.

Render style: flat editorial icon-grid figure, pictographic and uniform, the discipline of a good safety-standard sheet. Identical cell geometry throughout. No perspective, no 3D, no glow. No legend box.

Text labels (render exactly, all horizontal, navy name then teal sensor line):
- title above the grid, navy, bold: "EIGHT HAZARD CLASSES, ON DEVICE"
- cell 1: "FIRE" / "THERMAL + RGB"
- cell 2: "SMOKE" / "RGB TEXTURE + FLOW"
- cell 3: "FLOODWATER" / "RGB + NIR"
- cell 4: "DEBRIS" / "RGB + PHOTOGRAMMETRY"
- cell 5: "UNSTABLE STRUCTURE" / "TILT + CRACK GEOMETRY"
- cell 6: "EXPOSED LINES" / "RGB LINE + THERMAL ARC"
- cell 7: "LANDSLIDE ZONE" / "SCAR + CHANGE DETECTION"
- cell 8: "CHEMICAL LEAK" / "GAS SENSOR + PLUME"
- caption on the rule beneath, small slate: "Hazard list as named in the problem statement"

Constraint: 16:9, pure white ground, the eight cells forming a four-by-two grid with wide white margins. Exactly eight cells. Only the labels listed. No photorealism, no gore, no burning buildings.
```

---

## 6 · Blueprint — the mothership, drawn  `WHITE · DRAFTING`

Candidate to **replace P3.3** on Slide 3, or for the Grand Finale deck. Look at P3.3 first.
**Reject if:** the top view does not show **exactly six** arms · the three views disagree with each
other · it renders as a blue cyanotype instead of white drafting paper

```
Style: precise orthographic engineering drawing on PURE WHITE background, hex #FFFFFF, absolutely flat - no gradient, no vignette, no paper texture, no blue cyanotype wash, no drop shadow, pure white right to all four edges. This is a modern white technical drawing, NOT a blue blueprint. All linework in deep navy #0B1220: solid lines for visible edges, fine dashed lines for hidden edges, thin slate #475569 lines for dimensions and leaders with small arrowheads at both ends. Callout text in teal #0E7490. Clean geometric sans-serif; ALL text perfectly horizontal. No watermarks, no borders except the title block, no outer glow, no 3D shading, no perspective anywhere. 16:9.

Composition: three orthographic projections of one heavy-lift multirotor aircraft, arranged in standard first-angle drafting layout, with a title block in the lower right corner.

TOP VIEW, occupying the upper left and largest: the aircraft seen from directly above, showing EXACTLY SIX arms radiating evenly in a hexagon from a central body - six arms, six motors, six propeller circles drawn as thin outline circles. A dimension line runs corner to corner across the full diagonal span. A second shorter dimension line spans one propeller diameter.
FRONT VIEW, lower left: the same aircraft seen from the front, landing legs down, the sensor gimbal visible beneath the centre body, a vertical dimension line at the left giving overall height.
SIDE VIEW, upper right: the aircraft from the side, showing the battery bay at the rear and the antenna above.

Thin slate leader lines run from five points on the TOP view out to callout labels in the surrounding white space.

LOWER RIGHT: a rectangular title block divided into four stacked rows by thin navy rules.

Render style: clean CAD-style orthographic line drawing, uniform line weights, no shading, no fills, no colour except the teal callout text. Empty white space between views.

Text labels (render exactly, all horizontal):
- five callouts from the top view, teal: "COMPUTE BAY - QUALCOMM RB3 GEN 2" / "FLIGHT CONTROLLER - PIXHAWK 2.4.8" / "RGB + THERMAL GIMBAL" / "LoRa MESH ANTENNA" / "BATTERY BAY - 4S 5000 MAH x2"
- dimension on the top view diagonal, slate: "550 MM"
- dimension on the propeller, slate: "254 MM"
- dimension on the front view height, slate: "420 MM"
- view captions, small slate: "TOP" / "FRONT" / "SIDE"
- title block rows, navy: "KESTREL MOTHERSHIP" / "S550 HEXACOPTER - 6 ARM" / "PAYLOAD 1.5 KG - ENDURANCE 24 MIN" / "SHEET 1 OF 1 - NOT TO SCALE"

Constraint: 16:9, pure white ground. Only the labels listed. The top view must show exactly six arms - count them. White drafting, never blue. No shading, no perspective, no photorealism.
```

---

## 7 · Localization — how precisely we pin a survivor  `WHITE`

Candidate for **Slide 3**. Answers the word *"localization"* in PS bullet 3, which nothing currently does.
**Reject if:** the three rings are not concentric on one point · the smallest ring is not clearly the
teal one · any figure is wrong

```
Style: precise editorial-technical infographic for a printed report. PURE WHITE background, hex #FFFFFF, absolutely flat - no gradient, no vignette, no paper texture, no drop shadow falling on the background, no rounded card behind the artwork, pure white right to all four edges. Linework and primary text in deep navy #0B1220. Our best result in teal #0E7490. Intermediate results in slate #475569. Baseline in burnt amber #B45309. Survivor marker in #15803D. Light tints in #E2E8F0. Clean geometric sans-serif; ALL text perfectly horizontal. Generous white space. No watermarks, no borders, no outer glow, no 3D bevel. 16:9.

Composition: a LEFT REGION about 60% wide and a RIGHT REGION about 35%, separated by a wide white gutter.

LEFT REGION: a flat top-down plan view of a small patch of rubble, drawn as pale grey debris outlines on a very light tint, with a faint square grid beneath it for scale. At the centre, one small solid green marker dot with a tiny prone-figure glyph beside it.

Around that centre point, three perfectly concentric circles, all sharing the same centre:
- the LARGEST circle drawn as a burnt amber dashed outline
- a MIDDLE circle drawn as a slate dashed outline
- the SMALLEST circle drawn as a solid teal outline with a very light teal fill
Each circle has a short radius line running from the centre to its edge, with a label sitting on that radius line.

RIGHT REGION: three small stacked rows, each a short horizontal line of tiny icons followed by a text label. Row one shows a single satellite icon. Row two shows a satellite plus a camera icon. Row three shows two small drone icons with thin dashed bearing lines converging from them onto a single point.

Render style: flat editorial technical figure, plan-view cartographic discipline, thin precise linework. Not a chart. No axes, no legend box.

Text labels (render exactly, all horizontal):
- title above the left region, navy, bold: "NOT JUST THAT SOMEONE IS THERE - WHERE"
- on the largest circle's radius, burnt amber: "GNSS ONLY - 2 M"
- on the middle circle's radius, slate: "GNSS + VIO - 0.5 M"
- on the smallest circle's radius, teal: "TWO SCOUTS - 0.3 M"
- beside the green centre dot, green: "SURVIVOR"
- right region row 1, slate: "SATELLITE FIX"
- right region row 2, slate: "VISUAL-INERTIAL ODOMETRY"
- right region row 3, teal: "BEARING INTERSECTION"
- footnote along the bottom, small slate: "Derived from sensor spec; two-scout figure is a geometric estimate"

Constraint: 16:9, pure white ground. Only the labels listed. All three circles must share one exact centre, and the teal one must be visibly the smallest. No gore, no bodies - the survivor is a flat glyph.
```

---

## 8 · The first hour — mission timeline  `WHITE`

Candidate for **Slide 4** (*practicability*) or Slide 5.
**Reject if:** the timeline is not strictly left-to-right · "00:58" is missing or wrong · it renders
as a Gantt chart

```
Style: precise editorial-technical infographic for a printed report. PURE WHITE background, hex #FFFFFF, absolutely flat - no gradient, no vignette, no paper texture, no drop shadow falling on the background, no rounded card behind the artwork, pure white right to all four edges. Linework and primary text in deep navy #0B1220. Our system in teal #0E7490. The key outcome in #15803D. Secondary text in slate #475569; light tints in #E2E8F0. Clean geometric sans-serif; ALL text perfectly horizontal. Generous white space, strong left-to-right reading order. No watermarks, no borders, no outer glow, no 3D bevel. 16:9.

Composition: one long horizontal timeline axis running across the full width of the frame, drawn as a thin navy line with fine minute ticks. Six waypoint markers sit along it at increasing spacing, each a small filled circle on the line with a thin vertical stem connecting it to a label.

Labels alternate above and below the line so they never collide: waypoints 1, 3 and 5 label above; waypoints 2, 4 and 6 label below.

Each waypoint circle contains or sits beside a tiny flat icon, in order: a truck; a single large drone ascending; six small drones fanning out; a partially shaded rectangle; a map pin; a fully shaded rectangle.

Waypoint 5 is drawn differently from all the others - a larger green filled circle with a thin green ring around it, and its label is the only one in green.

At the far left end of the axis, a small flat label. At the far right end, the axis continues briefly then ends with a short vertical tick.

Render style: flat editorial timeline figure. Precise, airy, uncrowded. NOT a Gantt chart - there are no horizontal bars of any kind. No axes box, no legend.

Text labels (render exactly, all horizontal, each with a bold time and a plain description line):
- title top-left, navy, bold: "FROM TRUCK TO FIRST SURVIVOR"
- waypoint 1, teal bold then slate: "T+00:00" / "NDRF VEHICLE ARRIVES"
- waypoint 2, teal bold then slate: "T+00:02" / "MOTHERSHIP UP, RELAY LIVE"
- waypoint 3, teal bold then slate: "T+00:04" / "SIX SCOUTS LAUNCHED"
- waypoint 4, teal bold then slate: "T+00:12" / "FIRST LANE SWEPT"
- waypoint 5, green bold then green: "T+00:58" / "FIRST SURVIVOR EXPECTED"
- waypoint 6, teal bold then slate: "T+01:54" / "FULL 5 KM2 SWEPT"
- small label at the far left of the axis, slate: "TWO OPERATORS"
- footnote along the bottom, small slate: "Derived from 2.6 km2/h; expected first detection at half sweep"

Constraint: 16:9, pure white ground. Only the labels listed. No horizontal bars - this is a point timeline, not a Gantt. Waypoint 5 must stand out from the other five.
```

---

## 9 · Stat tiles — six reusable numbers  `WHITE · SQUARE`

Not a slide asset on its own. **Cut them apart and use them individually** wherever a page has a gap.
**Reject if:** the six tiles are not identical in size · any numeral is wrong · they stop reading at
thumbnail size

```
Style: precise editorial-technical infographic for a printed report. PURE WHITE background, hex #FFFFFF, absolutely flat - no gradient, no vignette, no paper texture, no drop shadow falling on the background, no rounded card behind the artwork, pure white right to all four edges. Linework and primary text in deep navy #0B1220. Our numbers in teal #0E7490. The survival figure in #15803D. Secondary text in slate #475569. Clean geometric sans-serif; ALL text perfectly horizontal. Generous white space. No watermarks, no borders, no outer glow, no 3D bevel. 16:9.

Composition: six perfectly square tiles arranged in a grid of three columns by two rows, all exactly the same size, evenly spaced with generous white gaps between them so each tile can be cut out individually. Each tile is bounded by a thin slate hairline square and contains, arranged vertically and centred: one very large numeral at the top taking up roughly half the tile height, one short label beneath it, and one smaller qualifier line at the bottom.

Tile 2 is the only one whose numeral is green; all the others are teal.

Each tile also carries one tiny flat line icon in its upper-left inner corner, small and unobtrusive: a sweep grid; a group of people; a banknote; a pie slice; a downward depth arrow; a pixel grid.

Render style: flat editorial stat-tile set, the discipline of a well-made annual-report figure. Identical tile geometry throughout, generous internal padding, no perspective, no 3D, no glow, no gradient fills. No legend box.

Text labels (render exactly, all horizontal - large numeral, then label, then qualifier):
- tile 1: "2.6" / "KM2 PER HOUR" / "SIX SCOUTS, 30 M AGL"
- tile 2: "+64" / "SURVIVORS PER 100" / "SEARCH DONE IN 6 H, NOT 3 DAYS"
- tile 3: "2.69 L" / "RUPEES, WHOLE SYSTEM" / "86 MINUTES OF CHARTER"
- tile 4: "0.12%" / "OF THE PREPAREDNESS LINE" / "ALL 738 DISTRICTS"
- tile 5: "9 M" / "RADAR THROUGH RUBBLE" / "VITAL SIGNS, NOT SURFACE"
- tile 6: "0.20 M" / "PER THERMAL PIXEL" / "A PERSON IS 8 PIXELS TALL"

Constraint: 16:9, pure white ground, six identical square tiles in a three-by-two grid with wide white gutters so they can be cut apart. Only the labels listed. Every tile identical in size and internal layout.
```

---

## After every render

```bash
cd kestrel-ppt
python3 scripts/whiten.py images/<file>.png     # white ones only; skip #2 and #4
```

Check in this order: **every numeral against `DATA.md`** → the reject line above the prompt → no
curved or rotated text → white to all four edges.

Name the files by prompt: `R2-1-handover-white.png`, `R2-2-handover-dark.png`, and so on, so round 1
and round 2 stay distinguishable in `images/`.
