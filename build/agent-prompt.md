# WashU OTM inventor companion (agent upload)

Generated: 2026-09-04
Includes the invention interview instructions plus an up-to-date snapshot of public OTM pages.
Sources: `invention-interview.md` then `ALL.md`. Edit those independently; regenerate this file.
Regenerate with: `python scripts/combine_agent_prompt.py`

---
You are an interview partner for a WashU investigator preparing an invention disclosure.

## Purpose

This interview does **not** replace the official disclosure at https://otminnovate.wustl.edu/log_in/. The investigator will still fill InnovateIP.

Your job is a **document from the inventor to the OTM case manager**: extra context so OTM can understand the invention. The Word file is not an instruction sheet for the inventor.

Finish in **about 10 minutes**. Prefer “good enough” over exhaustive.

## Hard limits

- Ask **one question at a time**.
- **Confidentiality gate first** (before any invention details), then **6 core questions**, then **at most 2** domain follow-ups, then **1 landmine sweep** (only if not already covered), then **1 wrap**. Then stop and write the brief.
- If they have not confirmed an internally supported, confidentiality-adequate AI tool, **do not ask about the invention** and **do not write a brief**.
- If the investigator already answered something, **do not re-ask**.
- Accept “skip / unknown / later.” Never stall on IDs, percentages, citizenship, addresses, award numbers, or file uploads.
- Do **not** walk InnovateIP hidden/reveal fields. Do **not** recreate Yes/No form answers in the report (“no public disclosure,” “no outside parties,” “internal funding only”) unless they change OTM’s next step.
- Do **not** declare inventorship, patentability, or freedom-to-operate.
- Keep your own talk short: one sentence of context max, then the question.
- **Never put inventor how-to in the Word file** (no InnovateIP URLs, no “file here,” no “upload this,” no “OTM may ask you…”). Those belong only in the chat after the file is ready.

## Start

Greet in 2–3 sentences: 10-minute prep; they still file in InnovateIP; you’ll produce a short Word brief they can attach for their OTM case manager. **Do not ask what the invention is yet.**

Then ask the confidentiality gate (exact intent; you may tighten wording):

> Before we go further: are you using a WashU-supported AI tool that adequately protects the confidentiality of your invention? Consumer/public chat tools may store or train on what you type and can count as a disclosure risk. Reply yes only if you are on an approved internal tool. If no or you are unsure, stop here and file in InnovateIP / ask OTM or WashU IT.

**If no, unsure, or they cannot confirm:** thank them, tell them not to describe the invention in this chat, point to https://otminnovate.wustl.edu/log_in/ and otm@wustl.edu. End the conversation. Do not extract invention details from any text they already pasted.

**If yes:** proceed to core Q1.

If their first message already describes the invention, still ask the gate first. If they then say no/unsure, do not produce the brief.

## Core questions (always)

Ask in order unless already covered (**after** a yes on the gate):

1. **What is it?** In a few sentences: what did you make or discover, and who is it for?
2. **Problem vs today.** What problem does it solve, and how is that better than the current alternative?
3. **What’s actually new?** The 2–4 things you believe are novel (your view, not a legal claim).
4. **Evidence.** Strongest data, prototype, or demo you have today — and the biggest missing experiment.
5. **Primary academic motivation.** What is driving this for you as a faculty/academic inventor? Offer these options; they pick **one primary** (a second is OK if they insist):
   - funding
   - publishing
   - supporting trainees/staff
   - expanding the current research program or its impact
   - commercialization / a for-profit venture
6. **What you want from OTM.** Patent question, partners, startup, research-tool sharing, Gap Fund / DEP, or “not sure.”

## Domain dig (optional, max 2 questions)

After Q3–Q4, pick **at most one** pack if the story clearly fits. Skip if mixed or unclear. Do not announce a long menu.

**Software / algorithm / digital tool**
- What is the product: code, model, workflow, or data?
- If licensed without the wet-lab method, would it still be useful? Any third-party code, models, or planned open-source vs restricted use?

**Research tool / reagent** (antibodies, plasmids, cell lines, epigenetic tools, kits)
- Is the invention the reagent, the protocol, the biological insight, or all three?
- Closest kit or method people use now? Any well-known backbones you built on (e.g. CRISPR, Tet-on, viral vectors) — names only, as a flag for OTM.

**Therapeutic / diagnostic / device**
- Stage of evidence (in vitro / animal / human) and who would use it (lab, clinic, patient).
- One competitor or standard of care you worry about.

Then return to remaining core questions. No second pack.

## Landmine sweep (one question)

Only if not already obvious. One combined question, not three:

> Anything OTM should treat as urgent or messy — a talk/paper/demo already done or soon, collaborators or materials/code from outside your lab, or federal/industry funding? If none of that applies, say so and we’ll skip it.

If they say none: **do not put that in the brief.** If they name something material: capture it once under **Flags for OTM** (see below). Do not interrogate.

## After the wrap question

Produce a **downloadable Word file** whenever this product can create one: `OTM-companion-brief.docx`. Simple headings and body. **Make every URL a clickable hyperlink** (Word hyperlink / linked display text, not a raw unlinked string). Same for Markdown fallback (`[text](url)`).

**Fallback order:** `.docx` → `.md` download → the same document sections as plain text in the chat. Do not apologize at length.

**Document header (required, before Section 1):** title `WashU OTM Companion Brief`, then this disclaimer in italics or a callout:

> This document was produced with AI assistance from an investigator interview. The inventor acknowledged the AI was approved for institutional use, including proper controls for the confidentiality level of the included content. It is not a legal opinion, not a complete patent search, and does not replace the InnovateIP disclosure. OTM and the inventor should verify all content before relying on it.

The Word file contains **only** the case-manager sections below (1–4). Do **not** include a filing checklist or any other inventor instructions in the file.

Keep **facts vs inferences** strictly separated:

- Sections 1–2: only what the investigator said. Omit empty/negative form recaps. Omit headings whose only content would be “none” or “not stated.”
- Section 3: preliminary search landscape, not inventor-stated fact.
- Section 4 **Current Gaps**: remaining unknowns useful to OTM (use case, evidence, architecture). Not a to-do list for the inventor.

### 1. Invention Description

**One short paragraph**, about **120–180 words** (hard cap **200**). Non-confidential; first person or lab voice. For the case manager (the inventor may also copy it into InnovateIP if they want).

Cover: what it is, problem, 2–4 differentiators, evidence stage. Do not list numbered novelty bullets. Mention disclosure, outside parties, or funding **only if they named something material** (not to say “none”).

### 2. Summary

Help the case manager **understand the invention**. Bullets, not an essay. **Required:**

- **One-liner**
- **Likely category** — story only, **not a filing instruction** (e.g. “sounds like a medical device / lighting intervention”). Do not tell them which InnovateIP radio to pick.
- **Novelty (investigator-claimed)**
- **Evidence / maturity**
- **Primary academic motivation** — their pick from the list (plus a second only if they named one)
- **Investigator ask**

**Optional — Flags for OTM:** include this heading **only** if something should change OTM’s next action, such as:

- public or imminent disclosure (date/venue if known)
- outside collaborators, vendors, materials, or code
- federal or industry (or other sponsor) funding that may create rights

Never write filler like “no public disclosure reported,” “no outside parties,” or “internal funding only.” The form already collects that.

### 3. Prior-art / Competitive Landscape

A **preliminary** landscape for the case manager — not a legal patentability opinion and not a substitute for OTM/counsel search. Do not title this “AI suggestions.” Do not include a “what to stress-test” subsection.

**Primary — do the prior-art search** if this product has web search, browsing, or similar. Run a few targeted queries (Google, Google Patents, PubMed, or equivalent) on the invention’s core differentiators. Then write the analysis from **what you actually found**. Keep it short: one paragraph plus up to 5 bullets.

- Lead with **closest approaches the investigator named**.
- Then **what the search turned up**: 3–5 closest product classes, commercial systems, or publications. For each, one clause on how this invention seems to differ.
- Cite **only retrieved hits**: clickable title or product name pointing at the **bare URL** (no `utm_source`).
- **Never invent** patent numbers, PMIDs, authors, years, or URLs. If a hit is thin or behind a paywall, say so.

**If you cannot search:** say so in one sentence, then give a category-level landscape (no fake citations). Do not pretend you searched.

**Secondary — suggested search terms (always include, after the landscape).** Up to 3 Boolean or keyword strings for Google / Google Patents / PubMed. These support the landscape; they are not a substitute for it.

Then at most 2 commercialization pathway notes using WashU OTM context if available (traditional license, research tool / Quick MTA, startup / Quick Start, Gap Fund for **non-drug** technologies **after** disclosure, Domain Expert Program). Say when something probably does **not** fit. Clickable OTM URLs. If you lack WashU-specific knowledge, say so and stay generic. Never invent policy.

### 4. Current Gaps

For the **case manager**: 2–4 bullets on what is still unclear about the *technology* (first commercial/clinical claim, custom vs off-the-shelf parts, evidence still needed, scope). Frame as gaps in the record, not questions the inventor is instructed to go answer.

If a gap could have been resolved in this interview and still matters, you should have asked it before writing the file. Do not add a “questions OTM may still ask” or “questions for the inventor” heading.

## After the file is ready (chat only)

In the chat, **at most three sentences**, inventor-facing:

- The Word file is ready to download.
- **Upload this document as a companion to your InnovateIP invention disclosure.** It does not replace the form.
- Optional: they may copy **Invention Description** into the disclosure’s description field.

Do **not** paste the full brief in the chat if a file was created.

## If they dump everything at once

Extract what you can, ask only missing core questions (still one at a time), then produce the brief as a downloadable `.docx` (Markdown, then plain text, as fallback). Do not exceed the 10-minute budget. The confidentiality gate still comes first; skip the dump until they confirm yes.

---

# OTM knowledgebase

Source file: `/Users/mattgaidica/Documents/Software/OTMScraper/kb/ALL.md`

# OTM Disclose Inventions Knowledgebase
Scraped: 2026-09-03

Concatenated pages for Gemini Gem upload. Each section preserves its source URL.

---

# Disclose Inventions
Source: https://otm.wustl.edu/disclose-inventions/
Scraped: 2026-09-03

[>> Disclose online.](https://otminnovate.wustl.edu/log_in/) (WUSTL key required)

Under Intellectual Property (IP) policy of Washington University in St. Louis (WashU), creators are required to disclose inventions made using significant university resources and/or pursuant to a research project funded through corporate, federal or other external sponsors.

WashU’s Office of Technology Management is responsible for assessing whether or not an invention using WashU IP qualifies for patent or copyright protection.

---

# Gap Fund
Source: https://otm.wustl.edu/disclose-inventions/gap-fund/
Scraped: 2026-09-03

## Purpose and Aim

The Washington University Gap Fund provides funding and support for translational work that will increase the chances of licensing and successfully commercializing promising non-drug technologies created by WashU researchers. The Technology Development Team in the Office of Technology Management (OTM) works collaboratively with WashU researchers to identify critical uncertainties and pivotal assumptions relevant to the commercialization of technologies and formulate appropriate work plans to resolve and validate them. Once OTM provides a Gap Fund award, the Technology Development Team provides ongoing support to Gap Fund projects to ensure that they are completed as scoped and help relieve WashU researchers of some of the administrative burden associated with identifying, negotiating, and executing agreements with service providers and consultants.

The Gap Fund is agnostic regarding the commercialization pathway (i.e., new venture or traditional out-licensing to an established company). However, the Gap Fund does not provide awards to business ventures. All work on Gap Fund projects is performed within the fence line of WashU and researchers work on the projects in their capacities as WashU employees.

## Contact

[## Malcolm Townes, PhD, MBA](https://otm.wustl.edu/people/malcolm-townes/)

Director of Technology Development

- [314-273-3389](tel:314-273-3389)
- [townes@**nospam.**wustl.edu](mailto:%74ownes%40wu%73t%6c%2ee%64%75)

- [LinkedIn](https://www.linkedin.com/in/malcolmtownes/)

##### Office Hours Appointments Available

Questions? Interested in discussing a potential project?

Schedule an office hours appointment here.

[Link to booking page for Malcolm Townes](https://outlook.office.com/bookwithme/user/a0c73ace80b642aeae740361caf93955%40wustl.edu/meetingtype/aSj-f5a9KUOYvCIvbxJ8sQ2)

##### Announcements

> We really appreciated the opportunity to pitch and hear from the committee members – getting additional feedback and learning what kinds of questions we’ll be asked during future pitches is enormously valuable.
>
> WashU Gap Fund applicant on presenting to the Gap Fund evaluation panel

## Eligibility

- The researcher must have a WashU appointment that is captured under the IP policy.
- The technology must be a non-drug innovation.
- Proof-of-feasibility of the technology must have been demonstrated.
- The technology must be disclosed to the WashU Office of Technology Management (OTM) and must be properly assigned to WashU prior to submission of an application.
- There must be a reasonable probability of securing adequate intellectual property protection for the technology.
- Please see the FAQs section below for other relevant guidelines.
- If you have questions about the eligibility requirements, please contact either the OTM case manager for the technology or Dr. Malcolm Townes for assistance.

## Application Process

All technologies presented to a Domain Expert Program (DEP) or Innovation Roundtable (IRT) panel conducted by OTM are automatically considered for a WashU Gap Fund award. Additionally, at any time during the year, WashU researchers may submit a proposal for technologies that have not been selected for presentation to a DEP or IRT panel. OTM accepts these types of proposals (i.e., ad hoc proposals) year-round on a rolling basis.

### **How to Submit an *Ad Hoc* Proposal: Step by Step**

1. Contact the OTM case manager for the technology to verify that the invention disclosure has been processed and the technology has been properly assigned to WashU and to confirm the appropriateness of the intended use of funds.
2. Prepare an initial pitch deck (see the Gap Fund project pitch deck template in the Tools and Resources section below). Make sure that you indicate the OTM technology reference number for the technology. Email the pitch deck to [townes@wustl.edu](mailto:townes@wustl.edu).
3. Perform a “dry run” of the presentation with OTM New Ventures and the OTM Innovation Fund Manager to receive suggestions and feedback.
4. Submit the final version of the pitch deck to the OTM Innovation Fund Manager.
5. Present the technology and proposed project to a Gap Fund evaluation panel assembled by the OTM Innovation Fund Manager.
6. OTM completes its assessment and makes a funding decision.

*Note.* The above process is for technologies that have not been presented to a Domain Expert Program (DEP) or Industry Roundtable (IRT) panel. Eligible technologies presented to a DEP or IRT panel are automatically considered for a Gap Fund award. They do not need to go through the above process unless they did not receive a Gap Fund award at the time and the researcher has updated the proposed project plan based on feedback from the DEP or IRT panel and would like the technology to be reconsidered.

## Funding

- Technically, there is no maximum award amount.  Instead, the Gap Fund makes funding commitments in blocks of up to $55,000 for non-drug projects.
- Projects to de-risk and mature a technology for a given application may be considered for multiple rounds of funding (i.e., multiple consecutive awards) without the need to submit a new application.
- Researchers should only request the minimum amount that is needed to achieve the project objectives.
- Funding will be disbursed in tranches linked to milestones.
- The funds must be used for allowable costs and for tasks that are consistent with the purpose and aim of the Gap Fund (see FAQs for additional information).

## Project Selection, Oversight, and Support

OTM selects projects for a Gap Fund award by identify the critical uncertainties and pivotal assumptions that impact the chances of successfully commercializing a technology, assessing whether resolving or validating the identified uncertainties and assumptions is within the means of the Gap Fund, and evaluating whether there is a reasonably high probability that the proposed project will achieve a desired outcome of the Gap Fund program.  Input from external advisors is an important part of the project selection process for the WashU Gap Fund.

Once a decision has been made to fund a project, the OTM Technology Development Team and the WashU researcher agree upon a detailed scope of work (SOW) for the project. OTM uses this SOW to monitor and track the progress of the project. Additionally, the researcher is required to periodically report on the progress of the project against the SOW.  A member of the OTM Technology Development Team often participates in meetings between the research team and service providers.

## Tools and Templates

- [Pitch Deck Presentation template](https://wustl.box.com/s/eqpxomdngscgp4upuurmxgrpccaitoeq)
- [Generalized technology readiness level scale](https://wustl.box.com/s/5l11fqpfu7j9t3nt7io5sbg8phww35cq)
- [CMS Physician Fee Schedule Look-Up Tool](https://www.cms.gov/medicare/physician-fee-schedule/search)
- [FDA Orange Book: Approved Drug Products with Therapeutic Equivalence Evaluations](https://www.fda.gov/drugs/drug-approvals-and-databases/approved-drug-products-therapeutic-equivalence-evaluations-orange-book)
- [Search for FDA Guidance Documents](https://www.fda.gov/regulatory-information/search-fda-guidance-documents)
- [Fair Health Consumer medical procedure cost estimator](https://www.fairhealthconsumer.org/medical)

## Recommended Resources

Conducting Customer Discovery
:   - Austin, J. (2021). *[Customer discovery basics](https://chrome-extension://efaidnbmnnnibpcajpcglclefindmkaj/https://entrepreneurship.hbs.edu/Documents/Session%20Summary/HBSRock-Customer-Discovery-Final.pdf).* Rock Center for Entrepreneurship, Harvard Business School.
    - Blank, S. (2013). Customer discovery. In S. Blank, Four steps to the epiphany: Successful strategies for products that win (5th edition)(pp. 40-103). Wiley.
    - Blank, S., & Dorf, B. (2012). Chapter 3: An introduction to customer discovery. In S. Blank & B. Dorf, The startup owner’s manual: The step-by-step guide for building a great company (pp. 53-68). K&S Ranch.
    - Blank, S., & Dorf, B. (2012). Chapter 5: Customer discovery, phase two: “Get out of the building” to test the problem: “Do people care?”. In S. Blank & B. Dorf, The startup owner’s manual: The step-by-step guide for building a great company (pp. 189-226). K&S Ranch.
    - Blank, S., & Dorf, B. (2012). Chapter 6: Customer discovery, phase three: “Get out of the building” to test the product solution. In S. Blank & B. Dorf, The startup owner’s manual: The step-by-step guide for building a great company (pp. 227-256). K&S Ranch.
    - Mancini, D. & Horvath, D. (2024). [Innovations vs. features: Tips for designing your product](https://www.projectmedtech.com/projectmedtechpodcast/episode/2e545796/episode-196-or-dylan-horvath-founder-and-ceo-at-cortex-design-or-innovations-vs-features-tips-for-designing-your-product). *Project MedTech Podcast*. Ep. 196, 12:58-26:15.
    - Ulwick, A. (2022). [What is a Jobs-To-Be-Done?](https://youtu.be/Et4H4Ty1qhQ) [Video]. *YouTube.*
    - VentureWell. (2023, October 5). [Customer discovery: Assumptions & Interviews](https://venturewell.org/vw-videos/customer-discovery-assumptions-interviews/) [Video].
    - Wilcox, J. (2017, January 4). [How to interview your customers. *Customer Development Labs.*](https://customerdevlabs.com/2013/11/05/how-i-interview-customers/)
    - Wilcox, J. (2017, January 12). [Customer discovery: What do you ask?](https://youtu.be/OTkP2JDeGWM) [Video]. *YouTube.*

Formulating Effective Value Propositions
:   - Centers for Medicare and Medicaid Services. (2021). *[How to use the MPFS look-up tool.](https://www.cms.gov/medicare/physician-fee-schedule/search/documentation)* U.S. Department of Health and Human Services.
    - Centers for Medicare and Medicaid Services. (2023). *[List of CPT/HCPCS Codes.](https://www.cms.gov/medicare/regulations-guidance/physician-self-referral/list-cpt/hcpcs-codes)* U.S. Department of Health and Human Services.
    - Technological Leadership Institute, University of Minnesota. (2018, March 29). [Technically speaking: Lowering risk in early-stage technology commercialization](https://youtu.be/HwNcYgUCKiY)[Video]. *YouTube.*
    - Ulwick, A. W. (2014). [*What is Outcome-Driven Innovation (ODI)?*](https://strategyn.com/resources-dynamic/what-is-outcome-driven-innovation/) [Whitepaper].
    - Ulwick, A. W., & Bettencourt, L. A. (2008). Giving customers a fair hearing. *MIT Sloan Management Review, 49*(3), 62-68.

Medical Device Development
:   - [A Complete Guide to Bringing a Medical Device to Market](https://blog.greenlight.guru/hubfs/Complete%20List%20of%20Content%20Guides%20and%20eBooks/A%20Complete%20Guide%20to%20Bringing%20a%20Medical%20Device%20to%20Market.pdf) [Blog]
    - Greenlight Guru. (2025, August 28). [MedTech 101: What you need to know about the medical device industry](https://youtu.be/5uiyRyECjVU) [Video]
    - [The Device Development Process](https://www.fda.gov/patients/learn-about-drug-and-device-approvals/device-development-process)
    - [What Are the Four Different Types of Medical Device Risk Analysis?](https://www.youtube.com/watch) [Video]
    - [How to determine if your product is a medical device](https://www.fda.gov/medical-devices/classify-your-medical-device/how-determine-if-your-product-medical-device)
    - [Classification of products as drugs and devices and additional product classification issues: Guidance for industry and FDA staff](https://www.fda.gov/regulatory-information/search-fda-guidance-documents/classification-products-drugs-and-devices-and-additional-product-classification-issues)
    - [Guide to understanding health technology assessment](https://wustl.box.com/s/dxb0ocn3nv4ffk28goe9o8igsesqotid) (pdf)
    - [Medical technology assessment guidelines for Blue Cross Blue Shield of Massachusetts](https://wustl.box.com/s/l511cxkw5bgpdy51oeua3798d5y1l9uy) (pdf)

Medical Device Regulation
:   - FDA Center for Devices and Radiological Health and Center for Biologics Evaluation and Research. (2025, May 28). *[Requests for feedback and meetings for medical device submissions: The Q-Submission program – Guidance for industry and Food and Drug Administration staff.](https://www.fda.gov/regulatory-information/search-fda-guidance-documents/requests-feedback-and-meetings-medical-device-submissions-q-submission-program)* U.S. Food and Drug Administration.
    - [Five Tips for a Competitive Regulatory Strategy](https://blog.greenlight.guru/hubfs/blog-files/5-Tips-for-a-Competitive-Regulatory-Strategy.pdf) [Blog]
    - Greenlight Guru. (2020, July 13). [*How to prepare and conduct pre-submission meetings*](https://youtu.be/W_DaHm1EDZk) [Video]. *YouTube.*
    - [Medical Device Regulations/FDA Approval](https://www.youtube.com/watch) [Video]
    - [Planning Your Medical Device Global Market Regulatory Strategy](https://www.greenlight.guru/blog/medical-device-global-market-strategy) [Blog]
    - [What actually happens in a Pre-Submission meeting with FDA? Part I](https://blog.sierralabs.com/what-actually-happens-in-a-pre-submission-meeting-with-fda-part-1) [Blog]
    - [What actually happens in a Pre-Submission meeting with FDA? Part II](https://blog.sierralabs.com/what-actually-happens-in-a-pre-submission-meeting-with-fda-part-ii) [Blog]

Additional Resources
:   Office of the Vice Chancellor for Research 2025 Researcher Forum: OTM’s Malcolm Townes, PhD, MBA, presented at the 2025 WashU Researcher Forum in a session titled, “Translating Research Discoveries Into Beneficial Products and Services: Lessons from the WashU Gap Fund Operated by the Office of Technology Management”.

    A recording and slides from the presentation are available on [Box](https://wustl.app.box.com/s/tht0ubxbbwccrunexq0fmcypz1yixfpr). (WUSTL-key protected)

    Office of the Vice Chancellor for Research 2024 Researcher Forum: OTM’s Malcolm Townes, PhD, MBA, presented at the 2024 WashU Researcher Forum in a session titled, “Crossing the ‘Valley of Death’: How the WashU Gap Fund Helps Increase the Chances for Promising Technologies to Make a Difference”.

    A recording and slides from the presentation are available on [Box](https://nam10.safelinks.protection.outlook.com/). (WUSTL-key protected)

## Frequently Asked Questions (FAQs)

**What are the goals and desired outcomes of the WashU Gap Fund?**
:   There are two primary goals of the WashU Gap Fund:

    1. Increase the probability of commercializing promising WashU technologies
    2. Cull technologies without a meaningful chance of being commercialized from the portfolio

    To accomplish these goals, projects must achieve one or more of the following desired outcomes:

    1. Substantially increase the probability that supported technologies are sufficiently attractive to compel established companies to license and commercialize them.
    2. Substantially increase the probability that supported technologies being commercialized via startup ventures are market competitive.
    3. Substantially increase the probability that supported technologies not commercialized via traditional mechanisms achieve meaningful adoption and use.
    4. Substantially increase the probability that the researchers will obtain significant amounts of external grant funding to further develop and mature supported technologies.
    5. Determine whether a technology has no meaningful chance of being commercialized.

How is the WashU Gap Fund different from the LEAP program?
:   The Gap Fund is an integrated component of OTM’s workflow to move promising technologies from the laboratory to commercial use. The objective of the Gap Fund is to strategically deploy capital to help OTM accomplish its mission of transferring technologies created from the research conducted at WashU to the marketplace so that they can be used to benefit society.

Is the WashU Gap Fund a competition program?
:   In operating the Gap Fund, OTM has made a conscious decision to move away from the open competition model to make better use of its limited resources. The new model enables OTM to provide much better support to those technologies that are funded as well as technologies that are not yet ready for gap fund assistance. In the end, the new model holds promise to enable more WashU technologies to be successfully commercialized than the previous funding programs.

Does the WashU Gap Fund provide funding to university start-up companies?
:   No, the Gap Fund does not provide funding to university start-up companies. The funding that the Gap Fund provides is directed to the laboratories of WashU researchers, who use the established WashU processes and procedures for contracting services and making purchases. As such, WashU owns any additional intellectual property (whether patentable or non-patentable) that is developed from gap funded projects.

Who is eligible to receive WashU Gap Fund support?
:   Any WashU researcher in good standing who has properly assigned their intellectual property rights for inventions and creations to the university is eligible to receive Gap Fund support.

What exactly does “non-drug technology” mean?
:   A “non-drug technology” is any technology that does not satisfy the criteria for a drug as defined by the U.S. Food and Drug Administration (FDA). Generally, a “non-drug technology” is:

    a.) any item that is not intended to be metabolized by humans or animals to diagnose, cure, mitigate, treat, or prevent disease, or

    b.) any item that is not intended to affect the structure or function of the body or organs of humans or animals at the molecular level

Can an researcher submit multiple applications for more than one project?
:   A person may submit multiple technologies for consideration. Because the WashU Gap Fund has very limited resources to support the maturation and de-risking of all non-therapeutic technologies across the entire university, an individual is generally limited to serving as principal investigator (PI) for only one active Gap Fund award at any given time. However, an individual may be allowed to serve as PI on more than one active Gap Fund award if there is compelling justification. When deciding whether to provide multiple simultaneous awards to a single PI, the status of the PI’s current active Gap Fund awards will also be taken into consideration. There is no limit to how many projects on which a person may be a non-PI team member.

When are applications for the Gap Fund accepted?
:   Applications and nominations for the Gap Fund are accepted at any time.

Can an investigator request more than $55,000 for a project?
:   The limit for a single Gap Fund award is $55,000 under current guidelines. Proposed projects with budgets significantly greater than this will be broken down into sequential sub-projects with budgets up to the $55,000 limit per award. A stage-gate approach will be used but the Gap Fund will only commit to providing $55,000 in funding at a time. Subsequent awards may be given if the results of the prior sub-projects warrant it.

For what can the funds be used?
:   The financial support provided by the WashU Gap Fund can only be used for direct Project costs. Funds are intended to cover costs directly related to achieving the objectives of the Project scope of work (SOW) including, but not limited to, the following:

    - Services from contract research organizations (CROs)
    - Consulting or professional service fees
    - Materials and supplies
    - Specialized equipment not capable of being obtained through partnerships, renting, or leasing
    - Testing services

    Funds cannot be used for university overhead or new venture start-up costs including, but not limited to, the following:

    - Facilities and administration (i.e., overhead) costs
    - Employee salaries and fringe benefits (except in rare instances on a case-by-case basis)
    - Student tuition remission, fellowships, and grants
    - Consulting or professional service fees for preparing organizational registrations documents
    - Organization registration filing fees (e.g., incorporation filing fees, attorney’s fees)
    - Fees associated with licensing intellectual property
    - Office expenses
    - Marketing and advertising expenses

Can a researcher receive a WashU Gap Fund award if they already have a grant from a funding agency?
:   Yes, a researcher can receive a WashU Gap Fund award if they already have a grant from a funding agency. However, the researcher must demonstrate that the work to be performed under the Gap Fund award cannot be performed under the grant from the funding agency.

What is considered “failing to perform” on a Gap Fund award and what are the consequences?
:   Failing to perform on a Gap Fund award can mean a variety of things including, but not limited to, the following:

    - Not performing the scope of work described in the award memorandum of understanding (MOU)
    - Unilaterally changing the direction of the project and performing work that has not been agreed upon by OTM
    - Spending the funds on the tasks other than those specified in the award MOU
    - Not providing the project deliverables as specified in the award MOU
    - Abandoning a project without notifying OTM
    - Project durations extending well beyond the agreed timeline without approval from OTM

    In cases where OTM determines that the researcher has failed to perform, OTM may terminate the project or withhold funds from the project at its sole discretion. Additionally, if the researcher has multiple simultaneous Gap Fund projects, OTM may withhold funds from one project if the researcher fails to perform on another project.

Can undergraduate students work on a Gap Fund project?
:   Because of intellectual property rights issues, undergraduate students cannot work on a Gap Fund project without prior notice to and agreement by OTM.

Can graduate students work on a Gap Fund project?
:   There are several types of students that fall under the term “graduate student”.  The only graduate students who can work on Gap Fund projects are those who are subject to the requirements and obligations specified in the WashU Intellectual Property Policy or those who are being compensated for their work on the project and agree to assign their intellectual property rights to WashU as part of the compensation agreement.

How are projects selected to receive Gap Fund awards?
:   The process for evaluating proposed Gap Fund projects is less about identifying winners and losers and more about determining if there is any way that an award can sustantially advance the technologies toward successful commercialization.  Decisions about whether to provide a Gap Fund award for a project are made with input from external advisors.  The criteria for providing an award are as follows:

    - The technology and the researcher satisfy the eligibility requirements.
    - The work plan focuses on critical uncertainties and pivotal assumptions (CUPAs) that are most relevant to making the technology competitive in the marketplace and are within the means of the WashU Gap Fund to resolve or validate.
    - There are no other viable options for funding the tasks necessary to appropriately resolve or validate the CUPAs.
    - There are no obvious fatal flaws that would prevent commercialization.
    - The probability of any potential single point of failure (SPOF) occurring is reasonably low.
    - The work plan prioritizes resolving and validating CUPAs with the lowest evaluation costs.
    - The work plan calls for resolving and validating independent CUPAs before addressing subsequent chained CUPAs.
    - The probability of achieving one or more program desired outcomes is sufficiently high.

    Several factors are considered when assessing whether a proposed project has a sufficiently high probability of achieving a desired outcome of the program.  These include, but are not limited to, the following:

    - Ability of the innovators to contribute to commercialization and out-licensing efforts
    - Coachability of the project leader and research team
    - Commercialization aptitude of the project leader and team
    - Alignment of the research and development plan with the market need
    - Anticipated increase in technology maturity level
    - Anticipated strength of intellectual property protection
    - Anticipated impact of the technology if it is successfully commercialized
    - Estimated size and growth of the target market

Are there any other guidelines that investigators should be aware?
:   Other guidelines of which investigators should be aware include the following:

    · WashU must be the lead institution if the technology has collaborators from other institutions

    · The maturity level of the technology must be at least the equivalent of TRL-3 but no higher than the equivalent of TRL-6 on the NASA technology readiness level (TRL) scale

    · There must not be any unresolved compliance issues with the technology

    · The technology must not yet be licensed or otherwise encumbered

    · There must be no apparent conflicts of interest that appear unmanageable or unresolvable

    · The investigator must be in “good standing” with WashU

    · There must be no serious unresolved issues with the investigator’s laboratory

    · Technologies previously denied funding but not determined to be unviable may be reconsidered after sufficient actions have been taken to address deficiencies

What is the technology readiness level scale?
:   The technology readiness level (TRL) scale is an ordinal scale that was developed by the National Aeronautics and Space Administration (NASA). It is used to characterize and describe the maturity level of a technology. The NASA TRL scale ranges from 1 (least mature) to 9 (most mature). OTM uses an adaption of the NASA TRL scale which ranges from 0 (least mature) to 9 (most mature).

---

# Licensing Process
Source: https://otm.wustl.edu/disclose-inventions/licensing-process/
Scraped: 2026-09-03

Under Washington University in St. Louis’s Intellectual Property (IP) policy, creators are required to disclose inventions made using significant university resources and/or pursuant to a research project funded through corporate, federal or other external sponsors.

## What is an invention?

The discovery or creation of a new material (either a new manufactured product or a new composition or matter), a new process, a new use for an existing material, or any improvements of any of these.

If you think you have discovered an invention with commercial potential, [submit an invention](https://otminnovate.wustl.edu/log_in/) in advance of making the invention public.

---

## Technology Transfer Process

Step 1: Invention Disclosure Submission
:   Inventor [submits an invention disclosure](https://otminnovate.wustl.edu/) with:

    - description of the invention;
    - names of all creators;
    - funding information;
    - discloses other information (e.g. potential publications)

Step 2: Invention Assessment
:   - Evaluation of the invention to determine:
      - the appropriate intellectual property protection mechanism (e.g. patent).
      - the potential commercial applications/products and the market(s).
    - Evaluation process takes 60 days from the date of submission.
      - The outcome of the analysis is communicated to the creators through an in person meeting, by phone or email.
      - There are multiple outcomes of the analysis:
        - Protect the invention (see step 3);
        - More research being required for the invention to be protected or commercialized;
        - Commercialize the technology without protection (see step 4);
        - In some circumstances, WashU will not retain ownership (in which case a discussion around return of IP will occur).

Step 3: Intellectual Property Protection
:   - WashU protects the intellectual property using the appropriate mechanism (e.g. filing a patent, registering a copyright, etc.).
    - WashU informs inventors of the protection chosen and corresponding rights and restrictions.
    - If patent protection is opted, then WashU partners with the creators and selected external patent counsel to draft a patent application.

Step 4: Marketing & Outreach
:   - WashU identifies potential industry partners and delivers to them a non-confidential marketing package promoting the technology.
    - WashU solicits feedback from industry contacts and facilitates technical discussions between interested parties and the creators.
    - WashU sets up a confidentiality/non-disclosure agreement (CDA/NDA) to protect information exchange between the interested parties and the creators.

Step 5: Licensing of Intellectual Property
:   - Once an industry partner expresses interest in commercializing WashU IP, a  licensing agreement is generated.
    - The licensing agreement includes both financial terms (e.g. milestone payments, royalty payments, etc.) and diligence milestones that define timelines and goals for the development and commercialization of the technology.

Step 6: Product Development & Commercialization
:   - The industry partner develops and commercializes the WashU technology in accordance with the diligence milestones set forth in the licensing agreement.
    - According to the financial terms of the agreement, the industry partner will make payments to Washington University, and WashU will distribute a percentage of this income to the technology’s creators per WashU’s IP policy.
    - WashU will solicit progress reports annually from the company to assess progress against development milestones.

## Income Distribution Process

Creator Share Forms
:   The Creator Share Form will dictate how the WashU distributes any funds among creators. This Creator Share Form will be considered perpetual and irrevocable except in those cases where the Lead Creator elects at the time of signing to amend the Creator Share Form at the lime of licensing. This situation occurs when the invention is not in a final state when disclosed. If this indication is made, WashU will seek an amended Creator Share Form upon the execution of a license agreement. At that point, the Creator Share Form will be considered perpetual and irrevocable.

Technology Weighting
:   In some cases, a license agreement may bundle several distinct technologies under a single agreement. In these instances, the lead creator will need to determine the weighting of each technology relative to the overall license agreement. For example, if two patent families were licensed under the same agreement, the Lead Creator may determine that one patent family contributed to 90% of the value of the license agreement while the other patent family only contributed 10%.  In this scenario, the Creators identified on the Creator Share Form of the first patent family would be entitled to 90% of the Creators’ Share of the license income, while Creators on the 2nd would get 10%.

    In the situation where multiple technologies are bundled under a single license agreement, the income that is received may be specific to just one of the technologies or span multiple technologies. The Lead Creator will make the determination as to whether technology-specific income will be shared only with the Creators of the contributing technology or technologies or whether the income will be shared with the Creators of all of the technologies included in that license agreement. This determination will be made at the time the license is executed.

    All Creators will have an opportunity to review income distributions in more detail upon request to WashU. Creators should consult the IP policy for raising issues/disputes under any allocation.

Identification of Creators
:   If an invention disclosure is submitted by a non-faculty Creator, WashU will request that the Creator Share Form be approved by the lab’s primary faculty member or other such appropriate lead (e.g. department chair).

Distribution of Income
:   One month prior to the distribution of income, a report will be sent to any Creator receiving income that summarizes the amount that he or she is to receive. If the individual has any question about how this income was calculated, he or she can contact the WashU for more detailed information.

    Finally, income will be distributed on a quarterly basis going-forward with distributions occurring in September, December, March, and June.

    | Funds Recieved | Distributed By: |
    | --- | --- |
    | June — August | 9/30 |
    | September — November | 12/31 |
    | December — February | 3/31 |
    | March — May | 6/30 |

## Release, Return, Re-Assignment of Intellectual Property

In the event that WashU Office of Technology Management assesses a technology disclosure and decides not to pursue IP protection, or has protected or commercialized the IP, but will no longer do so, the IP may be released, returned, or re-assigned to the Inventors. Please answer the question(s) below to guide you to the correct process.

---

# New Ventures
Source: https://otm.wustl.edu/disclose-inventions/new-ventures/
Scraped: 2026-09-03

The New Ventures team was formed in 2022 to grow the number of high value Washington University intellectual property startups. By working directly with the university’s research community, New Ventures helps in navigating the process of launching a startup. The team engages with WashU faculty innovators and entrepreneurs by connecting them to tools, investors and mentors to catalyze startups as they launch and scale their companies based on WashU intellectual property.

The New Ventures team supports company formation with:

- Business case creation: New Ventures helps with the formulation and refinement of a value proposition and pitch deck structure.
- Entrepreneurship education and coaching for the research community.
- Preparing nascent startup teams to engage with investors by identifying and making introductions to relevant investors
- Working to grow a broad and diverse investor community, and communicating opportunities for investment through a quarterly newsletter.

Learn more about how OTM and the New Ventures team help foster WashU startups below:

### Office Hours

OTM Office Hours is an in-person program series hosted by the New Ventures team that features current topics in tech transfer and innovation. Previous Office Hours events have covered topics such as: Intellectual Property 101, Funding, Career Options for a PhD, etc. Office Hours are typically held the second Thursday of the month and are open to all.

Check out our upcoming Office Hours events below:

03

Sep

## [OTM Office Hours: From Research to Reality](https://otm.wustl.edu/calendar_event/office-hours-from-research-to-reality/)

September 3, 2026

3:00 pm – 4:00 pm

08

Oct

## [OTM Office Hours: Practice Makes the Perfect Pitch](https://otm.wustl.edu/calendar_event/otm-office-hours-practice-makes-the-perfect-pitch/)

October 8, 2026

3:00 pm – 4:00 pm

### Contact Us

[## Karen Gheesling Mullis, PhD](https://otm.wustl.edu/people/karen-mullis/)

Director of New Ventures

- [314-747-0924](tel:314-747-0924)
- [mullis@**nospam.**wustl.edu](mailto:m%75lli%73@%77ustl%2ee%64u)

- [LinkedIn](https://www.linkedin.com/in/karen-gheesling-mullis-ph-d-23a4504/)

[## Liz Peek, PhD](https://otm.wustl.edu/people/liz-peek/)

New Ventures Senior Associate

- [314-747-1794](tel:314-747-1794)
- [peek@**nospam.**wustl.edu](mailto:peek@wust%6c.ed%75)

- [LinkedIn](https://www.linkedin.com/in/liz-peek-319a978a/)

[## Greg Markiewicz](https://otm.wustl.edu/people/greg-markiewicz/)

New Ventures Principal

- [314-747-1794](tel:314-747-1794)
- [markiewicz@**nospam.**wustl.edu](mailto:markiew%69%63%7a%40%77%75s%74%6c%2e%65d%75)

- [LinkedIn](https://www.linkedin.com/in/markiewiczgregs2020/)

### WashU Startup Investment Opportunities

Interested in learning more about investment opportunities in existing WashU startups? Sign up for the Office of Technology Management’s quarterly *Venture Update* newsletter [here](https://app.e2ma.net/app2/audience/signup/2045105/1970398/).

### WashU Startups

Learn more about companies based on WashU intellectual property and the latest advances from WashU researchers [here](https://otm.wustl.edu/washu-innovations/washu-faculty-startups/).

### Tools and Resources

[Pitch Deck Template](https://wustl.box.com/s/hqxsbk5ohypc51yoj62vg56ma4eanig8) (PPT) (password protected) : WashU innovators can utilize this pitch deck template as a guide for refining the quality and content of their pitch presentation for a investor meeting, a conference presentation, a funding opportunity, etc.

---

# Other Agreements
Source: https://otm.wustl.edu/disclose-inventions/other-agreements/
Scraped: 2026-09-03

In addition to licenses and Material Transfer Agreements (MTAs), WashU Office of Technology Management also handles other agreements in its promotion of technology transfer including confidential disclosure agreements (CDAs) and Inter-institutional Agreements (IIAs).  WashU does not participate in consulting agreements.

## Confidential Disclosure Agreements

##### ALSO KNOWN AS NDAS (NON-DISCLOSURE AGREEMENTS)

CDAs allow for the exchange of confidential information between Washington University faculty and staff with outside third parties under obligations to protect and preserve the information being shared.

OTM negotiates CDAs regarding discussions *related to the potential licensing of university developed inventions/technologies* that have been or will be disclosed to OTM through our invention disclosure process.  OTM puts these CDAs in place to avoid public disclosure and preserve the possibility of patent protection.

If you are about to, or already have disclosed a technology to OTM and would like to enter into a confidentiality agreement with a potential licensee, please follow the instructions listed here.

Send your OTM business development contact the following information:

- Type of agreement: one-way or two-way flow of information;
- Name of Company, contact name, email address and phone number;
- Who in your department will be disclosing information – list everyone you believe will be involved.
- What is the subject matter you plan to discuss;
- Purpose of the disclosure or exchange of information;
- Anticipated date of discussion.

OTM only reviews CDAs related to potential licensing activity.  If you have a CDA that is not related to licensing discussions,  please contact the Joint Research Office for Contracts (JROC) at [ResearchContracts@email.wustl.edu](mailto:ResearchContracts@email.wustl.edu)

## Inter-institutional Agreements

Washington University may enter into an Inter-institutional Agreement (IIA) for several reasons:

- Researcher(s) at Washington University are collaborating with researcher(s) at another institution and have invented something together
- Researcher(s) have a dual appointment with Washington University and another institute (for example Veterans Affairs or the Donald Danforth Plant Science Center)
- Researcher(s) began work which led to the creation of an invention at one institution and then move to Washington University and continue their work on this invention

In each of the above situations, the inventions are jointly owned by the university and the other institution. In an IIA both parties agree as to who will take the lead in patenting and licensing activities and how any revenue from licensing will be shared.

If you have created an invention in collaboration with researchers from another institution or as an employee of multiple institutions or if you have continued work on an invention begun at another institution, please notify our office by submitting an invention disclosure form via [>> otminnovate.wustl.edu](https://otminnovate.wustl.edu/log_in/) (use WUSTL Key to log in.)

## Consulting Agreements

A consulting agreement with a company in private industry is a personal agreement in which OTM and Washington University does not participate. The university is not a legal party to the agreement, and as such, we strongly recommend that you retain a lawyer to review the agreement to protect your best interests.

In order to help avoid confusion between your personal obligations to the company and your work here at Washington University, any consulting agreement with a company should contain the following language:

>  “Notwithstanding anything herein to the contrary, Company agrees that CONSULTANT serves Company under this Agreement in his individual capacity, as an independent contractor, and not as an agent or representative of Washington University (“Institution”), that Institution exercises no authority or control over CONSULTANT while acting in such capacity, that Institution receives no benefit from such activity, that CONSULTANT and/or Company cannot and will not make use of Institution resources or Institution managed funding in acting in such capacity, that Institution is not a party to this Agreement, and that Institution makes no representations or warranties under this Agreement and assumes no liability or obligation in connection with any such work or service undertaken by CONSULTANT. Company further agrees that any breach, error, or omission by CONSULTANT acting in such capacity or otherwise under this Agreement, shall not be imputed or otherwise attributed to Institution. Moreover, nothing in this Agreement shall be read or understood to encumber, in any way, any intellectual property that Institution claims ownership of through the Institution’s Intellectual Property Policy as such may be amended from time to time.”

If you receive research support from an entity that subsequently wants to retain you (or someone under your supervision) as a consultant, OR if you (or someone under your supervision) has worked for a company as a consultant and the company then wants to provide research support you should disclose the change in relationship to the Disclosure Review Committee ([Jeneane Braden](mailto:BRADENJ@WUSTL.EDU), 314.747.4152).

For further guidance, please see the Washington University [Individual (Research) Conflicts of Interest Policy](https://research.wustl.edu/research-conflicts-interest-policy-guidelines/) or the [Institutional Conflict of Interest Policy](https://research.wustl.edu/institutional-conflict-of-interest-policy/).

---

# Tech Transfer Contact by WashU Department
Source: https://otm.wustl.edu/disclose-inventions/otm-contact-by-washu-department/
Scraped: 2026-09-03

Directory of WashU departments and their OTM tech transfer contacts.

| Department | Contact | Profile |
| --- | --- | --- |
| Anesthesiology | John Gill | [profile](https://otm.wustl.edu/people/john-gill/) |
| Biochemistry & Molecular Biophysics | Deepika Poranki | [profile](https://otm.wustl.edu/people/deepika-poranki/) |
| Biology | Jennifer Richards | [profile](https://otm.wustl.edu/people/jennifer-richards/) |
| Biomedical Engineering | Craig Weilbaecher | [profile](https://otm.wustl.edu/people/craig-weilbaecher/) |
| Bone Marrow Transplant | Charles Hanford | [profile](https://otm.wustl.edu/people/charles-hanford/) |
| Brown School of Social Work | Daniel Zou | [profile](https://otm.wustl.edu/people/daniel-zou/) |
| Cell Biology & Physiology | Jennifer Richards | [profile](https://otm.wustl.edu/people/jennifer-richards/) |
| Chemistry | John Gill | [profile](https://otm.wustl.edu/people/john-gill/) |
| Computer Science | Brett Maland | [profile](https://otm.wustl.edu/people/brett-maland/) |
| Department of Medicine | Deepika Poranki | [profile](https://otm.wustl.edu/people/deepika-poranki/) |
| Department of Medicine – Palliative Medicine | Courtney Jungers | [profile](https://otm.wustl.edu/people/courtney-jungers/) |
| Department of Medicine — Allergy, Immunology | Charles Hanford | [profile](https://otm.wustl.edu/people/charles-hanford/) |
| Department of Medicine — Bioorg, Chemistry, Molecular Pharmacy | Deepika Poranki | [profile](https://otm.wustl.edu/people/deepika-poranki/) |
| Department of Medicine — Bone & Mineral | Nathan Han | [profile](https://otm.wustl.edu/people/nathan-han/) |
| Department of Medicine — Cardiology | Frank Hardin | [profile](https://otm.wustl.edu/people/c-frank-hardin/) |
| Department of Medicine — Dermatology | Deepika Poranki | [profile](https://otm.wustl.edu/people/deepika-poranki/) |
| Department of Medicine — Endocrine, Metabolism | Frank Hardin | [profile](https://otm.wustl.edu/people/c-frank-hardin/) |
| Department of Medicine — Endocrinology | Frank Hardin | [profile](https://otm.wustl.edu/people/c-frank-hardin/) |
| Department of Medicine — Gastroenterology | Daniel Zou | [profile](https://otm.wustl.edu/people/daniel-zou/) |
| Department of Medicine — General Med Sciences | Charles Hanford | [profile](https://otm.wustl.edu/people/charles-hanford/) |
| Department of Medicine — General Medicine & Geriatrics | Frank Hardin | [profile](https://otm.wustl.edu/people/c-frank-hardin/) |
| Department of Medicine — Hematology | Jennifer Richards | [profile](https://otm.wustl.edu/people/jennifer-richards/) |
| Department of Medicine — Hospital Medicine | Frank Hardin | [profile](https://otm.wustl.edu/people/c-frank-hardin/) |
| Department of Medicine — Infectious Diseases | Courtney Jungers | [profile](https://otm.wustl.edu/people/courtney-jungers/) |
| Department of Medicine — Medical Oncology | Charles Hanford | [profile](https://otm.wustl.edu/people/charles-hanford/) |
| Department of Medicine — Nephrology | Frank Hardin | [profile](https://otm.wustl.edu/people/c-frank-hardin/) |
| Department of Medicine — Nutritional Science & Obesity Medicine | Frank Hardin | [profile](https://otm.wustl.edu/people/c-frank-hardin/) |
| Department of Medicine — Pharmacogenomics | Charlie Hanford | [profile](https://otm.wustl.edu/people/charles-hanford/) |
| Department of Medicine — Pulmonary | Frank Hardin | [profile](https://otm.wustl.edu/people/c-frank-hardin/) |
| Department of Medicine — Rheumatology | Nathan Han | [profile](https://otm.wustl.edu/people/nathan-han/) |
| Developmental Biology | Jennifer Richards | [profile](https://otm.wustl.edu/people/jennifer-richards/) |
| Earth & Planetary Sciences | Courtney Jungers | [profile](https://otm.wustl.edu/people/courtney-jungers/) |
| Electrical & Systems Engineering | Craig Weilbaecher | [profile](https://otm.wustl.edu/people/craig-weilbaecher/) |
| Emergency Medicine | Frank Hardin | [profile](https://otm.wustl.edu/people/c-frank-hardin/) |
| Energy, Environmental & Chemical Engineering | Brett Maland | [profile](https://otm.wustl.edu/people/brett-maland/) |
| Genetics | Daniel Zou | [profile](https://otm.wustl.edu/people/daniel-zou/) |
| Institute of Clinical and Translational Sciences | Nathan Han | [profile](https://otm.wustl.edu/people/nathan-han/) |
| McDonnell Center for the Space Sciences | Craig Weilbaecher | [profile](https://otm.wustl.edu/people/craig-weilbaecher/) |
| Mechanical Engineering & Materials Science | Brett Maland | [profile](https://otm.wustl.edu/people/brett-maland/) |
| Molecular Microbiology | Jennifer Richards | [profile](https://otm.wustl.edu/people/jennifer-richards/) |
| Neurology | Deepika Poranki | [profile](https://otm.wustl.edu/people/deepika-poranki/) |
| Neuroscience | John Gill | [profile](https://otm.wustl.edu/people/john-gill/) |
| Neurosurgery | Craig Weilbaecher | [profile](https://otm.wustl.edu/people/craig-weilbaecher/) |
| Obstetrics & Gynecology | Courtney Jungers | [profile](https://otm.wustl.edu/people/courtney-jungers/) |
| Occupational Therapy | Courtney Jungers | [profile](https://otm.wustl.edu/people/courtney-jungers/) |
| Olin Business School | Deepika Poranki | [profile](https://otm.wustl.edu/people/deepika-poranki/) |
| Ophthalmology & Visual Sciences | Deepika Poranki | [profile](https://otm.wustl.edu/people/deepika-poranki/) |
| Orthopedic Surgery | Charles Hanford | [profile](https://otm.wustl.edu/people/charles-hanford/) |
| Otolaryngology | Charles Hanford | [profile](https://otm.wustl.edu/people/charles-hanford/) |
| Pathology & Immunology | Deepika Poranki | [profile](https://otm.wustl.edu/people/deepika-poranki/) |
| Pediatrics | Courtney Jungers | [profile](https://otm.wustl.edu/people/courtney-jungers/) |
| Philosophy – Neuroscience – Psychology (PNP) | John Gill | [profile](https://otm.wustl.edu/people/john-gill/) |
| Physical Therapy | Craig Weilbaecher | [profile](https://otm.wustl.edu/people/craig-weilbaecher/) |
| Physics | Brett Maland | [profile](https://otm.wustl.edu/people/brett-maland/) |
| Population Health Sciences | Daniel Zou | [profile](https://otm.wustl.edu/people/daniel-zou/) |
| Psychiatry | Nathan Han | [profile](https://otm.wustl.edu/people/nathan-han/) |
| Psychological and Brain Sciences | Jennifer Richards | [profile](https://otm.wustl.edu/people/jennifer-richards/) |
| Radiation Oncology | Brett Maland | [profile](https://otm.wustl.edu/people/brett-maland/) |
| Radiology | John Gill | [profile](https://otm.wustl.edu/people/john-gill/) |
| Sam Fox School of Design & Visual Arts | Daniel Zou | [profile](https://otm.wustl.edu/people/daniel-zou/) |
| School of Law | Daniel Zou | [profile](https://otm.wustl.edu/people/daniel-zou/) |
| School of Public Health | Deepika Poranki | [profile](https://otm.wustl.edu/people/deepika-poranki/) |
| Statistics and Data Science | Brett Maland | [profile](https://otm.wustl.edu/people/brett-maland/) |
| Surgery | Craig Weilbaecher | [profile](https://otm.wustl.edu/people/craig-weilbaecher/) |
| The Genome Institute | John Gill | [profile](https://otm.wustl.edu/people/john-gill/) |

---

# Inventions & Licensing Policies
Source: https://otm.wustl.edu/disclose-inventions/policies-resources/
Scraped: 2026-09-03

Washington University in St. Louis is committed to the development, implementation, and maintenance of policies and guidelines that promote the compliant, ethical, and responsible design, conduct, reporting, and reviewing of research in accordance with federal, state, and local regulations and sponsoring agency policies and procedures.

- [Individual (Research) Conflicts of Interest Policy](https://research.wustl.edu/research-conflicts-interest-policy-guidelines/)
- [Institutional Conflict of Interest Policy](https://research.wustl.edu/institutional-conflict-of-interest-policy/)
- [Faculty & Startup Companies](https://www.wustl.edu/policies/startup.html "WUSTL Start Up Policy")
- [Intellectual Property Policy](https://washu.edu/policies/intellectual-property-policy/)
- [Private Use Restrictions](https://www.wustl.edu/policies/privateresearch.html "WUSTL Private Research Policy")

---

# Quick Start License
Source: https://otm.wustl.edu/disclose-inventions/quick-start-license/
Scraped: 2026-09-03

The Quick Start License is an initiative to foster the formation of new startup companies based on technologies created at Washington University in St. Louis.

The Quick Start initiative is a simplified process that will allow faculty to focus on the development and commercialization of products and is meant to streamline the contract negotiation process. The Quick Start License is also designed make university startups more attractive to potential investors and should increase the success of the university startups.

- [WashU OTM Quick Start User Guide](#QSuserguide)
- [Frequently Asked Questions](#QSfaq)

Quick Start License General Terms:

- An exclusive license with right to sublicense
- No payment for past patent costs, future patent costs to be paid by Licensee
- No upfront, annual or milestone fees
- Financial and diligence performance milestones based on a detailed business plan
- No equity for Washington University
- A fixed 2% patent royalty rate on sales of any product(s)
- No minimum annual royalty payments
- A sliding sublicense revenue starting at 15% that steps down to 5% over five years
- A 0.95% “success fee” at an exit event of the company
- Applies to a single, solely owned, patented, Washington University intellectual property asset (excludes software and copyrights)

WashU faculty and employees (graduate students, post-docs and staff) who are creators of an invention and have interest in obtaining a license from OTM for their startup company can start the process by contacting [OTM Staff.](https://otm.wustl.edu/meet-the-team/)

If the company desires to acquire additional patented or unpatented intellectual property, software, copyright, or material assets in the future (post-execution of a Quick Start License), a separate license agreement will be necessary. This agreement will entail fair market value terms and conditions, encompassing, but not limited to, patent and non-patent royalties, reimbursement for patent costs (past, present, future), upfront fees, license maintenance fees, minimum royalties, milestone payments, success fees, and equity considerations.

**What are next steps if you do not qualify for a Quick Start License?**

When a company does not meet the requirements for a Quick Start License, WashU will negotiate an exclusive license agreement. The terms and conditions of an exclusive license agreement will be negotiated by both parties, and will vary depending on the nature of technology, stage of development, ownership, etc. Typically, an exclusive license agreement will be considered, if the license includes:

1. Multiple intellectual property (IP) assets: patented and non-patented assets, copyrights, software, tangible research materials etc.
2. Copyright and/or software assets
3. Mature IP Asset: non-provisional filing, PCT application, foreign filing
4. Jointly owned IP asset

Considerations under an exclusive license agreement:

- Patent and non-patent royalties
- Patent costs: licensee will be responsible for past, ongoing and future patent expenses
- Upfront payments, milestone payments, license maintenance fees
- Diligence: technical and financing milestones
- Business plan
- License grant: exclusive license to patent rights and a non-exclusive license to tangible research property, technical information, software etc.

## User Guide

In an effort to spur innovation and entrepreneurship efforts in the St. Louis region; WashU OTM is offering a simple, ready-to-use license agreement for start-up companies based on the university’s patented intellectual property. The license agreement has been vetted by local community leaders, venture capitalists, contract attorneys to arrive at terms and conditions that are deemed fair and reasonable to WashU and the startup company.

The Quick Start License has a back-end loaded deal structure with no upfront payments, no past patent costs, no annual minimum fees, no minimum royalties, one low flat patent royalty rate and a success fee at the time of an exit/liquidation event. This would allow start-up companies to invest time and effort in developing the university technology.

The primary objective is to streamline the contract execution process for both parties in an effort to reduce the ensuing legal costs and increase deal flow. In order to qualify for this license the below mentioned terms and conditions should be met:

- You are a WashU employee, a founder of a start-up based on a solely owned patented WashU intellectual property (WashU IP) and an inventor on any such WashU IP
- The patented WashU IP is the basis for forming the new company
- A detailed business plan is provided to the OTM business manager handling the specific patented technology
- A CEO (preferably a person with experience and not the PI) and an experienced management team with a proven track record is in place to lead the commercialization of the licensed WashU IP

### **Quick Start License Approval Process**

The use of Quick Start license is contingent upon the submission of a business plan and approval by OTM. Once you have identified the WashU IP you are interested in licensing, please contact OTM. If you do not have an OTM business manager, please email [otm@wustl.edu](mailto:otm@wustl.edu) to have one assigned to you.

Please be prepared to submit the following documents to OTM:

- Detailed business plan.
- As a WashU employee and company co-founder you may need to obtain a separate conflict-of-interest approval from the CIRC. This process is independent of OTM and you are responsible for initiating and completing this process.
- The Quick Start license will be executed only upon completion of the COI approvals.

### **Business Plan**

All startup companies must submit a business plan to qualify for the Quick Start License. The plan must be written by the team (CEO, CBO, key leaders) who will be leading the company with help from consultants/advisors. The business plan serves as a blueprint outlining the company’s vision for the university technology and the commercialization pathway it intends to adopt. This is the centerpiece of the start-up enterprise and therefore utmost care and diligence must be taken in drafting this document and coming up with meaningful diligence milestones. The OTM business manager will contact you if there are additional questions/concerns. The execution of the Quick Start license is contingent upon satisfying any concerns/questions that may arise upon internal review of the Business Plan. While every attempt will be made to work with the start-up to ensure that it qualifies for the Quick Start license, WashU OTM will determine whether or not a start-up company qualifies for the Quick Start license.

- Company information
  - Name of company, address, nature/type of the company organization, and articles of incorporation.
  - Name of CEO and founding members and defined roles, number of employees: bio data and role of each individual (employee/consultants/advisors etc.)
  - Names of the members of the Board of Directors
  - Start-up governance and ownership
- Funding status
  - current investors -level of funding provided by each investor, background /track record for each investor
  - available funds and projected burn rate
  - timeline for fund raising efforts
  - financing objectives and plans, valuations
  - company pro-forma financials
- R&D development timeline
  - include detailed timelines and research and development (R&D) timeline, e.g. therapeutic — IND, Phase I, II, III, NDA filing timelines
  - provide diligence milestones in order to arrive at a go/no go decision with respect to the licensed WUSTL IP
  - operating plans for R&D
  - required partnerships or alliances needed for milestones
- Target market
  - Details regarding at least one lead indication/target market
    - prevalence, incidence
    - unmet need
    - target market size : penetration rate, 3-5 year net sales forecast
    - projected selling price, gross margins
- Marketing strategy
  - primary markets
  - distribution channels
  - potential partners
  - competitors: clearly outline the unique selling proposition (product/ service) , potential risks, market entry strategy, SWOT analysis

### **Contacts & Communications**

The primary and first point of contact for Quick Start license at WashU is the OTM business manager and at the company contact should be the CEO or his/her designate. The WashU faculty member who is the founder of the company should not be the primary point of contact for the company.

## Frequently Asked Questions

1. Who qualifies for the Quick Start License?
:   If you are a WashU employee, a founder of a startup based on a patented (solely owned) Washington University intellectual property (WashU IP) and an inventor on any such WashU IP.

2. I am a WashU employee and a co-founder but not an inventor on the WashU IP. Will my company qualify for this license?
:   No, you will not qualify (please refer to question 1).

3. I am a WashU employee, an inventor and a co-founder but the WashU IP is jointly owned with another university. Will my company qualify for this license?
:   Yes, but only if the third party is willing to accept the terms and conditions of the Quick Start License.

4. I am a WashU employee and an inventor but not a co-founder. Will the company qualify for this license?
:   No (please refer to question 1)

5. I am a WashU employee, an inventor and a co-founder of a company that has executed a license with Washington University previously. Can I re-negotiate the terms of the previous license?
:   No, you will not be able to re-negotiate the terms of the previous license.

6. What happens if an inventor wants to start a company but his fellow WashU co-inventor(s) do not?
:   The Washington University inventors will need to resolve this issue independent of OTM. The formation of a Washington University start up should be agreed upon by all inventors.

7. Who do I contact to discuss the Quick Start License?
:   Please email [otm@wustl.edu](mailto:otm@wustl.edu) and you will be connected to the appropriate business manager.

8. Is the Quick Start License negotiable?
:   No, the terms of the Quick Start License are fixed and if not acceptable, a more detailed and time consuming exclusive license agreement template will be used.

9. I have a few edits to the Quick Start License; what do I do next?
:   This agreement is intended to not require edits. However, if there are specific concerns you may discuss it with your OTM business manager. Please note that a request for additional edits will slow down the execution process because OTM will need to involve the Office of the Executive Vice Chancellor & General Counsel to review and comment on any such edits.

10. I do not have a business plan, can I sign the Quick Start License and submit the business plan later?
:   No, you will not qualify for the Quick Start License if you do not have a business plan. Please refer to the Quick Start License [User Guide](#QSuserguide).

11. I am uncertain what the diligence milestones are at the current time point; can I provide them post-execution of the Quick Start License?
:   No, you will not qualify for the Quick Start License. The diligence milestones should be part of your business plan.

12. What are the salient features of the Quick Start License?
:   In order to expedite and simplify the contract process and lessen the burden on startup companies, the Quick Start License template has a simple deal structure with one flat royalty rate, a low success fee at the time of liquidation/IPO (initial public offering), waiver on all past patent expenses, no upfront fees, no annual maintenance fees and no minimum annual royalties. However, the licensee will be responsible for all ongoing and future patent costs post-execution of the Quick Start License. Washington University will be in control of the prosecution process but the licensee will be copied on all relevant correspondence and have time for comment.

13. Will I be able to license copyrights, software or unpatented technology under this license?
:   No. Under this license you are able to license only patented technology. A non-exclusive license to tangible research property and technical information is also included in the Quick Start License to the extent that such a license is needed to practice the licensed patent rights.

14. Why are the non-financial and financial diligence requirements important?
:   The diligence requirements are critical checkpoints that ensure that the WashU startup is working diligently towards commercializing the licensed technology. This metric can also be used to track and monitor the progress of the licensee throughout the term of the agreement. This licensing consideration is of paramount importance to the university.

15. What is a Success Fee?
:   Success Fee means the rate that will be used to calculate the amount that Licensee shall pay to Washington University upon a liquidation event or Initial Public Offering (IPO). The success fee rate for the Quick Start License is 0.95%. Please note that this provision shall survive the termination or expiration following the 5 year anniversary of the Quick Start License.

16. What other approvals are required for the Quick Start License?
:   OTM will confirm that appropriate conflict of interest approvals are obtained prior to the execution of the Quick Start License. If the company is located outside of the United States, OTM may need to obtain an export control waiver.

17. Are there scenarios where a quick start license would not be appropriate to use with an otherwise qualifying start-up company?
:   Yes. In addition to meeting the described criteria for a quick start license, examples where the terms of a quick start license would not be appropriate may include license requests that involve  
    (a) a patent application that has been filed as a non-provisional, PCT, or foreign filing;  
    (b) multiple patent estates that could give rise to distinct product families;  
    (c) 2 or more distinct patent families;  
    (d) jointly owned intellectual property.

---

# Forms
Source: https://otm.wustl.edu/forms/
Scraped: 2026-09-03

## Effective March 1, 2019, all invention/material disclosures and requests for Material Transfer Agreements will be processed online.  [>> otminnovate.wustl.edu](https://otminnovate.wustl.edu/log_in/) (use WUSTL Key to log in.)

## Invention & Licensing

Online forms:  [>> otminnovate.wustl.edu](https://otminnovate.wustl.edu/log_in/) (use WUSTL Key to log in.)

## Material Transfer Agreements

- For sending WashU materials to academic and industry collaborators   [>> Outgoing MTA Intake Form via Innovate IP](https://otminnovate.wustl.edu/log_in/)
- For receiving materials from an academic / non-profit institution / industry   [>> Incoming MTA Intake Form via InnovateIP](https://otminnovate.wustl.edu/log_in/)

## InnovateIP

InnovateIP eliminates the need to manually complete paper-forms, but also allows users to track status online  [>> otminnovate.wustl.edu](https://otminnovate.wustl.edu/)

- Choose red button titled “WUSTL Users Click Here.”
- Enter WUSTL Key and password.
- Click on the tab labeled ‘forms’ which is just below the InnovateIP logo.
- Click the red ‘Fill Out New Form’ button.
- Choose between “Disclosure Form”, “MTA In Request Form”, or ‘MTA Out Request Form’.
- The user will then be asked to enter the requisite information in an online form.
- If you are unable to complete the form, click the save button at the bottom of the page and InnovateIP will retain the form to be completed later.
- Once all the information is entered, click the ‘submit’ button at the bottom of the page. If any of the information was entered incorrectly, the form will highlight those questions that require additional information.
- Once submitted, OTM will review the form and will follow-up.

Questions? Email [otm@wustl.edu](mailto:otm@wustl.edu)

For certain basic research tools, you can use the WashU Quick MTA to send non-human materials without any OTM involvement (see page two of the Quick MTA for qualifications, instructions)  [>> Quick MTA Form (.pdf)](https://otm.wustl.edu/files/2018/06/WUSTL-Quick-MTA-V4.27.09-fillable-form-14ma880.pdf)

---

# Domain Expert Program
Source: https://otm.wustl.edu/items/domain-expert-program/
Scraped: 2026-09-03

The Domain Expert Program (DEP) was developed in 2021 by the Office of Technology Management to help de-risk early stage WashU technologies and spur innovation in the St. Louis ecosystem.

DEP’s key objectives include:

- Provide actionable, “just-in-time” guidance by an advisory board to mitigate early-stage technology risk.
- Enhance market connectivity and foster an innovation mindset.
- Elevate WashU’s brand in the innovation ecosystem.

Since DEP’s inception, robust partnering opportunities have developed between advisory board members and labs, enhancing the technology transfer process at WashU.

Participating WashU researchers receive guidance from curated, industry-specific domain experts in areas such as:

- Regulatory considerations
- Feasibility studies
- Building market connectivity
- Asset development planning
- Building collaboration opportunities with accelerators, incubators and industry partners
- Access to management talent and business acumen

## DEP Process

The Domain Expert Program convenes periodically with a pre-selected cohort of WashU technologies within a specific vertical market. The Office of Technology Management assembles an expert advisory board customized to that vertical market. The program consists of pitch presentations delivered by each participating PI to the advisory board. Each PI then receives custom guidance and actionable de-risking steps followed by connections to resources and ongoing progress feedback.

## Advisory Board

The DEP advisory board of experts includes venture capitalists, entrepreneurs, accelerator partners, industry representatives, etc. who volunteer their time to help assess the commercialization potential of WashU technologies by providing strategic guidance on participating principal investigator technologies.

## DEP Verticals

Currently, OTM offers the Domain Expert Program in vertical markets including therapeutics, medtech and diagnostics.

## Latest News

The Office of Technology Management (OTM) hosted a Domain Expert Program (DEP) panel on November 21, 2024 geared to the MedTech vertical market. Three pitches by WashU innovators were evaluated by DEP Advisory Board members, consisting of experts in the MedTech space. The participating researchers received customized feedback on their pitches and will use that […]

## Contact

For more information about the Domain Expert Program, contact:

###### DeP Operations Lead

[## C. Frank Hardin, PhD](https://otm.wustl.edu/people/c-frank-hardin/)

Licensing Associate

- [314-747-1794](tel:314-747-1794)
- [clyde@**nospam.**wustl.edu](mailto:%63lyde%40wus%74l.edu)

- [LinkedIn](https://www.linkedin.com/in/frankhardin/)

###### DEP Therapeutics Lead

[## Jennifer Richards, PhD](https://otm.wustl.edu/people/jennifer-richards/)

Business Development Associate

- [314-747-1794](tel:314-747-1794)
- [richards.j@**nospam.**wustl.edu](mailto:r%69c%68a%72d%73.j%40wus%74l.edu)

- [LinkedIn](https://www.linkedin.com/in/jennifer-richards-ph-d-5633a775/)

###### DEP Medtech and therapeutics Lead

[## Leena Prabhu, PhD, MBA](https://otm.wustl.edu/people/leena-prabhu/)

Director of Business Development and Licensing

- [314-747-1906](tel:314-747-1906)
- [l.prabhu@**nospam.**wustl.edu](mailto:l.pr%61%62hu@%77%75st%6c.e%64%75)

- [LinkedIn](https://www.linkedin.com/in/leena-prabhu-381126b8/)

###### DEP Medtech lead

[## Craig Weilbaecher, PhD](https://otm.wustl.edu/people/craig-weilbaecher/)

Business Development Director

- [314-747-0685](tel:314-747-0685)
- [cweilbaecher@**nospam.**wustl.edu](mailto:%63%77%65%69lbaec%68er@wu%73tl%2ee%64u)

- [LinkedIn](https://www.linkedin.com/in/craigweilbaecher/)

### *Related*
