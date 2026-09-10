# Slide 2 — Proposed Solution

**Official section:** "Proposed Solution (Describe your Idea/Solution/Prototype)"
Template sub-bullets, verbatim: *detailed explanation of the proposed solution · how it addresses the
problem · innovation and uniqueness of the solution*

**Prompts: 3.** `P2.1` the frog *(done, dark)* · `P2.2` the hero *(done, dark)* · `P2.3` the SACHET loop *(to run)*.

> **Prompt text is not in this file.** The canonical, copy-paste-ready prompts live in
> [`../PROMPTS-TO-RUN.md`](../PROMPTS-TO-RUN.md), rewritten 11 Sep 2026 for the **white** official
> template with the style prefix already merged in. What stays here is the *argument* - why each
> visual exists, what it must land, and what to reject it for. Any prompt fence still shown below is
> the superseded dark v1, kept only for the Grand Finale deck where no template is imposed.


---

## The argument this page has to land

There is no problem slide in this template. Six pages, and page two is already "Proposed Solution" —
so the problem has to be established *by* the solution, in the same breath. The way to do that is to
stop arguing that India needs drones (a drone was already flown at Wayanad and it found nothing) and
argue the real gap instead:

> At Wayanad, a sensor reported **three breath signals** under the debris. 1,300 people searched that
> spot. Nothing was there — the assessment was that it may have been **a frog**. A separate thermal
> drone flew over Mundakkai and reported **zero human presence**. Six days, 1,300 personnel, 15 km²,
> 206 people never found.
>
> The gap is not aircraft. It is **resolution, corroboration, and area**. Kestrel fixes all three.

**Kestrel:** one mothership carrying Qualcomm compute hovers at 100 m as the brain and the radio
relay. Six ₹25,600 scouts launch from the NDRF vehicle and sweep at 30 m, where a person is 8 pixels
of thermal and 154 pixels of RGB instead of a tenth of one pixel.

**And for the person the cameras cannot see at all, Kestrel does not use cameras.** Thermal and RGB
both die behind a concrete slab — they are one vote in two coats. So the swarm also listens for the
**BLE and Wi-Fi beacons every phone emits with no SIM and no tower**, which pass through 3 m of
rubble and cost us nothing because the scout's brain *is* a Snapdragon handset; it carries
**FINDER-class vital radar** that reaches 9 m; it samples the **CO2 plume** a breathing person pushes
up through debris at 3 ppb; and it drops **acoustic pods** onto the pile that keep listening after it
has flown on. No stream is ever the decision on its own — the streams vote, weighted, and only a
cell that independent streams push past threshold becomes a survivor marker. The whole thing runs
on-device with no network at all.

---

## Layout

```
┌───────────────────────────────┬──────────────────────────────┐
│  P2.1  THE FROG               │  P2.2  KESTREL IN OPERATION  │
│  the failure, reconstructed   │  the system, one frame       │
│  (16:9, upper left)           │  (16:9, upper right)         │
├───────────────────────────────┴──────────────────────────────┤
│  P2.3  THE NETWORK ASKS, THE PHONE ANSWERS   (full width)    │
├──────────────────────────────────────────────────────────────┤
│  three native text chips: WHAT'S NEW  +  the 15 km² line     │
└──────────────────────────────────────────────────────────────┘
```

---

## P2.1 — The frog `[cinematic-diagrammatic]`

Paste the **Tier-1 prefix** from `STYLE.md` first - this is a dark, photographic asset that stays dark.

**Already rendered: `images/P2.1-frog.png` - no action.**

```
A single 16:9 frame split by one thin vertical amber rule into two unequal panels, left panel 60% wide.

LEFT PANEL: a night-time landslide debris field in the Western Ghats — churned red mud, snapped concrete slabs, uprooted trees, floodlights raking across it, small distant silhouettes of dozens of rescue workers in orange with headlamps scattered across the rubble at different depths, a mechanical excavator paused. Above the rubble floats a translucent cyan holographic marker pin with concentric pulsing rings, pointing at one specific spot in the debris. Sombre, documentary realism, cold floodlight against warm mud.

RIGHT PANEL: an extreme close-up macro shot of the same rubble at that exact spot, lit by a single headlamp — and in a small gap between two wet concrete blocks sits one small brown frog, rendered in sharp photographic detail, its body glowing faint orange as if seen partly in thermal. Behind it, a faint thermal-camera pixel grid overlay of very large coarse squares.

Composition: the holographic marker in the left panel and the frog in the right panel sit at the same height, so the eye travels straight from one to the other.

Render style: photorealistic with restrained technical overlay. No gore, no bodies, no faces.

Text labels (render exactly, small uppercase technical type):
- top-left of LEFT panel, cyan: "WAYANAD 01 AUG 2024"
- beside the holographic marker, cyan: "3 BREATH SIGNALS"
- lower-left of LEFT panel, slate grey, stacked on three lines: "1,300 PERSONNEL" / "40 TEAMS" / "6 ZONES"
- top of RIGHT panel, amber: "NOTHING WAS FOUND"
- directly under the frog, amber: "POSSIBLY A FROG"

Constraint tail: 16:9. No other text anywhere in the frame. No watermark, no border, no lens flare.
```

*This is the most important image in the deck. It is a true, cited event, it is quietly devastating,
and it converts "multi-sensor fusion" from a template buzzword into the obvious answer to a
documented failure. If only one prompt gets three regeneration attempts, it is this one.*

---

## P2.2 — Kestrel in operation `[cinematic hero, HUD-labelled]`

Paste the **Tier-1 prefix** from `STYLE.md` first - this is a dark, photographic asset that stays dark.

**Already rendered: `images/P2.2-hero.png` - no action.**


```
Wide cinematic aerial three-quarter view at blue-hour dusk over a flood-and-landslide-hit Indian hill town: collapsed buildings, a mud-choked river, a broken road. In the near foreground on the intact road sits an orange-and-white NDRF response truck with its rear doors open, a lit interior, and a folding launch rail; two operators stand at a rugged tablet on a tripod.

Rising from the truck, four small matte-grey quadcopters in a staggered climbing line, and two more already out over the debris field flying low and level at rooftop height along parallel search lanes, each trailing a thin cyan flight-path ribbon so the lanes read as a visible sweep grid over the town.

High above and behind everything, one larger matte-black hexacopter hovering steady, unmistakably the parent aircraft — bigger, heavier, a small sensor gimbal beneath it and a whip antenna above. From it, faint translucent cyan radio arcs connect down to each scout and back to the truck, forming a visible mesh.

Lighting: cold blue ambient, warm amber spill from the truck interior, cyan rim-light on the airframes. Photorealistic, epic but restrained scale, hopeful rather than militaristic.

Text labels (render exactly, as small HUD tags with thin cyan leader lines to their subject):
- on the hexacopter: "MOTHERSHIP — QUALCOMM 12 TOPS"
- on the nearest low-flying quadcopter: "SCOUT 30 M AGL"
- on one radio arc: "LoRa MESH — NO NETWORK NEEDED"
- on the truck: "TRUCK-LAUNCHED — 6 SCOUTS"
- bottom-right corner of the frame, amber: "2.6 KM2 PER HOUR"

Constraint tail: 16:9. Exactly these five labels, nothing else. No weapons, no missiles, no military markings. No watermark, no border.
```

*Note the truck. The mothership does not air-launch the scouts and this image must not imply that it
does — six S500 scouts weigh ~7.2 kg against a 3 kg lift budget. See `DATA.md` §0, correction 1.*

---

## P2.3 — The network asks, the phone answers, the drone listens `[DATA-EXACT]` · **v2**

> **The closest call in this kit, and it is your call, not mine.** v1 (15 km² twice — crowd vs six)
> is the most immediately graspable image in the deck. But its comparison is already made twice more:
> as native text on this slide, and in full on Slide 5's survival wall, where the same 5-days-versus-6-hours
> gap becomes `+64 survivors per 100`. This slide's stated sub-bullet is *"innovation and uniqueness
> of the solution"* — and **novelty is criterion #1** in the official list. This is the most novel
> idea in the project, so on this slide it outscores a comparison we make elsewhere anyway. v1's
> render is retired to the finale deck; its prompt is archived at the bottom of this file.
>
> **If you disagree, the alternative is clean:** keep v1 here and put this on Slide 3 in place of the
> airframes cutaway. I'd resist that one — the airframes image is what carries the Qualcomm silicon
> and the recycled phone, and a Qualcomm panel should see their own board on the aircraft.

**-> Use entry 1 in [`../PROMPTS-TO-RUN.md`](../PROMPTS-TO-RUN.md) - "The SACHET loop", white/tier-2, prefix pre-merged.**

*The fence below is the superseded **dark v1** of this prompt. Finale deck only - do not run it for the submission.*

```
A 16:9 technical illustration on deep navy, composed as four numbered stages reading left to right across the frame, connected by one continuous cyan arrow that curves from stage to stage and finally loops back underneath the whole sequence to rejoin the first stage, so the process reads as a closed cycle.

STAGE 1: a cell tower standing intact on a hillside, emitting three broad concentric broadcast arcs outward across a small stylised valley below it. Several tiny phone icons scattered across the valley light up as the arcs pass over them.
STAGE 2: a close cutaway of rubble with a phone wedged in a void beneath a concrete slab. The phone's screen is dark, but a small Bluetooth glyph on it glows bright cyan, and three small concentric rings emanate outward from the phone and pass visibly THROUGH the surrounding concrete and out the top of the rubble.
STAGE 3: a small quadcopter flying low over that same rubble, with a translucent cyan reception cone beneath it catching the rings rising out of the debris. On the quadcopter's underside, a recognisable smartphone is visible mounted as its payload.
STAGE 4: a tactical map tile grid, in which one single cell is lit bright cyan and pushed to the top of a short vertical queue of three stacked list rows beside it.

Above the whole sequence, spanning the frame, two short contrasting header lines stacked one above the other, the upper one in amber and struck through with a thin line, the lower one in cyan.

Render style: clean isometric-technical illustration with restrained cutaway detail, generous space between stages, thin precise linework. Not a flowchart of boxes. No legend box.

Text labels (render exactly):
- upper header line, amber, struck through: "SACHET TODAY — EVACUATE"
- lower header line, cyan: "SACHET AS A SENSOR — BE DETECTABLE"
- at STAGE 1, stacked two lines, #E2E8F0 then slate grey: "1. CELL BROADCAST" / "1.43 BILLION PHONES, 36 STATES"
- at STAGE 2, stacked two lines, #E2E8F0 then cyan: "2. BLUETOOTH ON" / "RF PASSES THROUGH CONCRETE"
- at STAGE 3, stacked two lines, #E2E8F0 then cyan: "3. SCOUT LISTENS" / "ITS OWN PHONE RADIO — ZERO COST"
- at STAGE 4, stacked two lines, #E2E8F0 then green: "4. SECTOR PRIORITISED" / "SWARM RE-TASKED"
- one thin footnote line along the bottom edge, small slate grey: "C-DOT Cell Broadcast Solution, operationalised by NDMA as SACHET; 14.5 M tower cells; 134 bn alerts delivered"

Constraint tail: 16:9. Only the labels listed. The rings in stage 2 must visibly pass through the concrete, not around it. The arrow must close back on stage 1. No watermark, no border.
```

*Verify: the loop **must close** — the return arrow is what makes it a system rather than a pipeline.
And the phone on the scout's underside must be recognisable; that detail is what proves the stream
costs nothing. Figures trace to `DATA.md` §11c — `[DATA-EXACT]`.*

**Why this is the strongest idea in the project.** India has already built and switched on the
broadcast half. **C-DOT's Cell Broadcast Solution**, operationalised by NDMA as **SACHET** on the
ITU's Common Alerting Protocol, is integrated across **all 36 States and UTs with every Indian
mobile network**, reaches **1.43 billion citizens** through **14.5 million tower cells**, has
delivered **134 billion+ alerts in 19 languages**, and **overrides silent and Do Not Disturb.**

It is used to tell people to evacuate. **Nobody is using it to make survivors detectable.** One
broadcast to the affected cells only — *"if you are trapped: turn Bluetooth ON, do not switch your
phone off"* — turns every handset inside the disaster footprint into a beacon, over infrastructure
that already exists, at zero marginal cost. Phones emit BLE advertisements and WiFi probe requests
with no SIM, no service and no tower, RF passes through rubble that stops light and heat entirely,
and **the receiver is already on board** — the scout's brain *is* a Snapdragon handset, so its own
Bluetooth and Wi-Fi radios do the sensing for ₹0 and 0 grams.

Published precedent so this is not speculative: Sensors 10.3390/s22197502 and 10.3390/s22218433 both
put WiFi FTM and BLE on drones for locating victims under rubble; BlueFly and the ARTEMIS/Echo SAR
payload are fielded products. **We need presence, not identity** — MAC randomisation defeats
identification and does not defeat presence, and we neither need nor want to know whose phone it is.

**The line, named once.** Individual subscriber location from a telco is lawful-interception
territory under the DPDP regime and is the wrong ask. The clean layers are: outbound broadcast (zero
privacy cost, already national); **aggregate, pseudonymised sector counts** under a DDMA request on
the **Section 20, Telecommunications Act 2023** public-emergency basis, which names disaster
management explicitly; and on-aircraft passive presence sensing, which needs no telco at all. Layers
one and three we build. Layer two is a partnership, and we name it as future work rather than claim
it. Full reasoning in `DATA.md` §11c.

---

## Archived — P2.3 v1, 15 km² twice `[already rendered: images/P2.3-15km2-twice.png]`

Excellent render, all labels correct. Retired only for slide-budget reasons — its comparison survives
as native text below and in full on Slide 5. **Use it as the opening image of the Grand Finale deck.**

```
A single full-width editorial infographic on a deep navy ground, 16:9, laid out as two large panels side by side separated by generous negative space, no dividing line.

Each panel contains an identical stylised overhead map of the same destroyed valley — a pale grey-brown irregular blob shaped like a landslide scar running down to a river, drawn flat and cartographic, subdivided into a fine grid of 150 small square cells.

LEFT PANEL: the map is covered by 1,300 tiny amber human figure icons, densely and unevenly clustered, most of them piled into only a few grid cells while the majority of the grid sits empty and pale. Above the map, six large amber sun icons in a horizontal row, evenly spaced.

RIGHT PANEL: the same map, but crossed by six clean parallel cyan sweep lanes that together cover the entire grid edge to edge, with six small cyan quadcopter icons spaced along the lanes and a single cyan hexacopter icon hovering at the centre. Above the map, a single small cyan clock icon.

Render style: flat editorial infographic, the visual language of a good newspaper graphic — precise, generous, uncluttered. Not a chart. No axes, no bars, no legend box.

Text labels (render exactly):
- centred above the LEFT panel, amber, large: "5+ DAYS"
- under the LEFT panel, slate grey, stacked two lines: "1,300 PERSONNEL" / "206 NEVER FOUND"
- centred above the RIGHT panel, cyan, large: "5.8 HOURS"
- under the RIGHT panel, slate grey, stacked two lines: "6 SCOUTS, 2 OPERATORS" / "ONE SHIFT"
- centred between the two panels, vertically stacked, in #E2E8F0: "15 KM2" / "SAME ZONE"
- single thin footnote line along the very bottom edge, small slate grey: "Wayanad 2024 destruction area; Kestrel at 2.6 km2/h derived"

Constraint tail: 16:9. Only the labels listed. No watermark, no border, no drop shadows.
```

*The two panels are the same map at the same size — that is the whole rhetorical move. Do not let the
model make them different shapes or scales. If the icon counts come back visibly wrong (the left panel
should read as a crowd, the right as six), regenerate; the exact icon count does not matter but the
crowd-versus-six impression does.*

---

## Native text — three "what's new" chips

The template asks explicitly for *innovation and uniqueness*. Three chips, cyan headers, one line each.

| | Innovation | One line |
|---|---|---|
| 1 | **Corroboration before it is a marker** | No survivor is reported from one sensor on one aircraft. Thermal band + RGB pose + a second scout's angle must agree, and the confidence and evidence tiles ship with the marker. The Wayanad frog does not survive this gate. |
| 2 | **Cheap eyes, expensive brain, and nothing thrown away** | ₹25,600 scouts carry a *recycled Snapdragon phone* as their compute — Hexagon NPU, 4K camera, IMU, GNSS and LTE modem in one 190 g ₹9,000 part. The ₹50,000 Qualcomm board flies once, on the aircraft that stays safe at 100 m. |
| 3 | **Streams that do not fail for the same reason** | Thermal and RGB are one vote in two coats — both die behind concrete. Kestrel adds **phone RF (WiFi + BLE) through 3 m of rubble at zero added cost**, FINDER-class vital radar to 9 m, CO2 plume at 3 ppb, and dropped acoustic pods. Independence is what buys confidence, not sensor count. |
| 4 | **Resolution chosen by arithmetic, not by catalogue** | We sized the thermal sensor from ground-sample-distance maths and rejected our own first choice. At 30 m a 32×24 array puts a human at 10% of one pixel; a 160×120 Lepton 3.5 puts them at 8×2 pixels. Slide 3 shows the working. |

**The 15 km² line — native text, one line under the chips.** Carries what the retired P2.3 v1 showed:

> **Wayanad, 2024: 1,300 personnel, 40 teams, 6 zones, 15 km² — 5+ days.** Kestrel sweeps the same
> footprint in **5.8 hours** at 2.6 km²/h. Slide 5 puts that on the survival curve.

---

## 30-second script

> "At Wayanad in 2024, a sensor reported three breath signals under the rubble. Thirteen hundred
> people searched. There was nothing there — most likely a frog. A thermal drone flew the same site
> and reported zero human presence. Six days later, two hundred and six people had still not been
> found. The gap isn't aircraft — it's resolution, corroboration and area. Kestrel is a mothership
> carrying Qualcomm compute at a hundred metres, and six twenty-five-thousand-rupee scouts launched
> off the back of an NDRF truck that sweep at thirty metres, where a person is eight thermal pixels
> instead of a tenth of one. Nothing is called a survivor until thermal, pose and a second scout
> agree. Same fifteen square kilometres as Wayanad: five days becomes under six hours."
