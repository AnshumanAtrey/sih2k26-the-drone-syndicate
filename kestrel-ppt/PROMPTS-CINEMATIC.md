# PROMPTS — CINEMATIC · six shots, six different jobs

**What went wrong:** you pointed at the cinematic register, I diagnosed it correctly — photographic
base, hard graphic overlay, data drawn *on* the scene — and then filled the final deck with flat
diagrams anyway. These six fix that.

Every one is **dark, photographic, tier 1**. On the white template they sit as framed panels
(1 px `#CBD5E1`, 6 px radius). **Do not run `whiten.py` on any of these.**

## The formula that makes the good ones work

Look at `P2.1-frog`, `P2.2-hero` and `R2-2-handover-dark` — they share it exactly:

1. **A real Indian disaster scene**, photoreal — Western Ghats hill terrain, NDRF orange, monsoon light
2. **Dusk or night**, cold blue ambient, warm amber from headlamps and strobes, cyan from screens
3. **Three to five HUD tags carrying real numbers**, on thin leader lines
4. **Human, not military** — no weapons, no insignia, faces indistinct or turned away

That's the whole recipe. Every prompt below is built on it.

## What each shot carries, and where it goes

| # | Shot | Information it carries | Candidate slide |
|---|---|---|---|
| **C1** | The truck is the brain | the architecture decision itself — **replaces the F3 diagram** | 3 |
| **C2** | Breadcrumbs into the dark | comms that reach inside buildings | 4 |
| **C3** | Thirty metres | detection — thermal + RGB at the altitude that works | 2 or 3 |
| **C4** | Six at first light | deployment speed, the whole system in one frame | 2 |
| **C5** | Four hazards, one frame | hazard classification, PS bullet 4 | 3 |
| **C6** | The void | what we are actually reaching for | 5 |

**Run in one chat, in order, attaching `images/P2.2-hero.png` to the first** and appending to every
prompt: *"match the lighting, palette, material finish and realism of the attached image."* Bleed is
wanted here — these should look like one shoot.

---

## C1 · The truck is the brain

**Reject if:** a large drone appears to carry the compute · the rack isn't clearly inside the vehicle

```
Style: premium defence-tech mission-control aesthetic. Deep navy-charcoal ground (#0B1220), cyan-teal primary accent (#22D3EE), warm amber-orange secondary accent (#F59E0B), restrained holographic HUD elements, cinematic lighting, photorealistic. No watermarks, no borders, no stock-photo gloss, no lens flare. All specified text in a clean geometric sans-serif, uppercase, small, in #E2E8F0 or #94A3B8. 16:9 widescreen.

Composition: night, at a staging point on a broken hill road above a landslide-hit Indian valley. The frame is dominated by an orange-and-white NDRF box-bodied response truck, rear doors swung wide, seen three-quarter from behind and slightly low so it feels substantial.

Inside the open rear, a lit equipment rack: a single-board computer with a finned heatsink and ribbon cables, cooling fans, a power unit cabled to the vehicle, and two monitors showing a dark tactical map with green markers. The interior glows cool cyan against the night. A telescopic mast rises from the truck roof with a small antenna at its top, faint cyan arcs radiating outward from it.

Two operators in orange stand at the open doors, one seated at the rack, one facing out toward the valley. Beyond them, far below, the debris field recedes into mist, and three small quadcopters are visible as distant navigation lights strung across it.

Lighting: deep blue night, warm amber spill from the truck interior and the operators' headlamps, cool cyan from the monitors, cold moonlight on the rubble beyond.

Text labels (render exactly, small HUD tags on thin leader lines):
- on the rack, cyan: "BASE STATION - 12 TOPS"
- beside the mast, cyan: "MAINS POWER, NO WEIGHT LIMIT"
- lower left, in #94A3B8: "THE BRAIN NEVER LEAVES THE GROUND"
- lower right, amber: "SCOUTS 6/6 - 2.6 KM2/H"

Constraint: 16:9. Exactly these four labels. No large aircraft anywhere. No weapons, no military insignia. Faces indistinct or turned away.
```

---

## C2 · Breadcrumbs into the dark

**Reject if:** the dropped pucks aren't visible as a trail · it reads as a single drone with no chain

```
Style: premium defence-tech mission-control aesthetic. Deep navy-charcoal ground (#0B1220), cyan-teal primary accent (#22D3EE), warm amber-orange secondary accent (#F59E0B), restrained holographic HUD elements, cinematic lighting, photorealistic. No watermarks, no borders, no stock-photo gloss, no lens flare. All specified text in a clean geometric sans-serif, uppercase, small. 16:9 widescreen.

Composition: the interior of a partially collapsed concrete building at night, seen down the length of a dust-hung corridor that recedes into darkness. Broken slabs lean against one another, rebar hangs, a floor has given way on the right.

A small quadcopter hovers mid-corridor, deeper in, its own light throwing a hard cone forward. Directly beneath it, one small puck-shaped device is falling the last half-metre toward the rubble, caught mid-drop.

Behind the drone, receding back toward the camera, three identical pucks already lie on the debris at intervals, each with a small cyan indicator light. Faint cyan arcs link puck to puck to puck in an unbroken chain that runs past the camera and out of frame toward the entrance, where a sliver of blue night sky is visible.

Lighting: near-black interior, one hard white beam from the drone, small cyan points from the pucks, cold blue spill from the distant opening. Heavy airborne dust catching the light.

Text labels (render exactly, small HUD tags on thin leader lines):
- at the falling puck, cyan: "BREADCRUMB DROP"
- along the chain of pucks, cyan: "MESH HOLDS - 3 HOPS TO THE TRUCK"
- upper right, amber: "RELAY AT ALTITUDE: NO SIGNAL HERE"
- lower right, in #94A3B8: "CERBERUS METHOD, DARPA SUBT"

Constraint: 16:9. Exactly these four labels. At least three already-dropped pucks visible in a receding line. No people, no bodies.
```

---

## C3 · Thirty metres

**Reject if:** the thermal inset isn't clearly a thermal image · the altitude tag is missing

```
Style: premium defence-tech mission-control aesthetic. Deep navy-charcoal ground (#0B1220), cyan-teal primary accent (#22D3EE), warm amber-orange secondary accent (#F59E0B), restrained holographic HUD elements, cinematic lighting, photorealistic. No watermarks, no borders, no stock-photo gloss, no lens flare. All specified text in a clean geometric sans-serif, uppercase, small. 16:9 widescreen.

Composition: a near-overhead drone-camera view, looking steeply down at a debris field at night from low altitude - close enough that individual broken slabs, twisted roofing sheet and splintered timber are sharply resolved, and a collapsed rooftop fills much of the frame. The drone's own light pools on the wreckage directly below.

Lying in a gap between two slabs, partly sheltered, one person on their side, still, seen from above at an angle that keeps the face hidden. A crisp cyan detection box is drawn around them with small corner brackets.

Inset in the upper right corner, a clean rectangular picture-in-picture panel with a thin cyan border, showing the identical view rendered as a thermal image: mostly cold blue-grey rubble, with the human figure glowing as a clearly shaped warm white-orange form - recognisably a body, not a blob.

A faint cyan altitude scale runs down the left edge of the frame.

Lighting: night, hard downward light from the drone, deep shadow in the gaps, cold blue ambient beyond the pool of light.

Text labels (render exactly, small HUD tags):
- top left, cyan: "ALT 30 M"
- beside the detection box, cyan: "SURVIVOR - CONF 0.94"
- on the thermal inset, in #94A3B8: "FLIR LEPTON - 0.20 M/PIXEL"
- bottom right, amber: "8 PIXELS TALL. AT 50 M, ONE."

Constraint: 16:9. Exactly these four labels. Face hidden or turned away, no blood, no injury detail, person intact and alive. The thermal inset must read as a genuine thermal image.
```

---

## C4 · Six at first light

**Reject if:** any aircraft looks like it carries the compute · fewer than six scouts in the air

```
Style: premium defence-tech mission-control aesthetic. Deep navy-charcoal ground (#0B1220), cyan-teal primary accent (#22D3EE), warm amber-orange secondary accent (#F59E0B), restrained holographic HUD elements, cinematic lighting, photorealistic. No watermarks, no borders, no stock-photo gloss, no lens flare. All specified text in a clean geometric sans-serif, uppercase, small. 16:9 widescreen.

Composition: dawn, a wide low-angle shot along a broken road at the edge of a flood-and-landslide-hit Indian hill town. The first light is just catching the ridgeline; mist sits in the valley below.

In the near left foreground, the NDRF truck with its rear doors open and a mast raised, an operator at a tripod-mounted tablet. Rising from a folding rail beside it, six small matte-grey quadcopters in a staggered climbing line, the nearest close enough to show its downward camera and small thermal sensor, the furthest already out over the debris. Each trails a faint cyan flight-path ribbon, and together the ribbons fan out into the beginnings of a visible search grid over the town below.

One additional small quadcopter hovers higher and apart from the six, plain and sensorless, with a stub antenna.

Lighting: cold blue pre-dawn with a warm orange rim along the ridge, amber spill from the truck, cyan rim-light on the airframes. Epic but restrained, hopeful.

Text labels (render exactly, small HUD tags on thin leader lines):
- on the high plain quadcopter: "RELAY - NO INTELLIGENCE ABOARD"
- on the nearest scout: "SCOUT x6 - ARDUINO UNO Q"
- on the truck: "BASE STATION"
- bottom right, amber: "T+00:04 - SIX SCOUTS LAUNCHED"

Constraint: 16:9. Exactly these four labels. Six scouts plus one plain relay, nothing larger. No weapons, no military markings.
```

---

## C5 · Four hazards, one frame

**Reject if:** fewer than four distinct hazards are visible and tagged

```
Style: premium defence-tech mission-control aesthetic. Deep navy-charcoal ground (#0B1220), cyan-teal primary accent (#22D3EE), warm amber-orange secondary accent (#F59E0B), hazard red (#EF4444), restrained holographic HUD elements, cinematic lighting, photorealistic. No watermarks, no borders, no stock-photo gloss, no lens flare. All specified text in a clean geometric sans-serif, uppercase, small. 16:9 widescreen.

Composition: an elevated wide drone-camera view at dusk over a devastated Indian semi-urban riverside settlement, framed so that four distinct dangers occupy four different quadrants of the image and are all clearly legible:
- LOWER LEFT: brown floodwater standing deep between buildings, only rooftops above the surface
- UPPER LEFT: a building half-collapsed, its remaining wall visibly leaning, a long crack running down it
- UPPER RIGHT: a snapped utility pole with cables hanging low into the water, one cable end glowing faintly where it arcs
- LOWER RIGHT: a fresh landslide scar of raw red earth cutting down the hillside into the settlement

Each of the four is enclosed by a translucent polygon outline in the HUD, drawn crisply over the scene: the flood and landslide polygons in amber, the leaning building and the live cable in red. Thin leader lines run from each polygon to its label.

Lighting: overcast dusk, flat grey-blue light, one warm break in the cloud on the ridge. Documentary realism, sombre.

Text labels (render exactly, one per polygon, plus one corner tag):
- on the flood polygon, amber: "FLOODWATER"
- on the leaning building polygon, red: "UNSTABLE STRUCTURE"
- on the cable polygon, red: "EXPOSED LINES - LIVE"
- on the landslide polygon, amber: "LANDSLIDE ZONE"
- bottom left corner, cyan: "4 OF 8 CLASSES - ON DEVICE"

Constraint: 16:9. Exactly these five labels. All four hazards clearly visible and separated in the frame. No people, no bodies.
```

---

## C6 · The void

The emotional close. This is what all the arithmetic is for.

**Reject if:** the person is not clearly alive · it becomes gruesome · the sensing beam isn't visible

```
Style: premium defence-tech mission-control aesthetic. Deep navy-charcoal ground (#0B1220), cyan-teal primary accent (#22D3EE), warm amber-orange secondary accent (#F59E0B), restrained holographic HUD elements, cinematic lighting, photorealistic. No watermarks, no borders, no stock-photo gloss, no lens flare. All specified text in a clean geometric sans-serif, uppercase, small. 16:9 widescreen.

Composition: a tight, low, intimate view inside a survivable void beneath collapsed concrete - a wedge of space formed where a fallen slab has come to rest against a standing beam. Dust hangs in the air. The space is almost entirely dark.

A single narrow shaft of dawn light enters through a gap high in the rubble at the top right, falling across the space. In it, one adult hand and forearm are raised toward the gap, fingers open, unmistakably alive and reaching - the only part of the person clearly visible, the rest lost in shadow. Beside the hand, a phone lies on the rubble face-down, its small Bluetooth indicator glowing a faint cyan.

Descending through the same gap, a soft translucent teal sensing beam reaches down into the void and washes over the hand and the phone.

Lighting: near-black, one warm golden shaft from above, faint cyan from the phone and the beam, heavy dust motes suspended in the light.

Text labels (render exactly, small HUD tags, kept to the edges of the frame):
- upper right near the gap, cyan: "RF THROUGH 3 M OF CONCRETE"
- beside the phone, cyan: "BLE BEACON - DETECTED"
- lower left, in #94A3B8: "5.8 HOURS, NOT DAY THREE"
- lower right, amber: "99 ALIVE PER 100"

Constraint: 16:9. Exactly these four labels. Show only a hand and forearm - no face, no body, no blood, no injury. The person must read as alive and reaching. Sombre and hopeful, never gruesome.
```

---

## What this does to the deck

Slide 4 stays diagram-led — cost, risk and procurement are inherently diagrammatic and the arguments
there are numerical. Everything else gains a photographic anchor:

| Slide | | | |
|---|---|---|---|
| 2 Proposed Solution | `P2.1-frog` 🎬 | **C4 six at first light** 🎬 | `F1-sachet` |
| 3 Technical Approach | **C1 the truck is the brain** 🎬 | `F2-buried-person` | **C5 four hazards** 🎬 |
| 4 Feasibility | `F4-cost-ladder` | `F5-when-it-fails` | `F6-money` |
| 5 Impact | `R1-8-survival-wall` | **C6 the void** 🎬 | `P5.3-dashboard` 🎬 |

`P2.2-hero`, `R2-2-handover-dark`, `R2-4-gps-denied`, `R3-8-event-dust` and `R1-9-uncounted` become
the bench — and `R2-2` is good enough that if C4 disappoints, swap it straight in.

**F3 three-tiers is cancelled.** C1 does its job better and does it cinematically.
