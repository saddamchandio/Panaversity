"""
Organize the Mess — safely find out what's actually in your folder.
Panaversity AI-101 · Lecture 7 · Project 4

SAFETY FIRST. This is the only project that touches real files, so it is built
around the safe order taught in the lecture:
  * DRY RUN BY DEFAULT — it shows a full plan and touches NOTHING.
  * It never deletes or overwrites. On --execute it COPIES into a NEW folder,
    leaving every original exactly where it was.
  * Duplicates are only REPORTED (same contents, verified by SHA-256), never
    auto-deleted — you decide.

WHAT "CLEAN" MEANS FOR ME (the brief):
  1. Find true duplicates (identical contents), so I can reclaim space.
  2. Flag very large files (over the threshold).
  3. Group everything by type into tidy subfolders.

Usage:
  python organize.py sample_messy_folder                 # DRY RUN (default, safe)
  python organize.py sample_messy_folder --execute       # copy into organized_output/
"""

import hashlib
import os
import shutil
import sys

LARGE_FILE_KB = 100  # flag anything bigger than this

TYPE_MAP = {
    "Images":     {".jpg", ".jpeg", ".png", ".gif", ".webp", ".heic"},
    "Documents":  {".pdf", ".doc", ".docx", ".txt", ".xlsx", ".csv", ".pptx"},
    "Audio":      {".mp3", ".wav", ".m4a", ".aac"},
    "Video":      {".mp4", ".mov", ".mkv", ".avi"},
    "Archives":   {".zip", ".rar", ".7z", ".tar", ".gz"},
    "Code":       {".py", ".js", ".java", ".cpp", ".c", ".html", ".css"},
    "Installers": {".exe", ".msi", ".dmg", ".apk"},
}


def category(ext):
    for cat, exts in TYPE_MAP.items():
        if ext.lower() in exts:
            return cat
    return "Other"


def sha256(path, buf=65536):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        while chunk := f.read(buf):
            h.update(chunk)
    return h.hexdigest()


def scan(folder):
    files = []
    for name in sorted(os.listdir(folder)):
        p = os.path.join(folder, name)
        if os.path.isfile(p):
            ext = os.path.splitext(name)[1]
            files.append({
                "name": name, "path": p, "ext": ext,
                "size": os.path.getsize(p),
                "cat": category(ext),
                "hash": sha256(p),
            })
    return files


def main():
    if len(sys.argv) < 2:
        print("Usage: python organize.py <folder> [--execute]")
        return
    folder = sys.argv[1]
    execute = "--execute" in sys.argv
    files = scan(folder)

    # --- duplicates: group by hash ---
    by_hash = {}
    for f in files:
        by_hash.setdefault(f["hash"], []).append(f)
    dup_groups = [g for g in by_hash.values() if len(g) > 1]

    # --- large files ---
    large = [f for f in files if f["size"] > LARGE_FILE_KB * 1024]

    mode = "EXECUTE (copying to new folder)" if execute else "DRY RUN (nothing will be touched)"
    print("=" * 62)
    print(f" ORGANIZE THE MESS   —   {mode}")
    print("=" * 62)
    print(f" Source folder : {folder}")
    print(f" Files scanned : {len(files)}")
    total_mb = sum(f['size'] for f in files) / 1024
    print(f" Total size    : {total_mb:,.1f} KB\n")

    # --- planned grouping ---
    print("-" * 62)
    print(" PLAN — files grouped by type (would be COPIED, originals kept)")
    print("-" * 62)
    plan = {}
    for f in files:
        plan.setdefault(f["cat"], []).append(f["name"])
    for cat in sorted(plan):
        print(f"   {cat}/  ({len(plan[cat])})")
        for n in plan[cat]:
            print(f"       {n}")

    # --- duplicate report ---
    print("\n" + "-" * 62)
    print(f" DUPLICATE FILES  ({len(dup_groups)} group(s), same contents verified by SHA-256)")
    print("-" * 62)
    reclaim = 0
    for g in dup_groups:
        keep = g[0]["name"]
        print(f"   identical  ({g[0]['size']} bytes):")
        for f in g:
            tag = "  [keep]" if f["name"] == keep else "  [redundant copy]"
            print(f"       {f['name']}{tag}")
        reclaim += sum(f["size"] for f in g[1:])
    print(f"   {'-'*44}")
    print(f"   Reclaimable if you delete the redundant copies: {reclaim} bytes")

    # --- large files ---
    print("\n" + "-" * 62)
    print(f" LARGE FILES  (> {LARGE_FILE_KB} KB)")
    print("-" * 62)
    for f in sorted(large, key=lambda x: -x["size"]):
        print(f"   {f['size']/1024:8,.1f} KB   {f['name']}")
    if not large:
        print("   (none)")

    # --- execute ---
    if execute:
        out = os.path.join(os.path.dirname(folder.rstrip("/\\")) or ".", "organized_output")
        os.makedirs(out, exist_ok=True)
        copied = 0
        for f in files:
            dest_dir = os.path.join(out, f["cat"])
            os.makedirs(dest_dir, exist_ok=True)
            shutil.copy2(f["path"], os.path.join(dest_dir, f["name"]))  # COPY, never move
            copied += 1
        # write a plan file too
        with open(os.path.join(out, "_duplicates_report.txt"), "w", encoding="utf-8") as r:
            for g in dup_groups:
                r.write("IDENTICAL: " + ", ".join(f["name"] for f in g) + "\n")
        print("\n" + "=" * 62)
        print(f" DONE — copied {copied} files into '{out}/' (grouped by type).")
        print(" Your original folder was NOT modified.")
        print("=" * 62)
    else:
        print("\n" + "=" * 62)
        print(" This was a DRY RUN. No file was moved, copied, renamed, or deleted.")
        print(" Re-run with  --execute  to copy into a new 'organized_output/' folder.")
        print("=" * 62)


if __name__ == "__main__":
    main()
