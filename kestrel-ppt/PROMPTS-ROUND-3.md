# PROMPTS — ROUND 3 · architecture alternatives · 11 Sep 2026

Eight prompts. Same rules: **each block is complete and self-contained**, prefix pre-merged, copy the
fence and paste. Full reasoning and sources in [`DATA.md`](DATA.md) §13–§17.

**These exist to kill or confirm the mothership.** It was an assumption we never tested, and twelve
searches across the current literature run against it. Generate all eight, then decide from output —
**#1 is literally the decision visual.**

## Two findings that drive everything here

**Qualcomm does not want a drone.** CES 2026: Dragonwing **IQ10** is "the heart of its 2026 robotics
strategy," and the trade press headline is *"Qualcomm targets Nvidia Jetson."* They **bought Arduino**
in Oct 2025 to reach students, and shipped the **UNO Q at $44** — Dragonwing QRB2210 + a real-time
STM32, **Wi-Fi and Bluetooth on board**. What Qualcomm wants from this PS is the Indian student
robotics ecosystem building on Dragonwing instead of Jetson. So the deck should read as **the
Dragonwing reference design for disaster robotics** — and our five-network fusion stack is exactly the
workload that proves RB3 Gen 2's own claim: *"the ability to run more networks simultaneously."*

**Also: LoRa is Semtech, not Qualcomm.** The Qualcomm device-to-device story is **5G sidelink / PC5**
and **Wi-Fi Aware**, and C-U2X research for UAV swarms already exists. Lead with the Qualcomm radio;
keep LoRa only as long-range low-rate backhaul.

## The evidence against the mothership

- **Zhejiang, Science Robotics 2022** — 10 drones through dense bamboo forest, decentralised, **no external facilities**
- **CERBERUS, DARPA SubT winner** — heavy map optimisation at the **base station**; connectivity held by **dropped breadcrumb radios**
- **ACHORD / CARA** (JPL) — droppable relays placed at lowest-SNR points
- **Market-based replanning** (arXiv 2606.01970) — decentralised bidding, **robust to agent loss, no coordinator**
- **EPFL vswarm** — swarming with no GNSS, no ranging, **no explicit communication**
- **Split/distributed DNN inference** — HiDP (DATE 2025), COHORT (2603.10436) — device-to-device collaborative inference

The mothership's one surviving virtue is that it is **easy to draw in six pages**. That is a
communication cost, not an engineering argument.

## Chats

New chats, grouped by kind. Do not reuse rounds 1 or 2.

| Chat | Prompts |
|---|---|
| **New D** — white, architecture | #1, #2, #7 |
| **New E** — white, Qualcomm + hardware | #4, #6 |
| **New F** — white, capability | #3, #5 |
| **Dark** — attach `images/P2.2-hero.png` | #8 |

---

## 1 · The architecture bake-off  `WHITE` — **run this first**

This one exists to make the decision *for* you. Four candidate architectures, one frame.
**Reject if:** column A does not look clearly worse · any tick/cross is in the wrong cell

```
Style: precise editorial-technical infographic for a printed report. PURE WHITE background, hex #FFFFFF, absolutely flat - no gradient, no vignette, no paper texture, no drop shadow falling on the background, no rounded card behind the artwork, pure white right to all four edges. Linework and primary text in deep navy #0B1220. Preferred options in teal #0E7490. Weak options in burnt amber #B45309. Failure marks in #B91C1C, pass marks in #15803D. Secondary text in slate #475569; light tints in #E2E8F0. Clean geometric sans-serif; ALL text perfectly horizontal. Generous white space. No watermarks, no borders, no outer glow, no 3D bevel. 16:9.

Composition: four equal vertical columns side by side, evenly spaced with generous white gutters, each column bounded by a thin slate hairline. Each column has a small schematic diagram in its upper half and a short stack of rows beneath it.

The four schematics, all drawn in the same flat icon style at the same scale, all showing a small debris field along the bottom:
COLUMN A: one large drone high in the centre with lines radiating down to six small drones below it. The large drone is drawn in burnt amber; a small red cross sits on it.
COLUMN B: a truck at ground level on the left drawn in teal, one small relay drone above it, and six small drones spread right; small square nodes are scattered on the ground between them forming a chain.
COLUMN C: seven small drones of identical size in a loose ring, each connected to its neighbours by short teal lines, with one of them carrying a tiny crown glyph.
COLUMN D: seven small drones of identical size in a row, each containing a small chip glyph, joined by one continuous teal band that runs through all seven like a pipeline.

Under each schematic, four rows separated by hairlines, each row holding a short label and either a green tick or a red cross.

Render style: flat comparison figure, spec-sheet discipline, identical column geometry. No perspective, no 3D, no photorealism. No legend box.

Text labels (render exactly, all horizontal):
- title top-left, navy, bold: "FOUR WAYS TO BUILD THIS. WE TESTED OURS."
- column headers, bold: A in burnt amber "FLYING MOTHERSHIP", B in teal "TRUCK IS THE BASE", C in teal "PEER SWARM", D in teal "SWARM IS THE COMPUTER"
- row labels down the left of the whole table, slate: "NO SINGLE POINT OF FAILURE" / "COMPUTE FULLY USED" / "WORKS INSIDE BUILDINGS" / "EVERY NODE QUALCOMM"
- column A marks, top to bottom: cross, cross, cross, tick
- column B marks: tick, tick, tick, tick
- column C marks: tick, cross, tick, tick
- column D marks: tick, tick, tick, tick
- small caption under column A, burnt amber: "OUR FIRST DESIGN"
- footnote along the bottom, small slate: "Evidence: Zhejiang Science Robotics 2022; CERBERUS DARPA SubT; ACHORD; market-based replanning 2026"

Constraint: 16:9, pure white ground. Only the labels listed. All four schematics at identical scale and style. Exactly four columns.
```

---

## 2 · The swarm is the computer  `WHITE`

The most Qualcomm-native idea available to us.
**Reject if:** the pipeline is broken · the chips are not all identical · "5 NETWORKS" missing

```
Style: precise editorial-technical infographic for a printed report. PURE WHITE background, hex #FFFFFF, absolutely flat - no gradient, no vignette, no paper texture, no drop shadow falling on the background, no rounded card behind the artwork, pure white right to all four edges. Linework and primary text in deep navy #0B1220. Compute and our system in teal #0E7490. Secondary text in slate #475569; light tints in #E2E8F0. Clean geometric sans-serif; ALL text perfectly horizontal. Generous white space, strong left-to-right reading order. No watermarks, no borders, no outer glow, no 3D bevel. 16:9.

Composition: an UPPER BAND and a LOWER BAND separated by generous white space.

UPPER BAND: seven small identical drone icons in one horizontal row, evenly spaced. Six of them are drawn at the same small size; the seventh, at the far right, is drawn as a truck instead of a drone. Inside each of the seven shapes sits one identical small square chip glyph, teal.

Running horizontally through all seven shapes, one continuous teal band like a pipeline, entering the leftmost and exiting the rightmost. Where the band passes through each shape it is drawn as a short segment with a different simple hatch pattern, so the seven segments are visibly different stages of one pipeline rather than seven separate things.

Above the band, five thin parallel lines run the full width in a light teal tint, stacked close together, suggesting five concurrent streams travelling along the same pipeline.

LOWER BAND: a horizontal row of five small square cards, each with a tiny icon and a short label, sitting beneath the pipeline with thin leader lines connecting each card up to the five parallel lines.

Render style: flat systems figure, clean pipeline diagram, thin precise linework, airy. No perspective, no 3D. No legend box.

Text labels (render exactly, all horizontal):
- title top-left, navy, bold: "SEVEN NPUs, ONE PIPELINE"
- subtitle beneath, slate: "NO SINGLE BRAIN TO LOSE"
- above the five parallel lines, teal, bold: "5 NETWORKS AT ONCE"
- label on the leftmost drone, slate: "SCOUT 1 - HEAD LAYERS"
- label on the rightmost truck, slate: "VEHICLE - TAIL LAYERS"
- the five cards, small navy: "RGB DETECTION" / "THERMAL" / "HAZARD CLASS" / "VIO POSE" / "AUDIO"
- footnote along the bottom, small slate: "Device-to-device split inference. Dragonwing RB3 Gen 2: run more networks simultaneously."

Constraint: 16:9, pure white ground. Only the labels listed. The pipeline band must be continuous through all seven nodes. All seven chip glyphs identical.
```

---

## 3 · Breadcrumbs — how the link gets inside  `WHITE`

Replaces the hovering relay with the DARPA-validated answer.
**Reject if:** the mesh does not visibly reach deeper than the drone does · fewer than four nodes

```
Style: precise editorial-technical infographic for a printed report. PURE WHITE background, hex #FFFFFF, absolutely flat - no gradient, no vignette, no paper texture, no drop shadow falling on the background, no rounded card behind the artwork, pure white right to all four edges. Linework and primary text in deep navy #0B1220. Live links and our system in teal #0E7490. Dead zones in burnt amber #B45309. Secondary text in slate #475569; light tints in #E2E8F0. Clean geometric sans-serif; ALL text perfectly horizontal. Generous white space. No watermarks, no borders, no outer glow, no 3D bevel. 16:9.

Composition: a vertical cutaway cross-section, seen from the side, of a partially collapsed multi-storey building with three floors and a rubble-filled basement, drawn as flat pale grey structural shapes with clean navy outlines. The building occupies the right two thirds of the frame; open ground and a truck occupy the left third.

A small drone flies in through a broken opening on the upper floor. Behind it, a trail of four small square puck-shaped nodes lies where it has dropped them: one outside the building, one just inside the opening, one at a stairwell on the middle floor, one at the edge of the basement. Short teal arcs link each node to the next in an unbroken chain running from the truck all the way to the deepest node.

At the deepest node, a small teal reception cone points further down into the rubble toward a small amber marker.

For contrast, in the upper left open sky, one drone hovers alone at altitude with a single long amber dashed line dropping from it that stops dead at the building's roof and does not continue inside.

Render style: flat engineering cutaway, clean architectural section discipline, thin linework, light tint fills. No perspective, no 3D, no photorealism. No legend box.

Text labels (render exactly, all horizontal):
- title top-left, navy, bold: "THE LINK GOES WHERE THE DRONE CANNOT"
- beside the hovering drone at altitude, burnt amber: "RELAY AT 100 M - STOPS AT THE ROOF"
- beside the trail of nodes, teal: "BREADCRUMB RADIOS - DROPPED AS IT FLIES"
- at the deepest node, teal: "MESH REACHES THE BASEMENT"
- at the truck, slate: "VEHICLE BASE"
- footnote along the bottom, small slate: "Dropped-relay meshing as used by CERBERUS, DARPA Subterranean Challenge winner"

Constraint: 16:9, pure white ground. Only the labels listed. The amber line from the high drone must visibly stop at the roof; the teal chain must visibly continue to the basement. No people, no bodies.
```

---

## 4 · The Qualcomm ladder  `WHITE`

Answers "why Qualcomm" with their own 2026 product line.
**Reject if:** any price or part number is wrong · it reads as an advertisement

```
Style: precise editorial-technical infographic for a printed report. PURE WHITE background, hex #FFFFFF, absolutely flat - no gradient, no vignette, no paper texture, no drop shadow falling on the background, no rounded card behind the artwork, pure white right to all four edges. Linework and primary text in deep navy #0B1220. Our system in teal #0E7490. Scale-path items in slate #475569. Light tints in #E2E8F0. Clean geometric sans-serif; ALL text perfectly horizontal. Generous white space. No watermarks, no borders, no outer glow, no 3D bevel, no brand logos of any kind. 16:9.

Composition: three rectangular plaques arranged as ascending steps from lower left to upper right, each plaque wider and taller than the one before it, connected by a thin teal arrow that climbs from the first to the third and then continues briefly beyond.

Each plaque contains a simple flat outline of a circuit board with a heatsink, drawn at a size proportional to the plaque, plus three short text lines to its right.

The first two plaques are outlined in teal; the third in slate.

Beneath the three plaques, one horizontal row of three small flat chips.

Render style: flat editorial product-ladder figure, spec-sheet discipline. No photorealism, no reflections, no logos, no brand marks. No legend box.

Text labels (render exactly, all horizontal):
- title top-left, navy, bold: "ONE VENDOR, THREE TIERS, ONE TOOLCHAIN"
- plaque 1, three lines: "ARDUINO UNO Q" / "DRAGONWING QRB2210 + STM32" / "3,900 RUPEES - THE SCOUT"
- plaque 2, three lines: "DRAGONWING RB3 GEN 2" / "QCS6490 - 12 TOPS HEXAGON" / "50,000 RUPEES - THE BASE"
- plaque 3, three lines: "DRAGONWING IQ10" / "18-CORE, CES 2026" / "THE SCALE PATH"
- the three chips in a row beneath, small navy: "QUALCOMM AI HUB" / "QNN RUNTIME" / "QUALCOMM LINUX"
- caption at the top right, teal: "WI-FI AND BLUETOOTH ON BOARD - THE SCOUT SNIFFS PHONES FOR FREE"
- footnote along the bottom, small slate: "Same compile path from a 3,900-rupee scout to an 18-core platform"

Constraint: 16:9, pure white ground. Only the labels listed. Do not draw any company logo or wordmark. Do not make it look like an advertisement - this is a spec figure.
```

---

## 5 · Say what you are looking for  `WHITE`

Open-vocabulary search. Answers PS bullets 4 and 6 in a way a fixed class list cannot.
**Reject if:** the typed phrase is not legible · the three result tiles are not visibly re-ranked

```
Style: precise editorial-technical infographic for a printed report. PURE WHITE background, hex #FFFFFF, absolutely flat - no gradient, no vignette, no paper texture, no drop shadow falling on the background, no rounded card behind the artwork, pure white right to all four edges. Linework and primary text in deep navy #0B1220. Our system in teal #0E7490. Matches in #15803D. Secondary text in slate #475569; light tints in #E2E8F0. Clean geometric sans-serif; ALL text perfectly horizontal. Generous white space, strong left-to-right reading order. No watermarks, no borders, no outer glow, no 3D bevel. 16:9.

Composition: three stages reading left to right, linked by two thin teal arrows.

STAGE 1, left: a simple rounded rectangle drawn as a text-input field with a blinking cursor bar at the end of a short typed phrase inside it, and a small keyboard glyph beneath.
STAGE 2, centre: a small flat chip glyph with three short lines radiating from its right side into three small square thumbnail frames stacked vertically. Each thumbnail contains a very simple flat scene sketch. The top thumbnail has a green outline; the lower two have slate outlines.
STAGE 3, right: a small tactical map grid in which three cells are shaded, one strongly in green and two lightly in slate, with a short numbered list of three rows beside it.

Above the whole sequence, two contrasting header lines stacked: the upper in burnt amber with a horizontal strike-through, the lower in teal.

Render style: flat interface-and-systems figure, clean product-diagram discipline, airy. No perspective, no 3D, no screenshot realism. No legend box.

Text labels (render exactly, all horizontal):
- upper header, burnt amber, struck through: "EIGHT FIXED CLASSES"
- lower header, teal: "OR JUST SAY WHAT YOU ARE LOOKING FOR"
- inside the text input field, navy: "blue tarpaulin near the school"
- at the chip glyph, teal: "VISION-LANGUAGE MODEL, ON DEVICE"
- beside the green thumbnail, green: "MATCH 0.91"
- beside the two slate thumbnails, slate: "0.44" and "0.31"
- above the map grid, slate: "SWARM RE-TASKED"
- footnote along the bottom, small slate: "Open-vocabulary aerial search: UAV-VLRR; AirHunt; split VLM inference for disaster response"

Constraint: 16:9, pure white ground. Only the labels listed. The typed phrase must be lower-case and legible exactly as written. No photorealism in the thumbnails - simple flat sketches only.
```

---

## 6 · The payload bay — what the flyer actually carries  `WHITE`

Marsupial done properly: it carries things that go where drones cannot.
**Reject if:** it shows the aircraft carrying other drones · fewer than three payload types

```
Style: precise editorial-technical infographic for a printed report. PURE WHITE background, hex #FFFFFF, absolutely flat - no gradient, no vignette, no paper texture, no drop shadow falling on the background, no rounded card behind the artwork, pure white right to all four edges. Linework and primary text in deep navy #0B1220. Our system in teal #0E7490. Secondary text in slate #475569; light tints in #E2E8F0. Clean geometric sans-serif; ALL text perfectly horizontal. Generous white space. No watermarks, no borders, no outer glow, no 3D bevel. 16:9.

Composition: an upper region and a lower region.

UPPER REGION, centred: a flat technical underside view of a multirotor aircraft with a rack of six identical release stations arranged in a row beneath its body, each station drawn as a small bracket with a servo pin. Three of the six stations are occupied by visibly different payloads; three are empty.

From each of the three occupied stations, a thin teal leader line drops down into the lower region to its own labelled panel.

LOWER REGION: three panels in a horizontal row, evenly spaced, each bounded by a thin slate hairline. Each panel contains a flat line drawing of one payload shown in use on a small patch of rubble:
- PANEL 1: a small square puck resting on rubble with teal arcs radiating outward and sideways.
- PANEL 2: a small spiked pod pressed into the rubble surface with thin concentric rings radiating downward into the debris.
- PANEL 3: a small tracked crawler part-way into a dark gap between two slabs, with a thin teal tether line trailing back out of the gap.

Render style: flat engineering figure, clean technical illustration, thin precise linework, light tint fills. No perspective, no 3D, no photorealism. No legend box.

Text labels (render exactly, all horizontal):
- title top-left, navy, bold: "SIX RELEASE STATIONS. NONE OF THEM CARRY DRONES."
- at the release rack, slate: "SERVO PIN-PULL x6 - FROM OUR OWN PRD"
- panel 1, navy then slate: "BREADCRUMB RADIO" / "EXTENDS THE MESH INDOORS"
- panel 2, navy then slate: "ACOUSTIC + CO2 POD" / "KEEPS LISTENING AFTER WE FLY ON"
- panel 3, navy then slate: "TETHERED CRAWLER" / "ENTERS THE VOID ITSELF"
- footnote along the bottom, small slate: "Marsupial deployment: the platform releases what reaches further than it can"

Constraint: 16:9, pure white ground. Only the labels listed. The aircraft must NOT be shown carrying or releasing other aircraft. Exactly six release stations, three occupied. No people, no bodies.
```

---

## 7 · No one is in charge  `WHITE`

How a leaderless swarm allocates work. The hardest idea to draw, so draw it as an auction.
**Reject if:** it shows a central node issuing orders · the lost drone does not visibly get covered

```
Style: precise editorial-technical infographic for a printed report. PURE WHITE background, hex #FFFFFF, absolutely flat - no gradient, no vignette, no paper texture, no drop shadow falling on the background, no rounded card behind the artwork, pure white right to all four edges. Linework and primary text in deep navy #0B1220. Our system in teal #0E7490. Loss in #B91C1C. Success in #15803D. Secondary text in slate #475569; light tints in #E2E8F0. Clean geometric sans-serif; ALL text perfectly horizontal. Generous white space. No watermarks, no borders, no outer glow, no 3D bevel. 16:9.

Composition: two panels side by side, separated by a wide white gutter, each containing the same flat top-down map divided into a grid of twelve rectangular search cells.

LEFT PANEL: five small drone icons positioned around the map, none of them larger or more prominent than the others. From each drone, two or three thin dashed teal lines reach toward nearby cells, and a tiny numeric tag sits on each line. Three cells are shaded solid teal, each with one solid line connecting it to the drone that claimed it.

RIGHT PANEL: the same map and the same five drone positions, except one drone is drawn dark with a small red cross on it and its lines are gone. The cells that drone had claimed are now shaded teal and connected by solid lines to two of the remaining drones, and those cells are drawn slightly larger to show the lanes widening. A small green tick sits in the corner of the panel.

Above each panel, a short caption. Above the whole figure, one title line.

Render style: flat top-down systems figure, clean and airy, thin precise linework. No perspective, no 3D. No legend box. Do not draw any central hub, tower, server or command node anywhere in the figure.

Text labels (render exactly, all horizontal):
- title top-left, navy, bold: "NO ONE IS IN CHARGE. NOTHING STOPS."
- caption above LEFT panel, teal: "EVERY SCOUT BIDS FOR CELLS"
- caption above RIGHT panel, teal: "ONE IS LOST - THE OTHERS RE-BID"
- small label beside one dashed bid line in the left panel, slate: "BID = TIME + BATTERY"
- beside the dark drone in the right panel, red: "SCOUT 4 LOST"
- beside the green tick, green: "COVERAGE HELD"
- footnote along the bottom, small slate: "Market-based task allocation; robust to agent loss, no coordinator required"

Constraint: 16:9, pure white ground. Only the labels listed. There must be NO central command node of any kind - that absence is the entire point. All drone icons the same size.
```

---

## 8 · Seeing through the dust  `DARK, CINEMATIC`

Event-camera sensing where a normal camera is blind. Attach `images/P2.2-hero.png` first.
**Reject if:** the two halves do not show the same scene · the right half is not clearly readable

```
Style: premium defence-tech mission-control aesthetic. Deep navy-charcoal ground (#0B1220), cyan-teal primary accent (#22D3EE), warm amber-orange secondary accent (#F59E0B), restrained holographic HUD elements, cinematic lighting, photorealistic. No watermarks, no borders, no stock-photo gloss, no lens flare. All specified text in a clean geometric sans-serif, uppercase, small. 16:9 widescreen.

Composition: one frame split down the middle by a thin vertical cyan rule into two halves showing the SAME scene at the same instant from the same viewpoint.

LEFT HALF: a conventional camera view inside a collapsed concrete structure, almost entirely obscured by thick swirling dust - a near-white haze with only the faintest suggestion of a slab edge. Almost nothing is discernible. Muddy, blown-out, useless.

RIGHT HALF: the identical scene rendered as an event-camera output - a sparse, high-contrast field of individual cyan and amber pixel-level dots on deep black, where only things that CHANGED are drawn. The dust is nearly invisible because it is diffuse, but a human arm and hand raised in a gap between two slabs is rendered in crisp bright cyan outline dots, clearly recognisable as a moving hand, because motion is what this sensor sees.

Lighting: left half flat, hazed and overexposed; right half near-black with luminous sparse dots.

Text labels (render exactly, small HUD tags):
- top of LEFT half, amber: "RGB - BLIND IN DUST"
- top of RIGHT half, cyan: "EVENT CAMERA - MOTION ONLY"
- beside the hand in the right half, cyan: "MOVEMENT DETECTED"
- bottom right of frame, in #94A3B8: "MICROSECOND LATENCY, 120 DB RANGE"

Constraint: 16:9. Exactly these four labels, nothing else. Both halves must show the same viewpoint and the same instant. Show only a hand and forearm - no face, no body, no injury, no blood.
```

---

## After every render

```bash
cd kestrel-ppt && python3 scripts/whiten.py images/<file>.png   # white ones only, skip #8
```

Name them `R3-1-bakeoff.png` … `R3-8-event-dust.png`.

**Then make the architecture call.** If #1, #2, #3 and #7 come back strong, the mothership is dead
and `slides/` needs rewriting — `DATA.md` §0 corrections 1 and 3 and every "mothership" mention
depend on the outcome. That rewrite is mechanical once you decide; say the word and I'll do it.
