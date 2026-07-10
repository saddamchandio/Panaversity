---
name: my-official-style
description: "Draft official correspondence in Saddam Hussain's exact ISMO house style — outgoing letters, reminders, technical/Grid-Code rebuttals, point-by-point tabular replies, appreciation letters, office orders, notices, forwarding/submission notes, POL statements, To-Whom-It-May-Concern certificates, and internal noting sheets, as paste-ready text. This skill is triggered ONLY when the user explicitly invokes it with the slash command `/my-official-style` (or the short alias `/official`). Do NOT auto-trigger on ordinary requests to write, draft, reply to, or polish a letter or any correspondence — not even when phrased as 'in my style', 'official style', or 'the usual format', and not even for ISMO / RCC(S) Jamshoro letterhead. Wait for the explicit slash command. When invoked, read SKILL.md and the relevant reference file, then follow the workflow."
---

# my-official-style

Drafts official correspondence in the precise register and layout used by Saddam Hussain at ISMO — RCC(S) Jamshoro. The goal is output that is indistinguishable from his own hand: same skeleton, same courtesy idioms, same escalation pattern, same distribution conventions.

> **Invocation:** this skill runs **only** on the explicit slash command `/my-official-style` (or `/official`). It must not be applied to ordinary correspondence requests that don't carry the command. Everything below takes effect once the command is given.

## What this skill produces

**Paste-ready text only.** Lay the correspondence out exactly as it appears in his documents so he can paste it straight into the ISMO letterhead in Word. Do **not** generate a `.docx`, a header logo, or a footer image unless he explicitly asks for a Word file — the letterhead and footer are pre-printed; the skill fills the body between them. Show the reference/date header and the contact footer only when he asks for the full page; otherwise start from the addressee block.

Render bold on the elements that are conventionally bold (addressee, subject + subject-descriptor, closing line, signature block, CC annotations) so he can see the intended styling. If he says he is pasting into Word and the asterisks get in the way, offer a clean no-markdown version.

## Hard rules

- **Never invent facts.** Reference numbers, letter numbers, dates, cheque numbers, amounts, NTN, clause numbers and **quoted Grid Code text** must come from the user or from material in the conversation. Where a required detail is missing, insert a clearly bracketed placeholder like `[letter no. ____]`, `[Dated: __.__.____]`, `[Clause __ — verify text]` and list what you need. Fabricating a clause citation or a reference is the worst failure this skill can make.
- **No AI/Claude attribution anywhere** in the output. These are his official letters.
- **Decide the signer per letter.** Establish who signs before producing the signature block (see "Signing designations"). If it isn't clear from the request or the subject matter, ask in one line.
- **Match register to genre, not to mood.** Routine requests stay deferential; reminders firm up; rebuttals are pointed and clause-backed but never discourteous on the surface.

## Workflow

1. **Identify the genre** (see selector below) and the **signer**.
2. **Gather the variables** — addressee(s), subject, reference chain, the substantive facts/ask, urgency marker, enclosures, CC list. Infer everything you reasonably can from the request; ask only for genuinely missing essentials, consolidated into a single short question.
3. **Read the matching reference file** for the genre's template and worked example before drafting:
   - `references/letters.md` — request, reminder, forwarding/submission, billing/NTN, appreciation, certificate
   - `references/disputes.md` — technical/Grid-Code rebuttal and point-by-point tabular reply
   - `references/internal.md` — office order, notice, POL statement, noting sheet
4. **Draft** using the shared conventions plus the genre template.
5. **Flag placeholders** at the end so he can fill verified specifics.

## Genre selector

| If the user wants to… | Genre | Reference |
|---|---|---|
| Ask another office to do / provide / complete something | Request letter | letters.md |
| Chase a pending request | Reminder (REMINDER – I/II) | letters.md |
| Forward an application / case / documents | Forwarding / submission note | letters.md |
| Update billing name / NTN, correct a bill | Billing / administrative letter | letters.md |
| Praise an officer's work | Appreciation letter | letters.md |
| Certify a fact about an officer | To Whom It May Concern | letters.md |
| Push back on a flawed/incorrect position, cite Grid Code | Technical rebuttal | disputes.md |
| Answer a list of queries/allegations one by one | Point-by-point tabular reply | disputes.md |
| Order a transfer/posting/internal arrangement | Office Order | internal.md |
| Inform employees of a rule/arrangement | Notice | internal.md |
| Report monthly DG-set fuel use | POL statement | internal.md |
| Put a case up the internal chain for approval | Noting sheet | internal.md |

## Shared conventions (apply to every genre)

### Reference + date header (only when full page requested)
```
ISMO/<YEAR>/ED(SO)/SD(SNVRE)/<serial range>            <Mon> <DDth>, <YYYY>
```
- Reference stem is fixed: `ISMO/<YEAR>/ED(SO)/SD(SNVRE)/`; append the dispatch serial range (e.g. `3187-94`) only if known, else leave the trailing slash.
- Date format carries an ordinal suffix and an abbreviated or full month: `Jan 23rd, 2026`, `May 30th, 2025`, `March 04th, 2026`. (His own files occasionally slip — `Feb 11st`, `June 17nd` — always use the correct ordinal: 1st, 2nd, 3rd, 11th, 21st, 22nd, 23rd.)

### Addressee block (bold)
Designation on the first line, office/location beneath. Place any urgency marker right-aligned on the first line: `Most Urgent`, `Matter Most Urgent`, `REMINDER – I`. Multiple addressees are stacked (and can be laid out in two columns for joint letters).

### Subject line
`Subject:  <Title Case Subject>` — label and title both bold. Where a standing project is involved, repeat its full descriptor as a bold sub-line beneath the subject (e.g. the recurring *"New Connection of 750KW under Tariff C-2 in favor of … on Cost Deposit Basis"* block). A leading genre tag is common: `Subject: Reminder: …`, `Subject: Reply: …`, `Subject: Approval of Shutdown: …`.

### Reference block
```
Ref:    i.  <This office | Your good office | <Office>> letter no. <no.>          Dated: DD.MM.YYYY
       ii.  <…>                                                                    Dated: DD.MM.YYYY
```
Roman numerals; each line ends with a right-aligned `Dated: DD.MM.YYYY` (note the `.` separators). Use `(addressed to your good office, copy to this office)` and similar parentheticals where they apply. Body then refers back as `at Sr.No.(i)`, `at Sr.No.(iii)`.

### Body — voice and openers
Institutional third person throughout: **"this office," "the undersigned"** — never "I" in routine letters (first person is reserved for appreciation letters and, as "we," for set-piece technical letters). Address the recipient as **"your good office," "your good self," "your kind control."** Standard openers:
- `In this context it is apprised that …`
- `It is apprised that …` / `Please be apprised that …` / `It is intimated that …` / `It is submitted that …`
- `Reference is made to …`
- `In continuation of above referred letter at Sr.No.(i), …`
- `In the light of above referred letter …` / `With reference to the above-cited correspondence, particularly your letter at Sr. No. (ii), …`
- `Enclosed please find herewith …` (forwarding)
- `In compliance of Clause (X) of D.N. …`

### Body — requests and courtesy
Jussive politeness via **"may please be," "may kindly be"**: *"the relevant staff may please be advised…," "the remaining work may kindly be expedited."* Escalators: *"it is therefore requested that," "it is once again requested," "it is humbly requested that:," "you are hereby requested to:."* Pertinence flags: *"It is pertinent to mention/emphasize that," "It is further highlighted that."* Liability hedge where due: *"for which this office shall not be held responsible."* National-interest framing when stakes are high: *"in the best interest of the Nation," "in the greater National Interest."* Use `&` freely; abbreviate offices (`CE`, `XEN`, `SE`, `DM`, `GM`, `o/o`, `w.e.f.`).

### Closing line (bold, its own line)
Pick by tone:
- Routine: `Your kind cooperation in this regard shall be highly appreciated.`
- Critical: `Your kind cooperation in this critical matter shall be highly appreciated.`
- Push: `Your prompt action in this regard shall be highly appreciated.`
- Personal escalation: `Your kind personal attention in this regard shall be highly appreciated.` / `Your personal intervention to accomplish the above on urgent basis shall be highly appreciated.`
- Submission: `Submitted for your kind consideration, please.`
- Information only: `This is for your kind information, please.`
- Forwarding: `For your kind information and necessary action, please.`

### Enclosures
`D/A:` or `D.A:` (Description of Attachments), then `a. … b. … c. …` or `D/A: as above.` Use `P.T.O.` if content runs past the page before the signature.

### Signature block (bold)
Designation (1–2 lines) then office:
```
Senior Director
(Southern Network & VRE Operations)
ISMO – RCC(S) Jamshoro
```

### CC / distribution (bold "CC", dash list)
Each entry ends with a full stop. Append bold action tags where relevant: **For your kind information & necessary action, please.** / **With similar request, please.** / **For needful action, please.** / **For strict compliance, please.** / **For your kind information, please.** The list **always ends with** `Master File.`

### Contact footer (only when full page requested)
```
+92 22 2021052   |   www.ismo.gov.pk
Registered Office: ISMO – RCC(S) Building, Dadu-Sehwan Road, Jamshoro
```

## Signing designations (pick per letter)
- **Senior Director / (Southern Network & VRE Operations) / ISMO – RCC(S) Jamshoro** — default for outward operational and HESCO/NGC correspondence.
- **Director RCC (South Operations) / ISMO – RCC(S) Jamshoro** — operational/technical directives within the network.
- **Deputy Director (E&M, Transport) / ISMO – RCC(S) Jamshoro** — transport, E&M, POL, vendor/contractor execution matters.
- **Deputy Director (Civil) / ISMO, Islamabad** — civil works / material-inspection matters routed from Islamabad.
- **Deputy Director (Tech) / ISMO – RCC(S) Jamshoro** — technical/VRE matters where Saddam signs in his own designation.
- **Executive Director (System Operations) / ISMO, Islamabad** — when escalated to ED level.

If the genre, addressee, and subject don't make the signer obvious, ask once: *"Who's signing — Senior Director (SN & VRE), Director (South Ops), or DD (Tech)/(E&M)?"*

## Tone calibration across the escalation ladder
1. **First ask** — purely deferential; appreciation of any work already done ("It is highly appreciated that the majority of work has been completed…").
2. **Reminder** — courteous but pointed: name the lapse ("regretfully no progress has been observed so far"), restate the ask "once again," add an urgency marker.
3. **Rebuttal / dispute** — firm, evidence- and clause-led; label incorrect claims plainly ("This claim is **misleading**"); correct the record; still close on cooperation and national interest.

Keep sentences long and predominantly passive, in the South-Asian official register — that cadence is part of the signature. Don't modernise it into crisp business English unless asked.
