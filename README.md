# Documentary Skill for Claude Code

Make a short faceless documentary with Claude Code: researched facts with sources, a narrated script, animated scenes built in code (maps, timelines, big numbers, diagrams), automatic sync to the voice, and a 1080p MP4.

Example inside: **The Panama Canal — The $375 Million Shortcut** (`film_template.html`).

## What you need
- [Claude Code](https://claude.com/claude-code)
- Google Chrome, FFmpeg, Python 3
- An [ElevenLabs](https://elevenlabs.io) account for the narrator's voice
- Whisper for sync: `pip install openai-whisper`

## How to use
1. Download this repo (green **Code** button → **Download ZIP**) and unzip it.
2. Copy the `documentary-skill` folder into `~/.claude/skills/`.
3. Ask Claude Code: *"Make a short documentary about the Hoover Dam."*
4. Claude follows `SKILL.md`: research → script → scenes → voice → sync → check → render.

## Files
| File | What it does |
|---|---|
| `SKILL.md` | The step-by-step process Claude follows |
| `research_prompt.md` | Prompt for researching facts with sources |
| `script_format.md` | Script format with a screen plan |
| `film_template.html` | Example film (Panama Canal): map, timelines, numbers, lock diagram |
| `voice.py` | Sends each chapter to ElevenLabs |
| `sync.py` | Whisper word timings → `plan.json` |
| `render.py` | Frame-by-frame render in headless Chrome → FFmpeg |
| `lib/` | D3.js and world map data (licenses in `lib/LICENSES.txt`) |

Always check the facts before you publish.

## Credits
Map data: [Natural Earth](https://www.naturalearthdata.com) via [world-atlas](https://github.com/topojson/world-atlas) (ISC). Drawing: [D3.js](https://d3js.org) (ISC).
