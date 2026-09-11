# PROMPTS — FINAL · six images, one sitting, deck done

Architecture decided: **the truck is the base, there is no flying mothership** (`DATA.md` §18).
The deck is six slides. **Fifteen of its visuals already exist.** These six are the only ones left.

No more rounds after this.

## The final deck

| Slide | Visual 1 | Visual 2 | Visual 3 |
|---|---|---|---|
| 1 Title | *(no image)* | | |
| 2 Proposed Solution | ✅ `P2.1-frog` | ✅ `P2.2-hero` | ⬜ **#1 SACHET loop** |
| 3 Technical Approach | ⬜ **#2 buried person** | ⬜ **#3 the three tiers** | ✅ `R2-5-hazard-taxonomy` |
| 4 Feasibility & Viability | ⬜ **#4 cost ladder** | ⬜ **#5 when it fails** | ⬜ **#6 whose asset, whose money** |
| 5 Impact & Benefits | ✅ `R1-8-survival-wall` | ✅ `R1-9-uncounted` | ✅ `P5.3-dashboard` |
| 6 References | *(no image)* | | |

**Slide 5 is finished.** Slide 2 needs one. Slides 3 and 4 need the rest.

The pixel ladder is cut — its slot on slide 3 goes to the hazard taxonomy, which is already rendered
and answers a PS bullet we were failing. The ground-sample-distance argument survives as one native
line of text plus `DATA.md` §5, and nobody scores a slide on a figure that repeats a table.

## Run these in two chats

**Chat A:** #1, #2, #3 · **Chat B:** #4, #5, #6 — grouped by slide so within-slide styles match.

Everything below is white/tier-2, prefix pre-merged. Copy the fence, paste, 16:9, 2–3 variants.
Afterwards: `python3 scripts/whiten.py images/<file>.png`. Name them `F1-sachet.png` … `F6-money.png`.

**The one rule that outranks all others: every printed numeral must match `DATA.md`.**

---

## 1 · The SACHET loop → Slide 2

**Reject if:** the return arrow doesn't close the loop · rings in stage 2 route around the concrete
instead of through it · "1.43 BILLION" wrong

```
Style: precise editorial-technical infographic for a printed report. PURE WHITE background, hex #FFFFFF, absolutely flat - no gradient, no vignette, no paper texture, no drop shadow falling on the background, no rounded card behind the artwork, pure white right to all four edges. Linework and primary text in deep navy #0B1220. Our system in teal #0E7490. Status quo in burnt amber #B45309. Success in #15803D. Secondary text in slate #475569; light tints in #E2E8F0. Clean geometric sans-serif; ALL text perfectly horizontal. Generous white space, strong left-to-right reading order. No watermarks, no borders, no outer glow, no 3D bevel. 16:9.

Composition: four numbered stages in one horizontal row reading left to right, evenly spaced with wide white gaps. A single continuous teal arrow links stage 1 to 2 to 3 to 4, then curves down and runs back beneath the whole row to rejoin stage 1, so it reads unmistakably as a closed cycle.

STAGE 1: a cell tower on a small hill in clean line art, emitting three broad concentric broadcast arcs outward across a simplified valley below. A scatter of small phone icons across the valley highlight teal as the arcs pass over them.
STAGE 2: a cutaway of rubble with a phone wedged in a void beneath a heavy concrete slab. Its screen is dark but a small Bluetooth glyph on it is filled teal, and three concentric rings emanate from the phone and are drawn passing straight THROUGH the concrete slab and out of the top of the rubble - the rings must visibly cross the slab, not route around it.
STAGE 3: a small quadcopter flying low over that same rubble with a pale teal reception cone beneath it catching the rings rising from the debris. On its underside, a small circuit board with a visible antenna.
STAGE 4: a grid of map tiles with exactly one tile filled solid teal, and a short arrow from it to the top row of a three-row stacked list beside it.

Above the row, two header lines stacked: the upper in burnt amber with a horizontal strike-through, the lower in teal.

Render style: clean flat technical line illustration with light tint fills. Precise, uncrowded, editorial. Not a flowchart of rectangles. No legend box.

Text labels (render exactly, all horizontal):
- upper header, burnt amber, struck through: "SACHET TODAY - EVACUATE"
- lower header, teal: "SACHET AS A SENSOR - BE DETECTABLE"
- under STAGE 1, two lines, navy then slate: "1. CELL BROADCAST" / "1.43 BILLION PHONES, 36 STATES"
- under STAGE 2, two lines, navy then teal: "2. BLUETOOTH ON" / "RF PASSES THROUGH CONCRETE"
- under STAGE 3, two lines, navy then teal: "3. SCOUT LISTENS" / "ITS OWN QUALCOMM RADIO, ZERO COST"
- under STAGE 4, two lines, navy then green: "4. SECTOR PRIORITISED" / "SWARM RE-TASKED"
- footnote at the bottom, small slate: "C-DOT Cell Broadcast Solution, run by NDMA as SACHET"

Constraint: 16:9, pure white ground. Only the labels listed. The return arrow must close the loop.
```

---

## 2 · What reaches a buried person → Slide 3

**Reject if:** the RGB or thermal band penetrates below the rubble surface — that inverts the whole
argument · the CO2 plume travels downward · any depth numeral wrong

```
Style: precise editorial-technical infographic for a printed report. PURE WHITE background, hex #FFFFFF, absolutely flat - no gradient, no vignette, no paper texture, no drop shadow falling on the background, no rounded card behind the artwork, pure white right to all four edges. Linework and primary text in deep navy #0B1220. Our system and good values in teal #0E7490. Surface-only values in burnt amber #B45309. Success in #15803D. Secondary text and rules in slate #475569; light tints in #E2E8F0. Clean geometric sans-serif; ALL text perfectly horizontal. Generous white space. No watermarks, no borders, no outer glow, no 3D bevel. 16:9.

Composition: a LEFT REGION about 65% of the width and a RIGHT REGION about 30%, separated by a wide white gutter.

LEFT REGION: a vertical cutaway cross-section seen from the side, in the style of a geological section drawing - a collapsed-building rubble pile of broken concrete slabs, bent rebar, splintered timber and soil, drawn as flat light grey and pale tan shapes with clean navy outlines. About two thirds of the way down, one small void containing a single curled human figure in burnt amber, clearly alive and intact.

A small quadcopter hovers above the pile at the top of the frame. Four sensing bands descend from it into the section, each a different colour, each stopping at a visibly different depth, drawn as translucent tapering beams with a hard flat end where they stop:
- a PALE GREY band that stops dead at the very top surface of the rubble and penetrates nothing
- a BURNT AMBER band that also stops dead at that same surface, beside the grey one
- a broad TEAL band that passes deep into the pile and clearly reaches past the human figure
- a GREEN dotted plume that starts at the human figure and travels UPWARD out of the pile toward the drone, opposite in direction to the others

Resting on top of the rubble, one small dropped sensor pod with short spikes into the debris and faint concentric rings radiating downward from it.

A vertical depth scale runs down the left edge of the section with three tick marks.

RIGHT REGION: five small labelled input chips stacked vertically, each with a short arrow feeding right into one tall vertical gauge shaped like a thermometer, filled from the bottom to about three quarters in teal. Two horizontal marker lines cross it: a lower amber line and an upper green line. A green map pin sits at the top.

Render style: precise flat engineering cutaway with clean outlines and light tint fills. No photorealism, no texture. No legend box.

Text labels (render exactly, all horizontal):
- title above the left region, navy, bold: "WHAT ACTUALLY REACHES A BURIED PERSON"
- on the pale grey band where it stops, slate: "RGB - SURFACE ONLY"
- on the burnt amber band where it stops, amber: "THERMAL - SURFACE ONLY"
- on the broad teal band, teal: "PHONE RF - THROUGH 3 M"
- just below that, teal, smaller: "WIFI + BLE, ZERO EXTRA COST"
- at the deepest point the teal band reaches, teal: "UWB VITAL RADAR - 9 M RUBBLE"
- on the rising green plume, green: "CO2 PLUME - 3 PPB"
- at the dropped pod, slate: "ACOUSTIC POD - DROPPED"
- depth ticks top to bottom, small slate: "0 M" / "3 M" / "9 M"
- title above the right region, navy, bold: "WEIGHTED, NOT AND-GATED"
- the five chips top to bottom, small navy: "RGB POSE" / "THERMAL" / "PHONE RF" / "VITAL RADAR" / "CO2 + ACOUSTIC"
- at the lower marker line, amber: "RE-INSPECT"
- at the upper marker line, green: "PUBLISH"
- beside the pin, green: "SURVIVOR + CONFIDENCE"

Constraint: 16:9, pure white ground. Only the labels listed. The grey and amber bands MUST stop at the rubble surface and penetrate nothing - that contrast is the entire point. No gore, no injury detail.
```

---

## 3 · The three tiers → Slide 3 `ARCHITECTURE CHANGED — this replaces the old airframes figure`

The old figure showed a ₹1.11 lakh mothership. There is no mothership. This shows what there is now.
**Reject if:** it shows a large aircraft carrying the compute · the base station is not clearly in the
vehicle · any price wrong

```
Style: precise editorial-technical product illustration for a printed report. PURE WHITE background, hex #FFFFFF, absolutely flat - no gradient, no vignette, no paper texture, no drop shadow falling on the background, no rounded card behind the artwork, pure white right to all four edges. Linework and primary text in deep navy #0B1220. Callout lines and our-system highlights in teal #0E7490. Cost chips in burnt amber #B45309. Secondary text in slate #475569; light tints in #E2E8F0. Clean geometric sans-serif; ALL text perfectly horizontal. Generous white space. No watermarks, no borders, no outer glow. 16:9.

Composition: three elements in one horizontal row at correct relative scale, evenly spaced, each drawn as a clean flat technical illustration with thin teal leader lines running out to labels in the surrounding white space.

LEFT, largest: a cutaway side view of a response vehicle - a box-bodied truck with its rear doors open, revealing a rack inside holding a single-board computer with a finned heatsink, a display, and a power unit connected to the vehicle. A telescopic mast with a small antenna rises from the vehicle roof. The vehicle is clearly the largest and most substantial element in the frame.

CENTRE, small: a simple quadcopter carrying nothing but a radio module and a stub antenna, drawn plainly with no sensors and no gimbal.

RIGHT, small: a quadcopter of the same size as the centre one, but carrying a small circuit board with a visible antenna, a downward camera, and a tiny square thermal sensor. Beneath it, five tiny puck-shaped pods in a row hang from a small rack.

Between the three elements, in the white gutters, one rounded cost chip each.

Render style: flat-shaded technical product illustration with precise navy outlines, service-manual discipline. Matte grey-black airframes, a plain white-and-orange vehicle. No photorealism, no reflections, no environment, no logos.

Text labels (render exactly, all horizontal, on leader lines):
LEFT vehicle: "BASE STATION - IN THE VEHICLE" / "QUALCOMM RB3 GEN 2 - 12 TOPS" / "MAINS POWER, NO WEIGHT LIMIT" / "MAST + HIGH-GAIN ANTENNA"
CENTRE drone: "RELAY - HOLDS THE LINK ALOFT" / "CARRIES NO INTELLIGENCE"
RIGHT drone: "SCOUT x6" / "ARDUINO UNO Q - DRAGONWING QRB2210" / "WIFI + BT ON BOARD" / "FLIR LEPTON ON TWO OF SIX" / "BREADCRUMB PODS x6"
Cost chips in the gutters: teal chip "BASE 59,000", amber chip "RELAY 25,800", amber chip "SCOUT 23,600"
One line along the bottom, navy, bold: "THE BRAIN NEVER LEAVES THE GROUND"

Constraint: 16:9, pure white ground. Only the labels listed. No large aircraft. The vehicle must be visibly the biggest element. No weapons, no military markings.
```

---

## 4 · The cost ladder → Slide 4

**Reject if:** the amber column is not far taller than the teal one · "13,800" or "502" wrong

```
Style: precise editorial-technical infographic for a printed report. PURE WHITE background, hex #FFFFFF, absolutely flat - no gradient, no vignette, no paper texture, no drop shadow falling on the background, no rounded card behind the artwork, pure white right to all four edges. Linework and primary text in deep navy #0B1220. Our system in teal #0E7490. Baseline in burnt amber #B45309. Secondary text in slate #475569; light tints in #E2E8F0. Clean geometric sans-serif; ALL text perfectly horizontal. Generous white space. No watermarks, no borders, no outer glow, no 3D bevel. 16:9.

Composition: a LEFT REGION about 55% of the width and a RIGHT REGION about 40%, separated by a wide white gutter.

LEFT REGION: two columns on one shared thin slate baseline, both exactly the same width, both built from identical flat illustrated bundles of Indian rupee banknotes drawn as stacked rectangles with a banding strap - flat vector, no photorealism, no shadows.
- the FIRST column is very tall and slender, rising almost to the top of the frame, outlined and tinted burnt amber, with a small amber line-art single-engine helicopter resting on top.
- the SECOND column is almost flat: a single thin bundle barely above the baseline, at least twenty times shorter than the first, outlined and tinted teal, with one small truck and six tiny quadcopters laid out in a row on top.
The enormous height difference is the entire point and must be unmistakable at a glance.

RIGHT REGION: one long slim horizontal rounded bar lying on its side, divided by fine ticks into three equal segments. The leftmost portion - a little under half - is filled solid teal; the remainder is filled burnt amber to the bar's right edge. A thin vertical navy line marks the boundary. A tiny teal truck-and-drones icon sits above the teal portion; a tiny amber helicopter above the amber portion.

Render style: flat editorial vector infographic. The columns must read as stacked money, not chart bars - keep the banding visible. No axes, no gridlines, no legend box.

Text labels (render exactly, all horizontal):
- centred above the left region, navy, bold: "RUPEES PER KM2 SURVEYED"
- above the tall column, burnt amber, large: "13,800"
- beneath that, burnt amber, small: "CHARTER HELICOPTER"
- above the short column, teal, large: "502"
- beneath that, teal, small: "KESTREL SWARM"
- in the gutter beside the tall column, burnt amber, very large: "27x"
- above the bar, navy, bold: "SAME MONEY, DIFFERENT PURCHASE"
- under the teal portion, teal, two lines: "2.69 LAKH - 86 MIN" / "THE ENTIRE SYSTEM, ONCE"
- under the amber portion, burnt amber, two lines: "1.89 LAKH PER HOUR" / "AND IT KEEPS RUNNING"
- tick labels, small slate: "1 H" / "2 H" / "3 H"
- bottom-left, small slate: "CHARTER 1.6 L/HR + 18% GST, IAMSAR SWEEP RATE"
- bottom-right, small slate: "KESTREL CAPEX OVER 300 FLIGHT HOURS"

Constraint: 16:9, pure white ground. Only the labels listed. The amber column must be dramatically taller. No coins, no confetti.
```

---

## 5 · When it fails → Slide 4

**Reject if:** the descending arrow breaks · rung 4's lanes are not visibly wider than rung 1's

```
Style: precise editorial-technical infographic for a printed report. PURE WHITE background, hex #FFFFFF, absolutely flat - no gradient, no vignette, no paper texture, no drop shadow falling on the background, no rounded card behind the artwork, pure white right to all four edges. Linework and primary text in deep navy #0B1220. Healthy links in teal #0E7490. Degraded states in burnt amber #B45309. Failure in #B91C1C. Secondary text in slate #475569; light tints in #E2E8F0. Clean geometric sans-serif; ALL text perfectly horizontal. Generous white space. No watermarks, no borders, no outer glow. 16:9.

Composition: four small isometric scenes arranged as descending steps from upper left to lower right, like four rungs of a staircase, each on its own thin flat platform, with wide white space between them. One thick arrow runs down the whole staircase, starting solid teal and fading through pale teal to burnt amber at the bottom - continuous and unbroken from first rung to last.

RUNG 1, top: a response vehicle at the left, one small relay drone above it, six quadcopters over a debris field, all joined by a dense bright teal mesh, plus one link to a cell tower at the edge.
RUNG 2: the same, but the mesh is sparse and thin and the cell tower has a red cross through it.
RUNG 3: no mesh. The quadcopters fly their lanes alone, each with a small glowing data-core cylinder inside, and a trail of small square pods lies on the ground linking back toward the vehicle.
RUNG 4, bottom: two of the six quadcopters lie dark on the debris with small red crosses. The remaining four continue, and their search lanes are drawn visibly wider apart than in rung 1, so the same ground is still covered by fewer aircraft.

Along the bottom edge, one closing line.

Render style: clean flat isometric line illustration with light tint fills, precise and uncrowded. No photorealism, no explosions, no fire.

Text labels (render exactly, all horizontal, one beside each rung):
- rung 1, teal: "FULL MESH + 5G - MBPS"
- rung 2, teal: "TOWER DOWN - PEER MESH ONLY"
- rung 3, slate: "NO LINK - BREADCRUMBS CARRY IT HOME"
- rung 4, burnt amber: "SCOUTS LOST - LANES WIDEN"
- centred along the bottom, navy, bold: "IT GETS SLOWER. IT DOES NOT STOP."

Constraint: 16:9, pure white ground. Only the labels listed. The descending arrow must be unbroken across all four rungs. No weapons, no fire.
```

---

## 6 · Whose asset, whose money → Slide 4

**Reject if:** the teal sliver is comfortably readable — it must look almost too small to see · the
bottom tier is not the widest · "0.12%" or "16,015" wrong

```
Style: precise editorial-technical infographic for a printed report. PURE WHITE background, hex #FFFFFF, absolutely flat - no gradient, no vignette, no paper texture, no drop shadow falling on the background, no rounded card behind the artwork, pure white right to all four edges. Linework and primary text in deep navy #0B1220. Our system in teal #0E7490. Slow paths in burnt amber #B45309. Large neutral quantities and secondary text in slate #475569; light tints in #E2E8F0. Clean geometric sans-serif; ALL text perfectly horizontal. Generous white space. No watermarks, no borders, no outer glow, no 3D bevel. 16:9.

Composition: a LEFT HALF and a RIGHT HALF separated by a wide white gutter.

LEFT HALF: three horizontal plaques stacked vertically, joined by thin vertical navy connectors, each plaque wider than the one above it.
- TOP, narrowest: a small government-building icon beside a tight cluster of small shield icons.
- MIDDLE, wider: a state-outline icon beside a small group of human-figure icons.
- BOTTOM, by far the widest, spanning the full width of this half: filled edge to edge with a dense uniform grid of many tiny identical building icons. Resting on top of it, drawn distinctly larger and in solid teal, one response vehicle with six small quadcopters beside it - so the system clearly belongs to this tier and no other.
A long dashed burnt-amber arrow curves from the top plaque down to the bottom plaque with a small clock icon on it. A separate short solid teal arrow loops tightly within the bottom plaque with a small lightning icon on it.

RIGHT HALF: one very long horizontal bar spanning almost the full width of this half, filled flat slate. Directly beneath its far-left end, a second bar of the same height but almost invisibly short - a teal sliver only a hair wide, needing a thin teal leader line pulled out to its label. Below both bars, a row of three small flat outlined chips.

Render style: flat editorial infographic, institutional-report discipline. The two bars are a direct physical size comparison, not a chart. No axes, no gridlines, no legend box.

Text labels (render exactly, all horizontal):
- above the left half, navy, bold: "WHOSE ASSET"
- top plaque, slate: "NDMA + NDRF - 16 BATTALIONS"
- middle plaque, slate: "SDMA + SDRF - STATE"
- bottom plaque, teal: "DDMA - ALL 738 DISTRICTS"
- on the dashed amber arrow, burnt amber: "NDRF MUST TRAVEL"
- on the teal loop arrow, teal: "DDMA IS ALREADY THERE"
- above the right half, navy, bold: "WHOSE MONEY"
- above the long slate bar, slate: "16,015 CRORE - PREPAREDNESS LINE 2021-26"
- on the leader line from the sliver, teal, two lines: "19.86 CRORE" / "ALL 738 DISTRICTS"
- beside the sliver, teal, very large: "0.12%"
- the three chips, small navy: "NO NEW BUDGET HEAD" / "90:10 FOR NE + HIMALAYAN STATES" / "CSR-ELIGIBLE, SCHEDULE VII"

Constraint: 16:9, pure white ground. Only the labels listed. The teal sliver must be almost imperceptibly thin next to the slate bar - if it is comfortably readable the figure has failed. Do not draw a map of any country.
```

---

## When these six land

The deck is complete. Assemble into `given/SIH2026-IDEA-Presentation-Format.pptx`: keep the template's
own headings, keep the pointer sub-bullets (shrink to 11 pt in a 2.7 in left rail — mandatory, see
`DATA.md` §1a), drop the three dark photographs in as framed panels, let the white diagrams blend
borderless. Delete slide 7. Export PDF. **Six pages, under 10 MB, nothing below 14 pt.**
