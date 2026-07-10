# Task 1 — Captured demo run (skill triggering on command)

**Surface:** Claude Code (proves portability — also used for Task 4)
**Command:** `/my-official-style`
**Genre selected by the skill:** Reminder (REMINDER – I) → `references/letters.md`

## Prompt given (one plain sentence after the command)

> `/my-official-style` Draft a REMINDER – I to the Chief Executive Officer, HESCO
> Hyderabad, chasing the pending energization of the newly constructed 11KV dedicated
> feeder to RCC(S) ISMO Jamshoro. Context: majority of civil/structural work including
> pole erection and stringing has been completed by HESCO field teams; installation of
> span and conductor on the terminal pole at the RCC(S) end remains pending, so final
> interconnection is not yet established; a representative of this office met your good
> self earlier but regretfully no progress has been observed so far. Signer: Senior
> Director (Southern Network & VRE Operations). Reference chain: (i) this office letter,
> (ii) Chief Engineer (P&E) HESCO letter. Mark it Most Urgent. Start from the addressee
> block. Standing project descriptor: New Connection of 750KW under Tariff C-2 …

## Output produced (paste-ready)

**Most Urgent**  ·  **REMINDER – I**

**Chief Executive Officer,**
**HESCO, Hyderabad.**

**Subject:  Reminder: Request for Completion and Energization of Newly Constructed 11KV Feeder to RCC(S) ISMO Jamshoro:**
**New Connection of 750KW under Tariff C-2 in favor of Chief Engineer (Southern Network & VRE Operations) RCC (South) Jamshoro as a Back-Up Supply Through New Independent/Dedicated Feeder having a length of 1.8km to be emanated from 132kV Grid Station Jamshoro (On Cost Deposit Basis).**

Ref:  i.  This office letter no. [____]                     Dated: [__.__.____]
      ii.  Chief Engineer (P&E) HESCO Hyderabad office, letter no. [____]     Dated: [__.__.____]

Reference is made to the above referred correspondence regarding the ongoing work of establishing a dedicated 11KV independent feeder from 132KV HESCO Grid Station Jamshoro to RCC(S) ISMO Jamshoro. It is highly appreciated that the majority of civil and structural work, including erection of poles and stringing, has been completed through the efforts of HESCO field teams. However, it is apprised with regret that the installation of span and conductor on the terminal pole at the RCC(S) end remains pending, due to which the final interconnection is yet to be established.

In continuation of above referred letter at Sr.No.(i), a representative of this office met your good self in this regard; however, regretfully no progress has been observed so far.

It is therefore once again requested that the relevant staff may please be advised for early completion of the remaining span & conductor work at the RCC(S) terminal pole, and that the already completed portion of the 11KV line may kindly be energized provisionally until the remaining works are fully accomplished. This initiative would not only support ISMO in ensuring power readiness and operational continuity, but would also prevent any theft of the installed 11KV equipment, for which this office shall not be held responsible.

In view of the criticality and pendency of the matter, your kind personal attention is solicited for its early resolution.

**Your kind cooperation in this critical matter shall be highly appreciated.**

**Senior Director**
**(Southern Network & VRE Operations)**
**ISMO – RCC(S) Jamshoro**

**CC**
- Chief Engineer (P&E), HESCO, Hyderabad. **With similar request, please.**
- Executive Director (System Operations), ISMO, Islamabad. **For your kind information, please.**
- Master File.

## Verification

- ✅ Fired only on the explicit command; produced the exact house-style skeleton.
- ✅ Correct reminder cadence and closing line for a "critical" escalation.
- ✅ **Anti-fabrication rule held** — unknown reference numbers left as `[____]` placeholders, not invented.
- ✅ CC list terminates in `Master File.` per convention.
