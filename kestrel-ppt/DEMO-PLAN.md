# DEMO-PLAN.md — the link judges can open

**Status: nothing built yet. Deadline 20 Sep 2026 — 4 days.**
Owner column is blank on purpose. Claim a row by putting your name in it and pushing.

Software teams put a live URL on their slide. **We are Hardware category (SIH26177), so we need the
hardware equivalent: something a judge opens in one click that proves the thing flies, sees, and runs
on Qualcomm silicon.** This file is how we get there.

---

## 0. The trap — read this before you put any link on a slide

**Qualcomm AI Hub job links are NOT public.**

Everything on AI Hub is private unless explicitly shared, and sharing means typing the **email
address of another AI Hub account holder**. There is no "anyone with the link" mode. A raw
`app.aihub.qualcomm.com/jobs/{id}` on the slide sends most judges to a login wall.

**The nuance we exploit:** a *Qualcomm* judge on a *Qualcomm* problem statement almost certainly has
an AI Hub account. So the job link is a flex for the panel that matters and a dead end for everyone
else. **Therefore: screenshot + job ID in the deck, never the bare link as the primary CTA.**

Source: `app.aihub.qualcomm.com/docs/hub/jobs.html`

---

## 1. What Qualcomm actually gives us

**There is no Qualcomm drone simulator. Nobody ships one.** Do not go looking for it. Three real
things exist instead:

| Tool | What it does | Free | Public link |
|---|---|---|---|
| **`qualcomm-qrb-ros/qrb_ros_simulation`** | Qualcomm's own **ROS 2 Jazzy + Gazebo** stack, explicitly for *"validation without physical Qualcomm robot prototypes"* | Apache | repo only |
| **Qualcomm Device Cloud (QDC)** | SSH into a **real RB3 Gen 2** in Qualcomm's cloud. Free minutes. RTSP video streaming supported | free tier | no — record it |
| **AI Hub Workbench** | compile · profile · run inference on real Snapdragon silicon | free | **no, login-gated** |

**Caveat that matters:** `qrb_ros_simulation` ships an RML-63 arm, two AMRs and a mobile manipulator.
**No aircraft.** It is not a drop-in drone sim.

**So the honest stack is:**

```
PX4 SITL + Gazebo        <- the airframe and the world (PX4 is already our flight stack)
qrb_ros_* ROS 2 nodes    <- perception, Qualcomm's own packages
QNN / AI Hub             <- the inference, on real Qualcomm silicon
```

The Qualcomm-ness is real, and it lives in the **perception and runtime layers** — not in a Qualcomm
drone simulator that does not exist. **Say it that way. Do not overclaim.**

Prior art to copy: Hackster, *"VLM-Driven ROS 2 Navigation on Gazebo via Dragonwing IQ-9075"* — almost
exactly our pattern, already running on Qualcomm silicon.

---

## 2. The plan — ranked by value per hour

| # | Artifact | Public? | Effort | Why it wins | Owner |
|---|---|---|---|---|---|
| **1** | **PX4 Flight Review** — upload a SITL ULog to `review.px4.io`, get a shareable analysis page | **yes, no account** | ~3–4 h | The aviation industry's own standard tool. A hardware judge recognises it instantly. **Proves flight, not just software** — the one thing software teams cannot fake | |
| **2** | **Hugging Face Space** (Gradio) — judge uploads a Wayanad/Nepal image, sees our person + hazard detections | **yes, free, no login** | ~2 h | Our direct equivalent of the software teams' live URL | |
| **3** | **AI Hub profile** of YOLOv8n INT8 on QCS6490 | screenshot only | ~1 h | Already `DATA.md` §26's top TODO. Replaces a **borrowed** number with **ours**, on their silicon | |
| **4** | **QDC screen recording** — the stack on a real RB3 Gen 2 → unlisted YouTube | **yes** | ~3–4 h | *"We ran it on your hardware"* without owning hardware | |
| 5 | Full Gazebo swarm mission video | yes | 1–2 days | Highest ceiling, and the item most likely to eat the slides rewrite. **Cut this first** | |

**Recommendation: do 1 + 2 + 3.** Roughly one focused day. That is a public flight log, a live
detector anyone can poke, and a Qualcomm-silicon profile — without touching the slides budget.
Item 4 if day two goes well. **Item 5 is the sacrifice.**

---

## 3. How to actually do each one

### Item 1 — PX4 Flight Review  `~3–4 h`

PX4 SITL writes a real ULog, identical in format to one from a real Pixhawk. Flight Review does not
know or care that it came from a simulator.

1. Build PX4 SITL with Gazebo — `make px4_sitl gz_x500`
2. Fly a **lawnmower survey** over a world sized to the Wayanad footprint (~15 km²), at **30 m AGL,
   4.0 m/s** — the numbers derived in `DATA.md` §21. Use QGroundControl's survey mission planner.
3. Include a **GPS-denied segment**: cut GPS mid-mission so EKF falls back to VIO. This is the PS's
   own bullet and it will show up in the log as a visible event.
4. Log lands in `build/px4_sitl_default/rootfs/log/<date>/*.ulg`
5. Upload at **https://review.px4.io** → public analysis URL, no account needed to view.

**Reject if:** the mission does not reach 30 m · there is no GPS-denied segment · the survey pattern
is not visible in the position plot. The plot *is* the artifact.

### Item 2 — Hugging Face Space  `~2 h`

1. `huggingface.co` account → **New Space** → SDK **Gradio** → visibility **Public**
2. `app.py` with a YOLOv8n person + hazard detector, `requirements.txt` with `ultralytics gradio`
3. **Ship 4–6 example images** pre-loaded so a judge clicks one and sees a result in two seconds
   without hunting for a file. This is the single highest-impact detail on this item.
4. Free CPU tier is fine — **and say on the page that it is CPU, and that the on-aircraft number is
   the AI Hub one from item 3.** Never imply the Space is running on Qualcomm silicon.

**Reject if:** no example images · the page claims or implies Qualcomm hardware · it needs a login.

### Item 3 — AI Hub profile  `~1 h` · **highest value, lowest effort, do this first**

```bash
pip install qai-hub
qai-hub configure --api_token <token from app.aihub.qualcomm.com>
```

Compile + profile YOLOv8n INT8 against **QCS6490** (base station) and **QRB2210** (scout). Free, on
real devices, no hardware needed.

Capture: **latency, throughput, and the compute-unit split (NPU vs GPU vs CPU).** That last one is
the money shot — it proves we are on the Hexagon NPU and not quietly on the CPU.

This retires the borrowed Foundries.io number in `DATA.md` §20 and replaces it with our model on our
silicon. **Screenshot it. Put the job ID on the slide, not the URL.**

### Item 4 — QDC recording  `~3–4 h`

`qdc.qualcomm.com` → Qualcomm ID → request free minutes on **Dragonwing RB3 Gen 2** → interactive
session → SSH. Run the detector on sample frames, screen-record, upload unlisted to YouTube.

**Reject if:** the terminal does not visibly show the RB3 Gen 2 hostname — the whole point is that a
viewer can see it is real Qualcomm hardware, not our laptop.

---

## 4. The landing page — one QR, not five links

**Judges will not click four links. They will click one.** And the deck ships as a **PDF that may be
projected**, so a **QR code beats a hyperlink**.

Build **one public page** holding everything: the Flight Review link, the HF Space embedded live, the
AI Hub screenshot + job ID, the QDC video, and a repo link. One QR on the slide points at it.

**Repo caveat — do not skip this.** `sih2k26-the-drone-syndicate` is **private**, and GitHub Pages on
a private repo needs a paid plan. **Do not just flip this repo public**: `DATA.md` now contains our
full strategic read on what Qualcomm wants and the hidden-criteria reasoning. That is not for judges
before judging.

**→ Make a separate small public repo for the landing page.** Nothing from `DATA.md` goes in it.

---

## 5. The line this buys us

> **Our detector ran on a real QCS6490 in Qualcomm's cloud, on frames from our simulated Wayanad,
> and the flight log is public.**

Every clause in that sentence is checkable by a judge in under a minute. That is the whole point.

---

## 6. Open decisions

- [ ] Who owns which row in §2 — put your name in the table
- [ ] Landing page: GitHub Pages on a new public repo, or something else?
- [ ] Do we spend day two on item 4 (QDC), or on the `slides/` rewrite? **They compete.**
- [ ] Which 4–6 example images ship with the HF Space — Wayanad, Nepal 2026, Assam?

## 7. Sources

- AI Hub job sharing — `app.aihub.qualcomm.com/docs/hub/jobs.html`
- `github.com/qualcomm-qrb-ros/qrb_ros_simulation`
- Qualcomm Device Cloud — `dragonwingdocs.qualcomm.com/Tools/Qualcomm-Device-Cloud/overview`
- PX4 Flight Review — `review.px4.io` · `docs.px4.io/main/en/log/flight_log_analysis`
- Hackster — *VLM-Driven ROS 2 Navigation on Gazebo via Dragonwing IQ-9075*
