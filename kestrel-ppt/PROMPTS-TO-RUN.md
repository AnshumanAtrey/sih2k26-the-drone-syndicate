# PROMPTS TO RUN — 11 Sep 2026

Nine prompts. **Each block below is complete and self-contained** — the style prefix is already
merged in, so copy the whole fenced block and paste. No assembly.

All nine are **tier 2: pure white background**, so they drop straight onto the white SIH template
with no frame and no visible edge. The three tier-1 dark images (`P2.1` frog, `P2.2` hero,
`P5.3` dashboard) are **done and stay dark** — photographs and screenshots are windows; diagrams are
page furniture (`STYLE.md`).

After each render: `python3 scripts/whiten.py images/<file>.png` snaps near-white to pure `#FFFFFF`
and trims the margin. Add `--transparent` only if you end up on a non-white slide.

## The five mistakes that produced bad images, and the rule each one became

| What went wrong | Rule now baked into every prompt below |
|---|---|
| Cost ladder compared **₹1.89 L/hr against ₹2.69 L** — a rate against a capital cost, as two heights | **Only ever compare like with like as a physical magnitude.** Different units get separate regions with their own labels |
| Survival clock was **radial** — implied cyclic time, forced curved text, read as a speedometer, had no title | **Time runs left to right. Never radial. Every diagram carries a title line.** All text horizontal |
| Fusion gate's three gates **all needed line of sight**, so it could not see a buried person | Content checked against the population it must cover, not just against the rubric |
| Airframe rendered **8 arms instead of 6** | **Models cannot count reliably above ~5.** Where a count carries meaning it is stated as "exactly N" twice; where it does not, the prompt says counts are illustrative so a good image is not rejected over them |
| Pixel ladder ignored "same size in all three panels"; `Tangshan` rendered `Tangshaan` | Identical objects are specified as **"the identical shape, copied"**. Long proper nouns are kept out of small footnotes where possible |

**Reject rule that overrides everything:** the **printed numerals** must be exact. Counts of repeated
icons are illustrative. A wrong numeral is worse than a plain chart.

---

## 1 · P2.3 — The SACHET loop  `NEW`

**Slide 2** · crop to a wide band (~4:1) · replaces the retired `P2.3-15km2-twice.png`
**Reject if:** the return arrow does not close back on stage 1 · the rings in stage 2 go around the
concrete instead of through it · the scout has no recognisable phone on it · "1.43 BILLION" is wrong

```
Style: precise editorial-technical infographic for a printed report. PURE WHITE background, hex #FFFFFF, absolutely flat - no gradient, no vignette, no paper texture, no coloured wash, no drop shadow falling on the background, no rounded card or panel behind the artwork, pure white right to all four edges. Linework and primary text in deep navy #0B1220. Our system and good values in teal #0E7490. Status quo and problem values in burnt amber #B45309. Rescue and success in #15803D. Secondary text, footnotes and rules in slate #475569; light tints in #E2E8F0. Clean geometric sans-serif; ALL text perfectly horizontal - never curved, never rotated, never set along an arc. Generous white space, strong left-to-right reading order. No watermarks, no borders, no frames, no outer glow, no lens flare, no 3D bevel, no stock-illustration gloss. 16:9.

Composition: four numbered stages in one horizontal row reading left to right, evenly spaced with wide white gaps between them. A single continuous teal arrow links stage 1 to 2 to 3 to 4, then curves down and runs back underneath the whole row to rejoin stage 1, so the process is unmistakably a closed cycle.

STAGE 1: a cell tower on a small hill, drawn as clean line art, emitting three broad concentric broadcast arcs outward and downward across a simplified valley. A scatter of small phone icons across the valley are highlighted in teal as the arcs pass over them.
STAGE 2: a cutaway of a rubble pile. Wedged in a void beneath a heavy concrete slab is a phone, its screen dark, with a small Bluetooth glyph on it filled teal. Three concentric rings emanate from the phone and are drawn passing straight THROUGH the concrete slab and continuing out of the top of the rubble - the rings must visibly cross the slab, not route around it.
STAGE 3: a small quadcopter flying low above that same rubble, with a pale teal reception cone beneath it catching the rings rising out of the debris. Mounted on the quadcopter's underside and clearly recognisable as a smartphone, its camera facing down.
STAGE 4: a small grid of map tiles in which exactly one tile is filled solid teal, with a short arrow from it to the top row of a three-row stacked list beside it.

Above the whole row, two short header lines stacked one above the other: the upper line in burnt amber with a horizontal strike-through line across it, the lower line in teal.

Render style: clean flat technical line illustration with light tint fills. Precise, uncrowded, editorial. Not a flowchart of rectangles. No legend box.

Text labels (render exactly, all horizontal):
- upper header line, burnt amber, struck through: "SACHET TODAY - EVACUATE"
- lower header line, teal: "SACHET AS A SENSOR - BE DETECTABLE"
- under STAGE 1, two lines, navy then slate: "1. CELL BROADCAST" / "1.43 BILLION PHONES, 36 STATES"
- under STAGE 2, two lines, navy then teal: "2. BLUETOOTH ON" / "RF PASSES THROUGH CONCRETE"
- under STAGE 3, two lines, navy then teal: "3. SCOUT LISTENS" / "ITS OWN PHONE RADIO, ZERO COST"
- under STAGE 4, two lines, navy then green: "4. SECTOR PRIORITISED" / "SWARM RE-TASKED"
- one thin footnote line at the bottom, small slate: "C-DOT Cell Broadcast Solution, run by NDMA as SACHET"

Constraint: 16:9, pure white ground. Only the labels listed above, nothing else. The return arrow must close the loop.
```

---

## 2 · P3.1 — The pixel ladder  `REGENERATE IN LIGHT`

**Slide 3** · crop to a wide band (~4:1) · replaces the dark `P3.1-pixel-ladder.png`
**Reject if:** the human silhouette is a different size in any panel · any of the nine numerals is
wrong · the left panel's person is not almost invisible

```
Style: precise editorial-technical infographic for a printed report. PURE WHITE background, hex #FFFFFF, absolutely flat - no gradient, no vignette, no paper texture, no coloured wash, no drop shadow falling on the background, no rounded card or panel behind the artwork, pure white right to all four edges. Linework and primary text in deep navy #0B1220. Our system and good values in teal #0E7490. Status quo and problem values in burnt amber #B45309. Secondary text, footnotes and rules in slate #475569; light tints in #E2E8F0. Clean geometric sans-serif; ALL text perfectly horizontal - never curved, never rotated. Generous white space, strong left-to-right reading order. No watermarks, no borders, no frames, no outer glow, no 3D bevel, no stock-illustration gloss. 16:9.

Composition: three square panels in one horizontal row, evenly spaced with wide white gaps, all three exactly the same size. Each panel shows the same pale grey rubble field, drawn as flat light-grey debris shapes on a very light #E2E8F0 tint.

In the centre of every panel sits the identical top-down silhouette of a person lying prone, in burnt amber - literally the same silhouette shape copied three times, at exactly the same size, in the same orientation, in all three panels. The person's size never changes between panels. Only the grid changes.

Over each panel a square pixel grid is drawn in slate, and the grid is drastically different between panels. Where a grid cell overlaps the body, that cell is tinted; the strength of the tint reflects how much of the cell the body fills.
LEFT PANEL: an extremely coarse grid, only two cells across. The whole person sits inside a small fraction of one enormous cell, which is tinted so faintly it is barely distinguishable from the surrounding rubble.
CENTRE PANEL: a medium grid, about six cells across. The person occupies most of one cell, tinted a clear solid amber.
RIGHT PANEL: a fine grid, about twenty cells across. The person spans roughly eight cells tall and two wide, each of those cells tinted solid teal, so the body's shape and posture are readable from the tinted cells alone.

Below the three panels, one thin horizontal teal rule spanning the full width, with a short formula sitting centred on it.

Render style: precise flat technical figure, the look of a well-made engineering diagram in a journal. Not a chart. No axes, no bars, no legend.

Text labels (render exactly, all horizontal):
- above LEFT panel, three lines, slate: "MLX90640 32x24" / "2.68 M PER PIXEL" / "10% OF ONE PIXEL"
- below LEFT panel, burnt amber, bold: "INVISIBLE"
- above CENTRE panel, three lines, slate: "MLX90640 NARROW" / "0.98 M PER PIXEL" / "71% OF ONE PIXEL"
- below CENTRE panel, burnt amber, bold: "MARGINAL"
- above RIGHT panel, three lines, slate: "FLIR LEPTON 3.5 160x120" / "0.20 M PER PIXEL" / "8 X 2 PIXELS"
- below RIGHT panel, teal, bold: "DETECTABLE - AND SHAPED"
- centred on the bottom rule, small slate: "GSD = 2 H TAN(FOV/2) / PIXELS   AT H = 30 M"

Constraint: 16:9, pure white ground. Only the labels listed. The human silhouette must be identical in size and shape in all three panels - this is the single most important requirement. Exact grid cell counts are illustrative; the printed numerals must be exact.
```

---

## 3 · P3.2 — What reaches a buried person  `NEW`

**Slide 3** · keep 16:9 · replaces the retired `P3.2-gate.png`
**Reject if:** the RGB or thermal band penetrates below the rubble surface — that inverts the whole
argument · the CO2 plume travels downward instead of up · any depth numeral is wrong

```
Style: precise editorial-technical infographic for a printed report. PURE WHITE background, hex #FFFFFF, absolutely flat - no gradient, no vignette, no paper texture, no coloured wash, no drop shadow falling on the background, no rounded card behind the artwork, pure white right to all four edges. Linework and primary text in deep navy #0B1220. Our system and good values in teal #0E7490. Status quo and surface-only values in burnt amber #B45309. Rescue and success in #15803D. Secondary text and rules in slate #475569; light tints in #E2E8F0. Clean geometric sans-serif; ALL text perfectly horizontal - never curved, never rotated. Generous white space. No watermarks, no borders, no frames, no outer glow, no 3D bevel. 16:9.

Composition: a LEFT REGION about 65% of the width and a RIGHT REGION about 30%, separated by a wide white gutter.

LEFT REGION: a vertical cutaway cross-section seen from the side, in the style of a geological section drawing - a collapsed-building rubble pile of broken concrete slabs, bent rebar, splintered timber and soil, drawn as flat light grey and pale tan shapes with clean navy outlines. About two thirds of the way down the pile, one small void containing a single curled human figure in burnt amber, clearly alive and intact.

A small quadcopter hovers above the pile at the top of the frame. Four sensing bands descend from it into the section, each a different colour, each stopping at a visibly different depth, each drawn as a translucent tapering beam with a hard flat end where it stops:
- a PALE GREY band that stops dead at the very top surface of the rubble and penetrates nothing at all
- a BURNT AMBER band that also stops dead at that same top surface, right beside the grey one
- a broad TEAL band that passes deep into the pile and clearly reaches past the human figure
- a separate GREEN dotted plume that starts at the human figure and travels UPWARD out of the pile toward the drone, in the opposite direction to the other three

Resting on top of the rubble is one small dropped sensor pod with short spikes into the debris and faint concentric rings radiating downward from it.

A vertical depth scale runs down the left edge of the section with three tick marks.

RIGHT REGION: five small labelled input chips stacked vertically, each with a short arrow feeding rightward into one tall vertical gauge shaped like a thermometer. The gauge is filled from the bottom to about three quarters in teal. Two horizontal marker lines cross it: a lower amber line and an upper green line. A green map pin sits at the very top of the gauge.

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
- depth scale ticks top to bottom, small slate: "0 M" / "3 M" / "9 M"
- title above the right region, navy, bold: "WEIGHTED, NOT AND-GATED"
- the five chips top to bottom, small navy: "RGB POSE" / "THERMAL" / "PHONE RF" / "VITAL RADAR" / "CO2 + ACOUSTIC"
- at the lower marker line, amber: "RE-INSPECT"
- at the upper marker line, green: "PUBLISH"
- beside the pin at the top, green: "SURVIVOR + CONFIDENCE"

Constraint: 16:9, pure white ground. Only the labels listed. The grey and amber bands MUST stop at the rubble surface and penetrate nothing - that contrast is the entire point of the figure. No gore, no injury detail.
```

---

## 4 · P3.3 — Two airframes  `REGENERATE IN LIGHT`

**Slide 3** · keep 16:9 · replaces the dark `P3.3-airframes.png`, and fixes its 8-arm error
**Reject if:** the large aircraft does not have **exactly six** arms · the phone on the small aircraft
is not recognisable as a phone · any price is wrong

```
Style: precise editorial-technical product illustration for a printed report. PURE WHITE background, hex #FFFFFF, absolutely flat - no gradient, no vignette, no paper texture, no drop shadow falling on the background, no rounded card behind the artwork, pure white right to all four edges. Linework and primary text in deep navy #0B1220. Callout lines and our-system highlights in teal #0E7490. Cost chips for the cheap unit in burnt amber #B45309. Secondary text in slate #475569; light tints in #E2E8F0. Clean geometric sans-serif; ALL text perfectly horizontal. Generous white space. No watermarks, no borders, no frames, no outer glow, no lens flare. 16:9.

Composition: two multirotor aircraft side by side at correct relative scale, seen in three-quarter view, both drawn as clean partial exploded diagrams with the top shell lifted and floating slightly above the body to reveal the internal stack. Thin teal leader lines run from each internal module out to a label in the surrounding white space.

LEFT, occupying about 60% of the frame: a large heavy-lift multirotor with EXACTLY SIX motor arms arranged evenly in a hexagon - six arms, six motors, six propellers, no more and no fewer. Revealed inside: a single-board computer with a finned heatsink at the centre, a separate smaller flight-controller board behind it, a compact gimbal underneath holding one small square thermal sensor module and one larger camera lens, a whip antenna on top, and two battery packs at the rear.

RIGHT, noticeably smaller: a minimal quadcopter with exactly four short arms and propeller guards. Revealed inside: a modern smartphone mounted flat and centrally as the aircraft's main computer, unmistakably a phone with a visible camera array, its screen facing up and its camera facing down through the frame; a tiny flight-controller board beneath it; a small radio module; one battery pack.

In the white gutter between the two aircraft, two rounded cost chips stacked vertically.

Render style: clean flat-shaded technical product illustration with precise navy outlines, in the manner of an exploded diagram in a service manual. Matte grey-black airframes. No photorealism, no reflections, no environment.

Text labels (render exactly, all horizontal, on leader lines):
LEFT aircraft: "QUALCOMM RB3 GEN 2 - 12 TOPS" / "PIXHAWK 2.4.8 - PX4" / "FLIR LEPTON 3.5" / "LoRa SX1262 HUB" / "4S 5000 MAH x2"
RIGHT aircraft: "RECYCLED SNAPDRAGON PHONE" / "HEXAGON NPU - QNN" / "LoRa NODE"
Cost chips in the centre gutter: a teal-outlined chip reading "MOTHERSHIP 1.11 L" and an amber-outlined chip reading "SCOUT 25,600"

Constraint: 16:9, pure white ground. Only the labels listed. The large aircraft must have exactly six arms - count them. No weapons, no military markings, no national insignia.
```

---

## 5 · P4.1 — The cost ladder  `NEW — v1 was rejected`

**Slide 4** · keep 16:9 · replaces `P4.1-cost-ladder-REDO.png`
**Reject if:** the amber column is not far taller than the teal one · the two columns are compared
against different units · "13,800" or "502" is wrong

> v1 stacked **₹1.89 L/hr against ₹2.69 L** — a rate against a capital cost — so no arrangement of
> heights could be read correctly, and the model made the helicopter stack taller than its own label
> justified. v2 puts the like-for-like comparison (**₹ per km² surveyed**) in one region, and moves
> the "86 minutes" idea into a separate meter where it cannot be misread as a height.

```
Style: precise editorial-technical infographic for a printed report. PURE WHITE background, hex #FFFFFF, absolutely flat - no gradient, no vignette, no paper texture, no drop shadow falling on the background, no rounded card behind the artwork, pure white right to all four edges. Linework and primary text in deep navy #0B1220. Our system and good values in teal #0E7490. Status quo and baseline values in burnt amber #B45309. Secondary text and rules in slate #475569; light tints in #E2E8F0. Clean geometric sans-serif; ALL text perfectly horizontal. Generous white space. No watermarks, no borders, no frames, no outer glow, no 3D bevel. 16:9.

Composition: a LEFT REGION about 55% of the width and a RIGHT REGION about 40%, separated by a wide white gutter.

LEFT REGION: two columns standing on one shared thin slate baseline, both exactly the same width, both built from identical flat illustrated bundles of Indian rupee banknotes drawn as simple stacked rectangles with a banding strap - flat vector illustration, no photorealism, no shadows.
- the FIRST column is very tall and slender, rising almost to the top of the frame, made of many stacked bundles, outlined and tinted in burnt amber. A small amber line-art single-engine helicopter rests on top of it.
- the SECOND column is almost flat: a single thin bundle barely above the baseline, at least twenty times shorter than the first, outlined and tinted in teal. One small hexacopter and six tiny quadcopters are laid out in a neat row on top of it.
The enormous height difference between the two columns is the entire point and must be unmistakable at a glance.

RIGHT REGION: one long slim horizontal rounded bar lying on its side, divided by fine tick marks into three equal segments. The leftmost portion of the bar - a little under half of the total - is filled solid teal; the remainder is filled burnt amber and continues to the right edge of the bar. A thin vertical navy line marks the boundary between the two fills. A tiny teal drone cluster icon sits just above the teal portion; a tiny amber helicopter icon sits just above the amber portion.

Render style: flat editorial vector infographic. The columns must read as stacked money, not as chart bars - keep the banknote banding visible. No axes, no gridlines, no legend box.

Text labels (render exactly, all horizontal):
- centred above the whole left region, navy, bold: "RUPEES PER KM2 SURVEYED"
- above the tall first column, burnt amber, large: "13,800"
- directly beneath that, burnt amber, small: "CHARTER HELICOPTER"
- above the short second column, teal, large: "502"
- directly beneath that, teal, small: "KESTREL SWARM"
- floating in the gutter beside the tall column, burnt amber, very large: "27x"
- above the meter bar, navy, bold: "SAME MONEY, DIFFERENT PURCHASE"
- under the teal portion, teal, two lines: "2.69 LAKH - 86 MIN" / "THE ENTIRE SYSTEM, ONCE"
- under the amber portion, burnt amber, two lines: "1.89 LAKH PER HOUR" / "AND IT KEEPS RUNNING"
- tick labels along the bar, small slate: "1 H" / "2 H" / "3 H"
- bottom-left, small slate: "CHARTER 1.6 L/HR + 18% GST, IAMSAR SWEEP RATE"
- bottom-right, small slate: "KESTREL CAPEX OVER 300 FLIGHT HOURS"

Constraint: 16:9, pure white ground. Only the labels listed. The amber column must be dramatically taller than the teal one. No coins, no confetti, no falling money.
```

---

## 6 · P4.2 — When it fails  `REGENERATE IN LIGHT`

**Slide 4** · keep 16:9 · replaces the dark `P4.2-degradation.png`
**Reject if:** the descending arrow is broken at any point · the fourth rung's lanes are not visibly
wider than the first's

```
Style: precise editorial-technical infographic for a printed report. PURE WHITE background, hex #FFFFFF, absolutely flat - no gradient, no vignette, no paper texture, no drop shadow falling on the background, no rounded card behind the artwork, pure white right to all four edges. Linework and primary text in deep navy #0B1220. Our system and healthy links in teal #0E7490. Degraded and warning states in burnt amber #B45309. Failure in #B91C1C. Secondary text in slate #475569; light tints in #E2E8F0. Clean geometric sans-serif; ALL text perfectly horizontal. Generous white space. No watermarks, no borders, no frames, no outer glow. 16:9.

Composition: four small isometric scenes arranged as descending steps from the upper left down to the lower right, like four rungs of a staircase, each on its own thin flat platform, with wide white space between them. One thick arrow runs down the whole staircase from top to bottom, starting solid teal and fading gradually through pale teal to burnt amber at the bottom - the arrow must be continuous and unbroken from the first rung to the last.

RUNG 1, top: one hexacopter and six quadcopters over a small debris field, all joined by a dense bright teal mesh web, plus one link running off to a cell tower at the edge.
RUNG 2: the same formation, but the mesh is sparse and thin, and the cell tower is drawn with a red cross through it.
RUNG 3: no mesh at all. The quadcopters fly their lanes alone, each with a small glowing data-core cylinder visible inside it, and one dotted path arcs from a quadcopter back to a small truck icon.
RUNG 4, bottom: two of the six quadcopters lie dark and inert on the debris marked with small red crosses. The remaining four continue flying, and their search lanes are drawn visibly wider apart than the lanes in rung 1, so the same ground is still covered by fewer aircraft.

Along the bottom edge of the frame, one closing line.

Render style: clean flat isometric line illustration with light tint fills, precise and uncrowded. No photorealism, no texture, no explosions, no fire.

Text labels (render exactly, all horizontal, one beside each rung):
- rung 1, teal: "FULL MESH + 5G - MBPS"
- rung 2, teal: "TOWER DOWN - LoRa KBPS"
- rung 3, slate: "NO LINK - DATA CORE FLIES HOME"
- rung 4, burnt amber: "SCOUTS LOST - LANES WIDEN"
- centred along the bottom edge, navy, bold: "IT GETS SLOWER. IT DOES NOT STOP."

Constraint: 16:9, pure white ground. Only the labels listed. The descending arrow must be unbroken across all four rungs. No weapons, no fire, no smoke.
```

---

## 7 · P4.3 — Whose asset, whose money  `NEW`

**Slide 4** · crop to a wide band (~4:1) · takes the slot vacated by the retired flight-path roadmap
**Reject if:** the teal sliver is thick enough to read comfortably — it must look almost too small to
see · the bottom tier is not the widest · "0.12%" or "16,015" is wrong

```
Style: precise editorial-technical infographic for a printed report. PURE WHITE background, hex #FFFFFF, absolutely flat - no gradient, no vignette, no paper texture, no drop shadow falling on the background, no rounded card behind the artwork, pure white right to all four edges. Linework and primary text in deep navy #0B1220. Our system and good values in teal #0E7490. Status quo and slow paths in burnt amber #B45309. Secondary text and large neutral quantities in slate #475569; light tints in #E2E8F0. Clean geometric sans-serif; ALL text perfectly horizontal. Generous white space. No watermarks, no borders, no frames, no outer glow, no 3D bevel. 16:9.

Composition: a LEFT HALF and a RIGHT HALF separated by a wide white gutter.

LEFT HALF: three horizontal plaques stacked vertically and joined by thin vertical navy connectors, each plaque wider than the one above it.
- TOP plaque, narrowest: a small government-building icon beside a tight cluster of small shield icons.
- MIDDLE plaque, wider: a state-outline icon beside a small group of human-figure icons.
- BOTTOM plaque, by far the widest, spanning the full width of this half: filled edge to edge with a dense uniform grid of many tiny identical building icons. Resting on top of this bottom plaque and drawn distinctly larger and in solid teal, one hexacopter with six small quadcopters beside it, so the aircraft clearly belong to this tier and no other.
A long dashed burnt-amber arrow curves from the top plaque all the way down to the bottom plaque, with a small clock icon on it. A separate short solid teal arrow loops tightly within the bottom plaque, with a small lightning icon on it.

RIGHT HALF: one very long horizontal bar spanning almost the full width of this half, filled flat slate. Directly beneath its far-left end, a second bar of exactly the same height but almost invisibly short - a teal sliver only a hair wide, so small it needs a thin teal leader line pulling out to its label. Below both bars, a single row of three small flat outlined chips.

Render style: flat editorial infographic in the manner of an institutional report figure. The two bars are a direct physical size comparison, not a chart. No axes, no gridlines, no legend box.

Text labels (render exactly, all horizontal):
- above the left half, navy, bold: "WHOSE ASSET"
- on the top plaque, slate: "NDMA + NDRF - 16 BATTALIONS"
- on the middle plaque, slate: "SDMA + SDRF - STATE"
- on the bottom plaque, teal: "DDMA - ALL 738 DISTRICTS"
- on the dashed amber arrow, burnt amber: "NDRF MUST TRAVEL"
- on the short teal loop arrow, teal: "DDMA IS ALREADY THERE"
- above the right half, navy, bold: "WHOSE MONEY"
- above the long slate bar, slate: "16,015 CRORE - PREPAREDNESS LINE 2021-26"
- on the leader line from the teal sliver, teal, two lines: "19.86 CRORE" / "ALL 738 DISTRICTS"
- beside the sliver, teal, very large: "0.12%"
- the three chips in a row, small navy: "NO NEW BUDGET HEAD" / "90:10 FOR NE + HIMALAYAN STATES" / "CSR-ELIGIBLE, SCHEDULE VII"

Constraint: 16:9, pure white ground. Only the labels listed. The teal sliver must be almost imperceptibly thin next to the slate bar - if it is comfortably readable the figure has failed. Do not draw a map of any country. Exact icon counts are illustrative; the printed numerals must be exact.
```

---

## 8 · P5.1 — The survival wall  `NEW — the clock was rejected`

**Slide 5** · crop to a wide band (~4:1) · replaces `P5.1-survival-clock-REDO.png`
**Reject if:** the four blocks are not the same size · the fill levels do not visibly descend left to
right · the teal banner is not over block 1 and the amber over block 4 · "+64" is missing

> The radial clock implied cyclic time, forced curved text, read as a speedometer and had no title.
> This is horizontal, every string is straight, and it carries its own question as a headline.
> **The `+64` is the single most important number in the project.**

```
Style: precise editorial-technical infographic for a printed report. PURE WHITE background, hex #FFFFFF, absolutely flat - no gradient, no vignette, no paper texture, no drop shadow falling on the background, no rounded card behind the artwork, pure white right to all four edges. Linework and primary text in deep navy #0B1220. Our system and good values in teal #0E7490. Baseline and warning values in burnt amber #B45309. Danger in #B91C1C. Survival and success in #15803D. Secondary text in slate #475569; light tints in #E2E8F0. Clean geometric sans-serif; ALL text perfectly horizontal - never curved, never rotated, never along an arc. Generous white space, strong left-to-right reading order. No watermarks, no borders, no frames, no outer glow, no 3D bevel. 16:9.

Composition: four large squares in one horizontal row, evenly spaced with wide white gaps, all four exactly the same size, all sitting on one shared thin slate baseline.

Each square is a neat 10-by-10 grid of one hundred small identical human-figure pictograms, the same size in every square. Within each square the figures are filled from the bottom rows upward like a liquid filling a vessel: every figure below the fill line is solid and saturated, every figure above it is a pale, barely-visible grey outline. The height of the fill line differs sharply between the squares and must clearly descend from left to right:
- SQUARE 1: filled almost completely to the top, in solid green. Only the very topmost sliver is pale.
- SQUARE 2: filled to roughly six sevenths of its height, in solid green.
- SQUARE 3: filled to roughly half its height, in solid burnt amber.
- SQUARE 4: filled to roughly one third of its height, in solid red. The upper two thirds are pale outlines.

Above the row, two small ribbon banners hang down on short stems: a TEAL banner positioned directly over SQUARE 1 containing a small hexacopter icon, and a BURNT AMBER banner positioned directly over SQUARE 4 containing a small human-figure icon.

Spanning the horizontal distance between those two banners, sitting just below them and above the squares, one long green double-headed measuring arrow with a small green outlined callout box at its midpoint.

One title line runs along the top of the frame. One thin footnote line runs along the bottom.

Render style: flat editorial pictogram figure, the discipline of a newspaper isotype graphic. Precise alignment, no perspective, no 3D, no glow, no gradient on the figures. Not a bar chart. No axes, no legend box.

Text labels (render exactly, all horizontal):
- title along the top, navy, bold: "OUT OF 100 TRAPPED PEOPLE, HOW MANY ARE STILL ALIVE"
- under SQUARE 1, two lines, green then slate: "99 ALIVE" / "AT 6 HOURS"
- under SQUARE 2, two lines, green then slate: "85 ALIVE" / "AT 24 HOURS"
- under SQUARE 3, two lines, burnt amber then slate: "53 ALIVE" / "AT 48 HOURS"
- under SQUARE 4, two lines, red then slate: "35 ALIVE" / "AT 72 HOURS"
- inside the TEAL banner, teal, two lines: "KESTREL FINISHES" / "5.8 HOURS"
- inside the AMBER banner, burnt amber, two lines: "1,300 PERSONNEL FINISH" / "DAY 3"
- inside the green callout box on the measuring arrow, green, two lines: "+64 SURVIVORS" / "PER 100 TRAPPED"
- footnote along the bottom, small slate: "Survival by extrication time, USAR literature"

Constraint: 16:9, pure white ground. Only the labels listed. All four squares identical in size, with fill levels clearly stepping down from left to right. Exact figure counts are illustrative; the printed numerals must be exact.
```

---

## 9 · P5.2 — The uncounted  `NEW`

**Slide 5** · crop to a wide band (~4:1) · replaces the retired `P5.2-monsoon-map.png`
**Reject if:** the ghost run in the top band is not far longer than the solid run · the two bands use
different icon sizes · "1,114" or "4,500" is wrong

```
Style: precise editorial-technical infographic for a printed report. PURE WHITE background, hex #FFFFFF, absolutely flat - no gradient, no vignette, no paper texture, no drop shadow falling on the background, no rounded card behind the artwork, pure white right to all four edges. Linework and primary text in deep navy #0B1220. Confirmed and counted values in burnt amber #B45309. Our system in teal #0E7490. Secondary text and uncounted values in slate #475569; light tints in #E2E8F0. Clean geometric sans-serif; ALL text perfectly horizontal. Generous white space, strong left-to-right reading order. No watermarks, no borders, no frames, no outer glow. 16:9.

Composition: two horizontal bands stacked one above the other with generous white space between them, both starting from the same left margin and both using exactly the same icon size.

In each band, a long horizontal run of small identical human-figure pictograms packed tightly in a single row, reading left to right. Each band's run has two clearly distinct treatments with an abrupt switch between them:
- SOLID figures, filled burnt amber, at the start of the run
- GHOST figures, drawn only as thin pale grey outlines with hollow centres, continuing after the solid ones

UPPER BAND: a short run of solid amber figures, followed by a run of pale ghost outlines that is roughly four times longer and dominates the width of the entire frame. If the row runs out of width it wraps once into a tight second row directly beneath.
LOWER BAND: a very short run of solid amber figures followed by an even shorter run of ghost outlines. This band is small and quiet, an echo of the one above.

At the far left of each band, outside the run, a small vertical tick and a two-line label naming the event.

One title line runs along the top of the frame. Bottom left, a small scale key showing one solid figure beside one ghost figure. Bottom right, a two-line closing statement in teal.

Render style: flat editorial pictogram figure, newspaper isotype discipline. Precise alignment, no perspective, no 3D, no glow. Not a bar chart. No axes, no legend box.

Text labels (render exactly, all horizontal):
- title along the top, navy, bold: "A DEATH TOLL COUNTS THE BODIES THAT WERE FOUND"
- left of the UPPER band, two lines, navy then slate: "NEPAL-TIBET" / "AUG 2026"
- above the solid run in the UPPER band, burnt amber: "1,114 CONFIRMED DEAD"
- above the ghost run in the UPPER band, slate: "4,500 STILL MISSING"
- left of the LOWER band, two lines, navy then slate: "WAYANAD" / "JUL 2024"
- above the solid run in the LOWER band, burnt amber: "357 CONFIRMED DEAD"
- above the ghost run in the LOWER band, slate: "206 STILL MISSING"
- at the scale key, bottom left, small slate: "ONE FIGURE = 100 PEOPLE"
- bottom right, teal, two lines: "21,000 PERSONNEL. 16 HELICOPTERS." / "THE LIMIT IS SEARCH CAPACITY, NOT WILL."

Constraint: 16:9, pure white ground. Only the labels listed. Both bands must use the identical icon size. The ghost run in the upper band must visibly dwarf everything else in the figure. Flat pictograms only - no bodies, no faces, no gore. Exact figure counts are illustrative; the printed numerals must be exact.
```

---

## After every render

```bash
cd kestrel-ppt
python3 scripts/whiten.py images/P5.1-survival-wall.png      # snap to pure white + trim
python3 scripts/whiten.py images/*.png                       # or the whole batch
```

Then check the four things that actually matter, in this order:

1. **Every printed numeral against `DATA.md`.** One wrong digit = reject.
2. **The reject line** printed above each prompt.
3. **No text is curved, rotated or vertical.**
4. **The background is white to all four edges** — no vignette, no grey band.

Generate 2–3 variants per prompt and keep the best. Resolution note: renders come back ~1672 px wide,
which is 163 DPI at 10.2 in on the slide. Fine on screen and in a PDF; if your tool offers a larger
output, take it.
