# PROMPTS — THE SINGLE DRONE · three shots that answer SIH26177 noun-for-noun

**Why this file exists.** `DATA.md` §19: the PS title is *"A deployable AI-powered autonomous
**drone**"* — singular — and **not one of its eight Expected-Solution bullets needs a second
aircraft.** Addendum 4 then moved the fusion stack and the language model into the truck. A judge
reading the deck cold can fairly conclude we answered a question they did not ask.

These three fix it by making **one scout a complete, self-sufficient, PS-compliant autonomous drone
with the truck switched off.** The base station becomes an *accelerator*, never a dependency.

> **One Kestrel scout is a complete answer to the problem statement. Six is the answer to Wayanad.**

## Where they go — and the slide swap they force

`DATA.md` §1a measured the real budget: **two 16:9 panels + one 4:1 band per slide.** So slides 2
and 3 swap jobs, which is also the more logical split:

| Slide | Was | **Becomes** |
|---|---|---|
| **2 Proposed Solution** | the swarm, half the system | **THE SYSTEM** — `C4` six at first light · `C1` the truck is the brain · `F1-sachet` |
| **3 Technical Approach** | `C1` truck · `F2` buried person · `C5` hazards | **ONE DRONE** — **`S1` three brains** · **`S2` the loop that decides** · `F2-buried-person` (band) |

`C5` four hazards and the pixel ladder move to the bench. **`S3` is the spare** — run it if S1 or S2
disappoints, or use it on slide 5 where the emotional register belongs.

Every number below traces to `DATA.md` §20–§24. These are `[DATA-EXACT]` prompts — **verify each
figure against the addendum before accepting a render.**

---

## S1 · One aircraft, three brains  `WHITE` `[DATA-EXACT]`

The anatomy shot. It has to prove the aircraft is complete on its own.

**Reject if:** the truck appears anywhere · the STM32 and the UNO Q are not visibly separate parts ·
the three tier bands are not clearly nested · any number disagrees with §21a

```
Style: precise editorial-technical product illustration for a printed report. PURE WHITE background, hex #FFFFFF, absolutely flat - no gradient, no vignette, no paper texture, no drop shadow falling on the background, no rounded card behind the artwork, pure white right to all four edges. Linework and primary text in deep navy #0B1220. Callout lines and our-system highlights in teal #0E7490. Rate chips in burnt amber #B45309. Secondary text in slate #475569; light tints in #E2E8F0. Clean geometric sans-serif; ALL text perfectly horizontal. Generous white space. No watermarks, no borders, no outer glow. 16:9.

Composition: ONE quadcopter, and nothing else in the frame. It sits left of centre as a three-quarter exploded technical view at large scale, four short arms with prop guards, matte grey-black, its top shell lifted and floating slightly above the airframe to reveal the stack inside.

Revealed inside, drawn as distinct recognisable parts with thin teal leader lines running out into the white space on the right:
- a single-board computer with a square SoC under a small heatsink and a visible antenna trace, mounted centrally
- a separate small microcontroller board beside it, clearly a different and smaller part
- a downward-facing RGB camera lens through the frame floor
- a small square thermal sensor module next to it
- a tiny stacked rack of five puck-shaped pods on a release rail underneath
- one battery pack at the rear

On the RIGHT THIRD of the frame, occupying the white space, three horizontal bands stacked vertically, each a wide rounded rectangle in a progressively lighter tint of #E2E8F0, nested so the lowest band is widest and the top band narrowest - a stepped pyramid lying on its side. A thin teal bracket links each band back to the part it runs on. Each band carries a rate chip in burnt amber at its right edge.

Render style: flat-shaded technical product illustration with precise navy outlines, service-manual discipline. No photorealism, no reflections, no environment, no logos, no sky.

Text labels (render exactly, all horizontal, on leader lines):
On the aircraft parts: "ARDUINO UNO Q - DRAGONWING QRB2210" / "STM32U585 - REAL-TIME MCU" / "RGB 12 MP DOWN" / "FLIR LEPTON 3.5" / "BREADCRUMB PODS x5"
The three bands, bottom to top, each two lines: "REFLEX - PX4 ON THE MCU" + "ATTITUDE, FAILSAFE, GEOFENCE" / "PERCEPTION - YOLOv8n INT8, VIO" + "PERSON + 8 HAZARD CLASSES" / "DECIDE - BEHAVIOUR TREE" + "WHERE TO LOOK NEXT"
Rate chips at the right edge of each band, bottom to top: "1 kHz", "20 Hz", "1 Hz"
One line along the bottom, navy, bold: "COMPLETE WITH THE TRUCK SWITCHED OFF"

Constraint: 16:9, pure white ground. Exactly these labels. ONE aircraft only - no truck, no second drone, no operator. The two compute boards must read as two clearly separate parts. No weapons, no military markings.
```

*The two-boards detail is the whole page. Qualcomm's own pitch for this board is the **dual brain**,
and it is also our safety argument: if Linux panics in flight, the STM32 still lands the aircraft.
No Jetson entry can say that. If the render merges them into one board, regenerate.*

---

## S2 · The loop that decides  `WHITE` `[DATA-EXACT]`

The autonomy shot. It has to prove the aircraft decides, and show *the physical mechanism* by which
it buys certainty — descent.

**Reject if:** it reads as a generic flowchart · the two altitudes are not visibly different ·
the person is not the same size in both altitude panels

```
Style: precise editorial-technical product illustration for a printed report. PURE WHITE background, hex #FFFFFF, absolutely flat - no gradient, no vignette, no paper texture, no drop shadow, pure white right to all four edges. Linework and primary text in deep navy #0B1220. Decision paths and highlights in teal #0E7490. Reject paths in burnt amber #B45309. Secondary text in slate #475569; light tints in #E2E8F0. Clean geometric sans-serif; ALL text perfectly horizontal. Generous white space. No watermarks, no borders. 16:9.

Composition: two regions separated by generous white space, no dividing line.

LEFT REGION, about 45% width - a closed circular decision loop drawn as four rounded nodes arranged in a ring, joined by thick teal arrows all flowing clockwise, with a small quadcopter icon at the centre of the ring. From the third node, one burnt amber arrow breaks out of the ring downward to a small separate node standing alone below.

RIGHT REGION, about 45% width - two square panels stacked vertically, each showing the identical top-down view of the same debris field with the same prone human figure lying on it, the figure drawn at exactly the same physical size in both. A square pixel grid overlays the figure in each panel, and the grid is visibly much coarser in the upper panel than the lower. In the lower panel the figure's outline and posture are clearly legible from the pixels; in the upper panel it is barely resolved. A thin vertical teal arrow runs down the left edge from the upper panel to the lower one, with an altitude scale beside it.

Render style: precise flat technical infographic, the discipline of a well-made engineering figure. Thin linework. Not a chart - no axes, no bars, no legend box.

Text labels (render exactly, all horizontal):
LEFT REGION, the four ring nodes clockwise from top: "LOCALISE - VIO + GPS" / "PERCEIVE - RGB, THERMAL, WiFi + BLE" / "UPDATE BELIEF - EVIDENCE GRID" / "CHOOSE - MOST INFORMATION PER JOULE"
- the amber break-out node below the ring: "BATTERY RESERVE - RETURN"
- centred above the ring, navy, bold: "1 Hz. DETERMINISTIC. NO LANGUAGE MODEL IN THIS LOOP."
RIGHT REGION:
- above the upper panel, slate, two lines: "SWEEP AT 30 M" / "0.076 M PER PIXEL - 22 PIXELS"
- above the lower panel, teal, two lines: "CONFIRM AT 15 M" / "0.038 M PER PIXEL - 45 PIXELS"
- beside the vertical arrow, navy: "IT BUYS CERTAINTY WITH ALTITUDE"
- one footnote along the very bottom, small slate: "A token takes 100 ms. A wall arrives in 20."

Constraint: 16:9, pure white ground. Exactly these labels. The human figure must be the identical size in both right-hand panels - only the grid changes. No watermark, no border.
```

*Same trick as the pixel ladder and it works for the same reason: **the person never changes size,
only the sampling does.** That is what makes the descent read as a mechanism rather than a claim.
The footnote is the line that separates us from every deck that puts an LLM on an aircraft.*

---

## S3 · Alone in the dark  `DARK` `[the spare - and the deployability argument]`

One scout, no truck, no network, still working. **Do not run `whiten.py` on this one.**

**Reject if:** any second aircraft or vehicle is visible · it reads as military · the storage tag is missing

```
Style: premium defence-tech mission-control aesthetic. Deep navy-charcoal ground (#0B1220), cyan-teal primary accent (#22D3EE), warm amber-orange secondary accent (#F59E0B), restrained holographic HUD elements, cinematic lighting, photorealistic. No watermarks, no borders, no stock-photo gloss, no lens flare. All specified text in a clean geometric sans-serif, uppercase, small, in #E2E8F0 or #94A3B8. 16:9 widescreen.

Composition: night, deep in a landslide-scarred Indian hill valley, far from any road or light. A single small matte-grey quadcopter hovers low over a debris field in the near foreground, close enough to show its downward camera and the small rack of pods beneath it. Its own light throws a hard cone onto the wreckage below.

The frame is otherwise empty of human presence - no vehicle, no operator, no other aircraft, no settlement lights. Behind and above, the ridgeline is a black silhouette against a faintly starred sky, and mist sits in the valley. The emptiness is the point.

A faint cyan flight-path ribbon trails behind the drone and disappears into the dark, and one small cyan storage glyph glows on the aircraft's flank.

Lighting: near-black night, one hard white beam downward from the drone, cold blue ambient on the mist and rubble, a faint cyan rim on the airframe. Solitary, sombre, self-reliant.

Text labels (render exactly, small HUD tags on thin leader lines):
- upper left, in #94A3B8: "NO TRUCK. NO MESH. NO NETWORK."
- at the storage glyph, cyan: "32 GB ON BOARD - THE AIRCRAFT IS THE LINK"
- lower left, cyan: "STILL DETECTING. STILL MAPPING."
- lower right, amber: "WORST CASE IS NOT NO DATA. IT IS DATA 18 MINUTES LATE."

Constraint: 16:9. Exactly these four labels. ONE aircraft, nothing else man-made in frame. No people, no bodies, no weapons, no military insignia.
```

---

## What these three do to the argument

| PS bullet | Answered by |
|---|---|
| Autonomous Navigation, GPS + GPS-denied | **S1** tier 2 · **S2** the ring · §24 drift arithmetic |
| On-Device AI Inference | **S1** the UNO Q band · §20 measured 17 FPS |
| Multi-Sensor Fusion | **S1** RGB + thermal + radio · `F2-buried-person` |
| Hazard Classification | **S1** "PERSON + 8 HAZARD CLASSES" |
| Geo-Tagged Mapping | **S2** evidence grid node |
| Emergency Alerting | **S2** publish threshold · §22d the on-board SLM |
| **Offline Resilience** | **S3** — and this is the bullet nobody else will answer this hard |
| Command Center Dashboard | `P5.3-dashboard`, slide 5, unchanged |

**Eight bullets, one aircraft, no truck required.** Then slide 2 says: *and here are six of them,
plus a truck, and that is how 15 km² gets swept in 5.8 hours instead of five days.*
