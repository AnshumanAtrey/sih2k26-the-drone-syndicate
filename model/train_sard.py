"""
Kestrel - fine-tune YOLOv8n for aerial search-and-rescue person detection.

Why this exists: the deck's detector is stock COCO YOLOv8n. COCO is ground-level
photography; a prone adult seen from 30 m is a different distribution and about
22 px tall. SARD is the published benchmark for exactly this task, so we train
on it and report a number comparable to the literature instead of a borrowed one.

Hard 3.0 h cap via ultralytics `time=` so the kernel cannot overrun its session.
"""
import os, glob, subprocess, sys, json, shutil, yaml, time

def sh(c): print(f"$ {c}", flush=True); subprocess.run(c, shell=True, check=False)

sh("pip -q install ultralytics==8.3.155 onnx onnxsim")
from ultralytics import YOLO
import torch
print("torch", torch.__version__, "cuda", torch.cuda.is_available(),
      torch.cuda.get_device_name(0) if torch.cuda.is_available() else "", flush=True)

# Do NOT hardcode the mount path - Kaggle's unpacked layout is not guaranteed to
# mirror the archive. Discover data.yaml, then work outward from it.
print("\n=== /kaggle/input tree (depth 3) ===", flush=True)
for dp, dns, fns in os.walk("/kaggle/input"):
    d = dp.replace("/kaggle/input", "").count(os.sep)
    if d > 3: dns[:] = []; continue
    print(" " * d + "|- " + os.path.basename(dp) + f"/   [{len(fns)} files]", flush=True)

yamls = glob.glob("/kaggle/input/**/data.yaml", recursive=True)
print("\ndata.yaml candidates:", yamls, flush=True)
if not yamls:
    print("FATAL: no data.yaml anywhere under /kaggle/input", flush=True); sys.exit(1)
cfg_path = yamls[0]
ROOT = os.path.dirname(cfg_path)
print("ROOT =", ROOT, flush=True)

cfg = yaml.safe_load(open(cfg_path))
print("\ndata.yaml as shipped:", json.dumps(cfg, indent=2), flush=True)

counts = {}
for split in ("train", "val", "valid", "test"):
    d = os.path.join(ROOT, split, "images")
    if os.path.isdir(d):
        counts[split] = len(glob.glob(d + "/*"))
        print(f"  {split:6} {counts[split]:6} images", flush=True)
if not counts.get("train"):
    print("FATAL: no train/images under", ROOT, flush=True); sys.exit(1)

cfg["path"]  = ROOT
cfg["train"] = "train/images"
cfg["val"]   = "valid/images" if counts.get("valid") else ("val/images" if counts.get("val") else "test/images")
cfg["test"]  = "test/images" if counts.get("test") else cfg["val"]
os.makedirs("/kaggle/working/cfg", exist_ok=True)
DATA = "/kaggle/working/cfg/sard.yaml"
yaml.safe_dump(cfg, open(DATA, "w"))
print("\nresolved config:", json.dumps(cfg, indent=2), flush=True)

# ---------------------------------------------------------------- train
t0 = time.time()
model = YOLO("yolov8n.pt")                       # COCO init, same arch the deck specs
model.train(
    data=DATA, epochs=80, imgsz=640, batch=16,
    time=3.0,                                    # hard wall-clock cap, hours
    patience=20, seed=0, workers=2, cache=False,
    project="/kaggle/working/runs", name="kestrel-sard", exist_ok=True,
    pretrained=True, optimizer="auto", val=True, plots=True,
)
print(f"\ntrained in {(time.time()-t0)/60:.1f} min", flush=True)

best = "/kaggle/working/runs/kestrel-sard/weights/best.pt"
m = YOLO(best)
metrics = m.val(data=DATA, imgsz=640, split="test")
res = {
    "mAP50":      float(metrics.box.map50),
    "mAP50_95":   float(metrics.box.map),
    "precision":  float(metrics.box.mp),
    "recall":     float(metrics.box.mr),
    "classes":    cfg.get("names"),
}
print("\n=== HELD-OUT RESULTS ===", flush=True)
print(json.dumps(res, indent=2), flush=True)
json.dump(res, open("/kaggle/working/metrics.json", "w"), indent=2)

# ---------------------------------------------------------------- export
# opset 12 + static batch so it drops straight into onnxruntime-web, same as the
# COCO model the Space ships today.
m.export(format="onnx", imgsz=640, opset=12, simplify=True, dynamic=False)
src = best.replace(".pt", ".onnx")
shutil.copy(src, "/kaggle/working/kestrel-sard-yolov8n.onnx")
shutil.copy(best, "/kaggle/working/kestrel-sard-best.pt")

# strip the value_info/IO duplication that broke our first AI Hub compile job
import onnx
g = onnx.load("/kaggle/working/kestrel-sard-yolov8n.onnx")
io = {t.name for t in list(g.graph.input) + list(g.graph.output)}
keep = [vi for vi in g.graph.value_info if vi.name not in io]
del g.graph.value_info[:]; g.graph.value_info.extend(keep)
onnx.checker.check_model(g)
onnx.save(g, "/kaggle/working/kestrel-sard-yolov8n.onnx")
print("\nONNX input :", [(i.name, [d.dim_value or d.dim_param for d in i.type.tensor_type.shape.dim])
                        for i in g.graph.input], flush=True)
print("ONNX output:", [(o.name, [d.dim_value or d.dim_param for d in o.type.tensor_type.shape.dim])
                       for o in g.graph.output], flush=True)
print("\nartifacts:", os.listdir("/kaggle/working"), flush=True)
