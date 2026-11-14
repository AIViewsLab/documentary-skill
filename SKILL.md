---
name: documentary
description: Make a short faceless documentary (MP4) with Claude Code — researched facts with sources, a narrated script with a screen plan, animated scenes built in code (maps, timelines, big numbers, diagrams), voice from ElevenLabs, automatic sync to the narration, and a frame-by-frame render. Use when the user asks for a documentary, a history or engineering explainer video, or "make a film about X".
---

# Documentary

Work in this order. Show the user each result before moving on.

1. **Research** — use `research_prompt.md`. Web search official / university sources. Save `facts.md`: every number with its source; mark estimates and disagreements.
2. **Script** — follow `script_format.md`: 6–10 chapters `## 01 Title`, narration text, and a `[screen: ...]` line after every paragraph. Only facts from `facts.md`.
3. **Scenes** — copy `film_template.html` and rebuild the scenes for the new story (new colors, layout and scene types — never reuse the same look for every video). Everything is drawn in code: no stock footage, no AI images. Each scene reads word times through `W(chapter, word)`.
4. **Voice** — `python3 voice.py script.md voice/ <voice_id>` (needs an ElevenLabs API key in `.elevenlabs_key`). One MP3 per chapter.
5. **Sync** — `python3 sync.py voice/` runs Whisper (`pip install openai-whisper`) and writes `plan.json`: chapter start times + every word with its time.
6. **Check** — `python3 render.py http://localhost:8000/film_template.html check.png --frames 5,30,60,...` and look at every still for overlaps or empty screens.
7. **Render** — `python3 render.py http://localhost:8000/film_template.html film.mp4`, then mix the chapter MP3s (placed at the start times from `plan.json`) and quiet music with FFmpeg.

Serve the folder with `python3 -m http.server 8000` before steps 6–7.
