"""Send each chapter of a script to ElevenLabs and save one MP3 per chapter.

  python3 voice.py script.md voice/ VOICE_ID [model]
Chapters are "## NN Title". Lines in [brackets] are not read. Existing MP3s are skipped.
Put your API key in a file named .elevenlabs_key next to this script.
"""
import json, os, re, sys, urllib.request

KEY = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".elevenlabs_key")).read().strip()
MODEL = sys.argv[4] if len(sys.argv) > 4 else "eleven_multilingual_v2"
SETTINGS = {"stability": 0.45, "similarity_boost": 0.8, "style": 0.25, "use_speaker_boost": True}


def say(text, path, voice, prev="", nxt=""):
    data = {"text": text, "model_id": MODEL, "voice_settings": SETTINGS}
    if prev: data["previous_text"] = prev
    if nxt: data["next_text"] = nxt
    req = urllib.request.Request(f"https://api.elevenlabs.io/v1/text-to-speech/{voice}?output_format=mp3_44100_128",
                                 data=json.dumps(data).encode(), method="POST",
                                 headers={"xi-api-key": KEY, "Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=300) as r:
        open(path, "wb").write(r.read())


script, out, voice = sys.argv[1:4]
os.makedirs(out, exist_ok=True)
text = open(script, encoding="utf-8").read()
chapters = []
for part in re.split(r"^## (?=\d\d )", text, flags=re.M)[1:]:
    title, _, body = part.partition("\n")
    lines = [l.strip() for l in body.splitlines() if l.strip() and not l.strip().startswith(("[", "#"))]
    chapters.append((title[:2], "\n\n".join(lines)))
for i, (num, body) in enumerate(chapters):
    path = os.path.join(out, f"{num}.mp3")
    if os.path.exists(path):
        print("exists:", path); continue
    say(body, path, voice, chapters[i - 1][1][-300:] if i else "", chapters[i + 1][1][:300] if i + 1 < len(chapters) else "")
    print("saved:", path, flush=True)
