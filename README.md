# Kestrel — SIH 2026

A drone that finds people after a landslide or flood.

**Team:** Drone Syndicate · **Team ID:** 133478
**Problem Statement:** [SIH26177](given/problem-statements/SIH26177.md) — Qualcomm Inc · Hardware · Robotics & Drones
**Deadline:** 20 September 2026

---

## The final PPT

**[kestrel-ppt/deck/KESTREL-SIH26177-idea-submission.pdf](kestrel-ppt/deck/KESTREL-SIH26177-idea-submission.pdf)**

6 pages. This is the file that gets uploaded to the SIH portal.

Built by [`kestrel-ppt/deck/build.py`](kestrel-ppt/deck/build.py). If anything changes, re-run that
and the layout is re-checked automatically — no overlapping text, nothing running off the page.

---

## The two live links on the PDF

| | Link |
|---|---|
| **Try the AI yourself** (QR on slide 3 and 6) | https://huggingface.co/spaces/anshumanatrey/kestrel-survivor-detection |
| **Watch the drone fly** (link on slide 6) | https://review.px4.io/plot_app?log=fe88f4b8-f677-4e81-8b96-e6512ebe8af2 |

Both are public. No login.

---

## Where every number on the PDF came from

We used four free websites. Each one did a different job.

### 1. Kaggle — the free training computer

**What it is:** a website that lends you a powerful computer for free.

**What we did:** training an AI needs a fast graphics card. A laptop doesn't have one. So we sent the
job to Kaggle and it ran for **2 hours 26 minutes**.

**What we got:** a trained model that spots people in drone photos. **It finds 95 out of 100 people**,
and when it says "person" it is right **97%** of the time.

**On the PDF:** slide 3, *"Trained, not borrowed"* → `mAP@50 0.952` is that 95%.

Files: [`model/`](model/)

### 2. Qualcomm AI Hub — the free chip rental

**What it is:** Qualcomm lets you send a file over the internet. They run it on a **real Qualcomm chip
in their building** and tell you exactly how fast it went.

**What we did:** sent our trained model. They ran it on two of their chips.

**What we got — every speed number on the PDF comes from here:**

| | Speed |
|---|---|
| Our model on the Arduino Ventuno Q | **1.72 milliseconds** |
| Our model on the RB3 Gen 2 | 10.77 milliseconds |
| A second AI (search-by-description) | 0.87 milliseconds |
| **Both together** | **2.59 milliseconds** |

They also confirmed **every part of our model ran on the AI chip**, none of it fell back to the slow
processor. That is the `247/247 NPU` on the slides.

**Why it matters:** we did not guess. We did not say "it should be fast." They gave us the number,
with a job ID a judge can look up.

**On the PDF:** slide 3 *"Measured and flown"* · slide 6, the table at the bottom.

### 3. Hugging Face — the free website host

**What it is:** a free place to put a working web page online.

**What we did:** built a page where anyone drops in a photo and watches our model find the people.

**What we got:** a public web address. No login, no password.

**One nice detail:** the AI runs **inside the visitor's own browser**. Nothing is sent to a server.
The problem statement asked for AI that works without internet — this page is proof.

**On the PDF:** the QR code on slide 3, and the same link on slide 6.

Files: [`kestrel-ppt/demo/`](kestrel-ppt/demo/)

### 4. GitHub — the free flight simulator

**What it is:** GitHub lends free computers too. Not for AI, for running programs.

**What we did:** ran the real drone flight software (PX4 — the same one on actual drones) and flew
our search pattern: **30 metres up, 4 metres per second, back and forth over 220m × 90m**.

**What we got:** a flight recording. We uploaded it to **Flight Review**, the website the drone
industry uses to check flight logs. It gave us a public link.

**Why we bothered:** we are in the **Hardware** category. A demo page and speed numbers are all
software. This is the only thing that shows the aircraft actually flying.

**On the PDF:** slide 6, the *"PX4 Flight Review: public flight log"* line.

Files: [`tools/fly_survey.py`](tools/fly_survey.py) · [`.github/workflows/px4-survey.yml`](.github/workflows/px4-survey.yml)

---

## The two QR codes

| QR | Goes to | Made by |
|---|---|---|
| Slide 3, and left QR on slide 6 | the live demo | **Hugging Face** |
| Right QR on slide 6 | our code and notes | **GitHub** |

The flight link on slide 6 is a text link, not a QR — from **Flight Review**.

---

## One line each

- **Kaggle** → trained the AI → gave us the **95% score**
- **Qualcomm** → ran it on real chips → gave us the **speed numbers**
- **Hugging Face** → hosts the demo → gave us the **QR code**
- **GitHub** → flew the simulation → gave us the **flight link**

All four free. Nothing estimated. Every number on the slides came from one of these actually running.

---

## Folders

| Folder | What's in it |
|---|---|
| [`kestrel-ppt/deck/`](kestrel-ppt/deck/) | **the final PDF** and the script that builds it |
| [`kestrel-ppt/DATA.md`](kestrel-ppt/DATA.md) | every number with its source. The long version |
| [`kestrel-ppt/demo/`](kestrel-ppt/demo/) | the live demo's code |
| [`model/`](model/) | the trained AI, its score, its training graphs |
| [`tools/`](tools/) | the flight script |
| [`given/`](given/) | official SIH files — all 229 problem statements, the rules, the template |
| [`docs-dataset.md`](docs-dataset.md) | how we scraped the 229 problem statements |

---

## Still to do

- [ ] Upload the PDF to the SIH portal (Team Leader only)
- [ ] Check the portal's file size limit — ours is 10 MB, can be made smaller if needed
