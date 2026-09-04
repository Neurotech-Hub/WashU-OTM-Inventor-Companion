# WashU OTM inventor companion

Tools to help **WashU inventors** give **OTM case managers** clearer context around an invention: a short, structured interview prompt plus a periodically refreshed snapshot of public [Office of Technology Management](https://otm.wustl.edu/disclose-inventions/) pages.

This does **not** file a disclosure, replace [InnovateIP](https://otminnovate.wustl.edu/log_in/), or give legal advice. The official record is still the InnovateIP form. The interview produces a **companion brief** you can attach so OTM can understand the story, evidence, and landscape faster.

## For inventors

**Use only a WashU-supported AI tool** that is approved for institutional use and that protects the confidentiality of unpublished inventions. Consumer ChatGPT, public Gemini, and similar products may store or train on what you type and can create a **public-disclosure risk**. If you are unsure, stop and ask OTM ([otm@wustl.edu](mailto:otm@wustl.edu)) or WashU IT before describing the invention.

### How to run the interview (~10 minutes)

1. Open an **institutionally approved** AI chat (or a Gem/agent your department has configured with this repo’s prompt).
2. If you are pasting the prompt yourself, copy everything **below the line** in [`prompts/invention-interview.md`](prompts/invention-interview.md).
3. Answer the confidentiality question first. Describe the invention only after you can confirm the tool is approved.
4. Complete the short interview. Download the Word brief (`OTM-companion-brief.docx` when the AI can produce it).
5. **File your disclosure in InnovateIP** and **upload the brief as a companion attachment**. You may also copy the Invention Description into the form. The brief does not replace the form.

### AI disclaimer

Output is **AI-assisted**. It is not a legal opinion, not a complete patent search, and not OTM’s assessment. Inventorship, patentability, and commercialization decisions stay with OTM and counsel. Verify facts before you or OTM rely on them. The brief itself should state that you used an approved institutional AI tool with appropriate confidentiality controls.

Questions about policy or filing: [otm@wustl.edu](mailto:otm@wustl.edu) · [Disclose inventions](https://otm.wustl.edu/disclose-inventions/) · [InnovateIP](https://otminnovate.wustl.edu/log_in/)

## What’s in this repo

| Piece | Role |
| --- | --- |
| [`prompts/invention-interview.md`](prompts/invention-interview.md) | Interview instructions for the AI (case-manager brief, not a second form) |
| [`kb/`](kb/) | Scraped public OTM pages (process, Gap Fund, DEP, policies, contacts) |
| `python -m otm_scraper` | Refresh `kb/` from otm.wustl.edu |
| `python scripts/combine_agent_prompt.py` | One file: prompt + knowledgebase for a single agent/Gem upload |

Details for maintainers: [`prompts/README.md`](prompts/README.md).

## Refresh the OTM knowledgebase

Python 3.11+. From the repo root:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -e .
python -m otm_scraper
```

Rebuilds `kb/pages/`, `kb/INDEX.md`, and `kb/ALL.md`. Combine for one agent upload:

```bash
python scripts/combine_agent_prompt.py
```

Writes `build/agent-prompt.md` (gitignored). Re-run the scraper when OTM updates public pages, then re-combine and re-upload to the agent.

**Crawl scope:** public HTML under `/disclose-inventions/` plus configured extras (default: `/forms/`). Not included: InnovateIP login content, PDF text extraction. Edit [`config.yaml`](config.yaml) for seeds, allowlists, or delay.

## License and copyright

Code, interview prompt, and this documentation are under the [MIT License](LICENSE).

`kb/` is a snapshot of **public web pages owned by Washington University in St. Louis**. It is not official OTM software, not an endorsement, and is not covered by the MIT License. Republish or rely on it only as your use of those public pages allows.

