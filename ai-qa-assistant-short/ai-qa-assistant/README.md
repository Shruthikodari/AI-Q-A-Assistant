# Internship Q&A Assistant


A polished Streamlit chat-style frontend that answers questions strictly from a `data/guidelines.md` file using OpenAI.


## Features
- Chat UI with HTML/CSS-styled bubbles
- Answers only from `data/guidelines.md` (source of truth)
- Easy single-file deploy with Streamlit


## Files
- `app.py` — the Streamlit application
- `data/guidelines.md` — your official internship guidelines
- `requirements.txt` — Python dependencies
- `CHANGELOG.md`, `CONTRIBUTING.md`, `LICENSE`


## Quick start
1. Create a virtual environment and install requirements:
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
