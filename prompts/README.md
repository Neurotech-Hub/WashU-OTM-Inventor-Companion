# Interview prompts

Companion to the official WashU invention disclosure in [InnovateIP](https://otminnovate.wustl.edu/log_in/). These prompts do not file or recreate that form.

## Invention interview (~10 minutes)

**File:** [invention-interview.md](invention-interview.md)

Produces a downloadable **Word** companion brief for the **case manager** (`OTM-companion-brief.docx` when the AI can; Markdown then chat text as fallback):

1. Invention Description
2. Summary
3. Prior-art / competitive landscape (search when possible; suggested keywords secondary), plus optional pathway notes
4. Current Gaps

Inventor how-to (upload the file with the InnovateIP disclosure) is **chat-only**, not in the Word file. The file must open with an AI-assistance disclaimer. URLs should be clickable.

### ChatGPT / Gemini chat

1. Copy everything below the horizontal line in `invention-interview.md`.
2. Paste as the first message (or custom instructions).
3. Talk through the interview. The first question is a confidentiality gate (WashU-supported AI tool). Expect ~6 questions about the invention (including primary academic motivation), at most two domain follow-ups, and one optional “landmine” question. Negative form answers (no disclosure, no outside parties, internal funding) are omitted from the brief unless they change OTM’s next step.

### Gemini Gem

1. Gem instructions: same prompt (below the line in `invention-interview.md`).
2. Knowledge: upload `kb/ALL.md` (or `kb/INDEX.md` + `kb/pages/`) from this repo so pathway notes can cite OTM pages.
3. Investigators chat with the Gem; they still submit the real form in InnovateIP.

Re-run `python -m otm_scraper` when OTM website content changes, then refresh the Gem knowledge files.

To upload **one** file (instructions + knowledgebase) instead of two:

```bash
python scripts/combine_agent_prompt.py
```

Output: `build/agent-prompt.md`. Edit `invention-interview.md` and re-scrape `kb/ALL.md` independently, then re-run the combiner.
