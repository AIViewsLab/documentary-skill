"""Transcribe the chapter MP3s with Whisper and write plan.json for film_template.html.

  python3 sync.py voice/ [--title 3.5] [--gap 0.7]
plan.json = {"title": s, "duration": s, "ch": {"01": {"start": s, "dur": s, "words": [{"w","s","e"}, ...]}, ...}}
"""
import argparse, glob, json, os, subprocess
import whisper

ap = argparse.ArgumentParser()
ap.add_argument("folder"); ap.add_argument("--title", type=float, default=3.5); ap.add_argument("--gap", type=float, default=0.7)
a = ap.parse_args()
model = whisper.load_model("small.en")
t, plan = a.title, {"title": a.title, "ch": {}}
for f in sorted(glob.glob(os.path.join(a.folder, "*.mp3"))):
    num = os.path.basename(f)[:2]
    dur = float(subprocess.check_output(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", f]))
    r = model.transcribe(f, word_timestamps=True, language="en")
    words = [{"w": w["word"].strip(), "s": round(w["start"], 2), "e": round(w["end"], 2)} for s in r["segments"] for w in s["words"]]
    plan["ch"][num] = {"start": round(t, 3), "dur": round(dur, 3), "words": words}
    print(num, f"{dur:.1f}s", len(words), "words")
    t += dur + a.gap
plan["duration"] = round(t + 2.5, 3)
json.dump(plan, open("plan.json", "w"), ensure_ascii=False)
print("plan.json written, film length", plan["duration"], "s")
