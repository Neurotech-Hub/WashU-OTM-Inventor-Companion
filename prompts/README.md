# Interview prompts

Companion to the official WashU invention disclosure in [InnovateIP](https://otminnovate.wustl.edu/log_in/). These prompts do not file or recreate that form.

## Default inventor upload

**File:** [`../build/agent-prompt.md`](../build/agent-prompt.md)

[Download `agent-prompt.md`](https://raw.githubusercontent.com/Neurotech-Hub/WashU-OTM-Inventor-Companion/main/build/agent-prompt.md) and drag or attach it into an institutionally approved agent. It includes the interview instructions **plus** an up-to-date, extensive reference to public OTM pages.

Regenerate after editing the prompt or refreshing `kb/`:

```bash
python scripts/combine_agent_prompt.py
```

## Invention interview only (secondary)

**File:** [invention-interview.md](invention-interview.md)

Prompt-only (no embedded OTM knowledgebase). Use when the agent already has `kb/` attached separately, or for editing the interview instructions.

Produces a downloadable **Word** companion brief for the **case manager** (`OTM-companion-brief.docx` when the AI can; Markdown then chat text as fallback):

1. Invention Description
2. Summary
3. Prior-art / competitive landscape (search when possible; suggested keywords secondary), plus optional pathway notes
4. Current Gaps

Inventor how-to (upload the file with the InnovateIP disclosure) is **chat-only**, not in the Word file. The file must open with an AI-assistance disclaimer. URLs should be clickable.

### ChatGPT / Gemini / agent chat

1. **Preferred:** [Download `agent-prompt.md`](https://raw.githubusercontent.com/Neurotech-Hub/WashU-OTM-Inventor-Companion/main/build/agent-prompt.md) and drag or attach it into the agent interface.
2. **Secondary:** [Download `invention-interview.md`](https://raw.githubusercontent.com/Neurotech-Hub/WashU-OTM-Inventor-Companion/main/prompts/invention-interview.md), or copy the **entire** contents of [`invention-interview.md`](invention-interview.md) and paste as the first message (or custom / system instructions).
3. Talk through the interview. The first question is a confidentiality gate (WashU-supported AI tool). Expect ~6 questions about the invention (including primary academic motivation), at most two domain follow-ups, and one optional “landmine” question. Negative form answers (no disclosure, no outside parties, internal funding) are omitted from the brief unless they change OTM’s next step.

### Gemini Gem

1. Preferred: upload/drag [`../build/agent-prompt.md`](../build/agent-prompt.md) as instructions (includes OTM reference).
2. Alternative: Gem instructions = entire [`invention-interview.md`](invention-interview.md); knowledge = `kb/ALL.md` (or `kb/INDEX.md` + `kb/pages/`).
3. Investigators chat with the Gem; they still submit the real form in InnovateIP.

Re-run `python -m otm_scraper` then `python scripts/combine_agent_prompt.py` when OTM website content changes, and commit the refreshed files.
