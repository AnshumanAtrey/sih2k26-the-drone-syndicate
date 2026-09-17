# model/ — the detector, and how it was trained

`kestrel-sard-yolov8n.onnx` is what the live demo runs and what Qualcomm AI Hub profiled.
Everything here is preserved because the Kaggle kernel that produced it shows `ERROR`: training
and validation both completed, and it died on the final ONNX export (`No module named 'onnxscript'`).
The weights are good; only the export step failed, and that was redone locally.

## Held-out test split (570 images, 732 instances)

| Metric | Value |
|---|---|
| **mAP@50** | **0.952** |
| mAP@50-95 | 0.665 |
| Precision | 0.969 |
| Recall | 0.900 |

Single class `human`. YOLOv8n from COCO init, 183 epochs in 2.43 h on a Tesla T4, 640x640.

**Honest comparison:** published work reports YOLOv4 at **97.15% mAP@0.4** on SARD. Ours is
**95.2% at the stricter @0.5**, so it sits alongside the literature, not above it.

## Dataset

**SARD** — the published aerial search-and-rescue benchmark, 1,980 images, 6,525 person instances,
via `nikolasgegenava/sard-search-and-rescue` on Kaggle, already in Roboflow YOLO format.

Worth recording: this is the dataset Roboflow **403'd** on us (`DATA.md` Addendum 5 §26), which is
why that addendum planned a VisDrone fine-tune instead. SARD was on Kaggle the whole time, in better
condition, and is the better choice because it is the benchmark the literature reports against.

## Measured on Qualcomm silicon

| Device | Precision | Latency | Throughput | Compute units |
|---|---|---|---|---|
| Arduino Ventuno Q (IQ-8275, Hexagon v75) | INT8 | **1.72 ms** | 580.7 FPS | **247/247 NPU** |
| Dragonwing RB3 Gen 2 (QCS6490, Hexagon v68) | INT8 | 10.77 ms | 92.8 FPS | 247/247 NPU |

Faster than the stock COCO model (1.85 ms) because the single-class head is smaller than 80 classes.

## Reproducing

`train_sard.py` is the kernel as run. It discovers `data.yaml` under `/kaggle/input` rather than
hardcoding a mount path — the first attempt died in 11 s because I assumed the unpacked layout would
mirror the archive, and it did not. It also caps training at 3 h wall-clock so a kernel cannot
overrun its session.

Add `onnxscript` to the pip line to make the export step succeed in-kernel.
