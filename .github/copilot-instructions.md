# Copilot / AI Agent Instructions

Purpose: get an AI coding agent productive quickly by documenting the repository's structure, key workflows, and repo-specific gotchas.

## Quick-picture
- Models and experiments live under `Models/`.
  - `Models/text/llm/` contains the canonical LLM example (`llm.py`).
  - `Models/text/theory/` holds human notes and a non-machine `requirment.tex` listing common dependencies.
- The repo targets multiple LLM providers via LangChain-style adapters (OpenAI, Anthropic, Google/PaLM, Hugging Face).

## Quick-start (Windows)
1. Create & activate a venv:
   - python -m venv .venv
   - .\.venv\Scripts\Activate.ps1
2. Install key packages (use `requirment.tex` as guidance until a formal file exists):
   - pip install langchain openai python-dotenv numpy scikit-learn
3. Provide API keys via environment variables or a `.env` for local testing (`python-dotenv`).
4. Run the example (after fixing typos in `llm.py`):
   - python Models\text\llm\llm.py

## Repo-specific patterns & conventions
- Directory purpose:
  - `Models/`: model-related code and examples
  - `Models/text/llm/`: canonical LLM usage examples
  - `Models/text/theory/`: notes and a human-written list of expected integrations (not a machine-readable `requirements.txt`)
- Integrations: repo expects multiple LLM providers (OpenAI, Anthropic, Google/PaLM, Hugging Face) via LangChain-style adapters.
- Env management: `python-dotenv` is used to load secrets; prefer `.env` for local experiments and system env vars in CI.
- Virtualenvs: there is an in-tree `venw/` under `Models/text/theory` — treat it as a local dev artifact (do not rely on it for CI).

## Important, project-specific notes
- `Models/text/llm/llm.py` currently includes broken example code — fix imports and usage before executing.
- There is no CI or tests yet; add targeted pytest tests for behavior you change.
- Dependency list is informal in `Models/text/theory/requirment.tex` — add `requirements.txt` or `pyproject.toml` when adding deps and update the tex file.
- There is an in-tree virtualenv at `Models/text/theory/venw/` — treat it as a local artifact (do not rely on it for CI).

## Common small fixes agents will perform
- Fix example typos in `Models/text/llm/llm.py`. Use this corrected snippet as a template:

```python
from dotenv import load_dotenv
from langchain import OpenAI

load_dotenv()
llm = OpenAI(model="gpt-3.5-turbo")
print(llm("Where is the Eiffel Tower?"))
```
- When adding dependencies, update `requirements.txt` (or `pyproject.toml`) and mirror the change in `Models/text/theory/requirment.tex`.

## When editing or adding features
- If you add dependencies, also add a `requirements.txt` or `pyproject.toml` and update `Models/text/theory/requirment.tex`.
- Keep changes small and focused: fix typos in examples, add a working example script, or introduce a tests/ folder with pytest tests.
- Document any external API keys required and prefer `python-dotenv` for local testing.

## Where to look for more context
- `Models/text/llm/llm.py` — canonical LLM example (fix or expand)
- `Models/text/theory/requirment.tex` — human notes about integrations and dependencies
- `Models/` hierarchy for additional model experiments

---
Feedback? Tell me which sections need more detail (setup, test examples, CI suggestions) and I’ll iterate. ✅