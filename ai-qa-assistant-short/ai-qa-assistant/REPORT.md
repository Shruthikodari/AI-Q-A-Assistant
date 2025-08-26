


---


## REPORT.md


```md
# Report — Internship Q&A Assistant


## Objective
Build a simple, maintainable chat application for interns to ask questions about the training program. Answers must remain consistent with the official internship guidelines.


## Implementation
- Frontend: Streamlit with custom HTML/CSS for a clean chat look.
- AI: OpenAI `gpt-4o-mini` (via `openai` Python client) to generate answers constrained to the guidelines.
- Data: `data/guidelines.md` as single source of truth.


## How it enforces guideline-only answers
The prompt includes the entire guidelines file and explicit system instructions telling the model to only answer from those guidelines. If the model cannot find an answer, it responds with a fixed fallback message.


## Limitations
- The enforcement relies on prompt engineering; the model may still hallucinate in edge cases. Use human moderation for critical rules.


## Future Work
- Add citation highlighting (show which guideline lines were used)
- Logging and analytics for common questions
- Authentication for interns