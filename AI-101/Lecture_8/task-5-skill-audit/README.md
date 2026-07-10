# Task 5 — Audit a Skill Before Trusting It

**Skill audited:** `skill-creator` (official Anthropic skill, from the official skills set)
**How I audited it:** read the full skill folder — `SKILL.md`, the 3 agent prompts, the
`references/`, and **every Python script** — and scanned for network calls, credential
handling, and process execution. This is a code-level audit, not just a description read.

---

## 1. What the skill does (plain English)

`skill-creator` is a skill for **building and improving other skills**. It walks you
through: describe the skill you want → draft a `SKILL.md` → generate test prompts → run
them → view the results in a local dashboard → refine → optionally optimise the skill's
`description` so it triggers more reliably. It's a "workbench" for authoring skills.

To do that it ships some helper tooling:
- Python scripts (`scripts/`, `eval-viewer/`) that run test prompts, aggregate the
  results, and generate a report.
- A small **local** web viewer to eyeball eval results.
- Three sub-agent prompt files (analyzer / comparator / grader) used to score outputs.

## 2. What it touches (the sensitive-behaviour check)

| Question | Finding |
|---|---|
| **Contacts an external server / sends your data anywhere?** | **No outbound data.** No `requests`, `urllib`, `socket`, `http.client`, `boto3`, or SDK imports anywhere in the scripts. Nothing uploads your prompts, skills, or results. |
| **Handles credentials / secrets?** | **None.** No API keys, tokens, passwords, or secrets are read, stored, or transmitted. (Zero matches for `api_key`/`token`/`password`/`secret` in any code path.) |
| **Runs commands / executes code?** | **Yes, but locally and transparently.** `subprocess` is used to (a) run `lsof` to free a local port, and (b) spawn the local `claude` CLI to run your eval prompts. It also writes command files into your project's `.claude/commands/`. No `os.system`, no `eval()`/`exec()` on untrusted input. |
| **Opens a network service?** | **Localhost only.** The eval viewer binds to `127.0.0.1` (`http://localhost:<port>`) — not exposed to the network. |
| **The one external contact** | The **optional** eval-viewer HTML pages reference Google Fonts (`fonts.googleapis.com`) and the SheetJS library via CDN (`cdn.sheetjs.com`, pinned with an SRI integrity hash). These load **static assets** (fonts, a spreadsheet-parsing JS lib) **only if you open the viewer in a browser**. They fetch code/fonts *in*; they do **not** send your data *out*. |

## 3. Verdict — is it safe to enable?

**Yes — safe to enable.** For its core job (authoring and evaluating skills) it is
effectively self-contained: local Python stdlib scripts, a localhost-only viewer, and the
local `claude` CLI. It never asks for credentials and never transmits your content to a
third party.

**Two honest caveats a careful user should know:**
1. It **executes local processes** (spawns `claude -p`, runs `lsof`, kills processes on a
   port, writes files into `.claude/`). That's expected for a dev tool, but it means it is
   *not* a passive text skill — run it in a project where you're comfortable with it
   creating command files and spawning the CLI.
2. If you use the **optional browser viewer**, it will pull fonts + one JS library from
   public CDNs. If you need zero external requests, generate the **static** viewer and/or
   review offline; nothing about the core workflow requires those CDN calls.

## 4. Why I trust my own assessment

I didn't rely on the skill's self-description — I read the code and confirmed each claim:
- Searched all scripts for outbound-network imports → **none**.
- Searched for credential handling → **none**.
- Traced every `subprocess` call → all **local** (`lsof`, local `claude` CLI, local HTTP
  server on `127.0.0.1`).
- Located the only external references (CDN fonts + SheetJS) and confirmed they are
  inbound static assets in an **optional** viewer, not data exfiltration.

That is exactly the habit this task is meant to build: **you can state what a skill does,
what it touches, and whether to trust it — grounded in evidence, not vibes.**
