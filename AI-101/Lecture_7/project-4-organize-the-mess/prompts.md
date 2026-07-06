# Prompts used — Organize the Mess

The whole point here is **safety**, so my prompts demanded it explicitly.

## Initial prompt (with the brief)

> I have a messy folder. Write me a Python script that tells me what's in it:
> find true duplicate files (same contents, not just same name), flag very large
> files, and group everything by type (Images, Documents, Audio, Archives, Code,
> Installers, Other).

## Improved prompt 1 — DEMAND a dry run (the safety rule)

> Important: this touches my real files, so it must be safe. Show me the FULL
> plan first — every file, which folder it would go to, which are duplicates,
> which are large — and by default DO NOT move, rename, or delete anything.
> Only do something when I pass an explicit --execute flag.

## Improved prompt 2 — copy, never destroy

> When I do run --execute, it must COPY the files into a brand-new
> `organized_output/` folder grouped by type. It must never move, overwrite, or
> delete the originals. Duplicates should only be REPORTED — I will decide what
> to delete, not the script.

## Improved prompt 3 — prove duplicates are real

> Detect duplicates by hashing file contents with SHA-256, not by filename, so
> I can trust that two files flagged as identical really are byte-for-byte the
> same. Show how much space I'd reclaim if I deleted the redundant copies.

## Verification prompt

> After --execute, I want to confirm safety: my original folder should still
> have all 19 files, and the output folder should have 19 copies. I planted
> exactly 3 duplicate pairs and 1 large file — if the script reports exactly
> those, I'll trust it on my real Downloads folder.
