"""
Creates a synthetic 'messy folder' to demo the organizer safely.
Re-run any time to regenerate identical sample data.
Two pairs of files share identical bytes (true duplicates); one file is large.
"""
import os

BASE = os.path.join(os.path.dirname(__file__), "sample_messy_folder")
os.makedirs(BASE, exist_ok=True)

def write(name, content, times=1):
    with open(os.path.join(BASE, name), "w", encoding="utf-8") as f:
        f.write(content * times)

# --- documents (with a true duplicate pair) ---
resume = "SADDAM HUSSAIN — Resume\nElectrical Engineer, ISMO Jamshoro\n" * 40
write("resume_final.pdf", resume)
write("resume_final_v2.pdf", resume)                      # DUPLICATE of resume_final.pdf

assignment = "AI-101 Assignment 1: Prompt Engineering\nAnswer: ...\n" * 30
write("assignment1.docx", assignment)
write("assignment1 - Copy.docx", assignment)             # DUPLICATE of assignment1.docx

write("fee_challan_spring2026.pdf", "HBL Fee Challan\nAmount: PKR 45000\n" * 10)
write("k_electric_bill_may.pdf", "K-Electric Bill\nUnits: 640\nAmount: PKR 11380\n" * 10)
write("notes_meeting.txt", "Grid Code meeting notes\n- follow up NEPRA clause 4.2\n" * 8)
write("budget_2026.xlsx", "Month,Spend\nMay,44646\nApr,44965\n" * 12)

# --- images (screenshots + a duplicate photo via the "(1)" pattern) ---
photo = "JPEGDATA" * 200
write("IMG_20260501_123456.jpg", photo)
write("IMG_20260501_123456 (1).jpg", photo)              # DUPLICATE (downloaded twice)
write("Screenshot_2026-05-02_office.png", "PNGDATA" * 150)
write("Screenshot_2026-05-10_grades.png", "PNGDATA" * 160)
write("whatsapp_image_eid.jpg", "JPEGDATA2" * 120)

# --- media / archive / code / installer ---
write("nusrat_qawwali.mp3", "MP3DATA" * 300)
write("daraz_invoice.zip", "ZIPDATA" * 100)
write("old_scraper.py", "import requests\n# half-finished project\n" * 20)
write("setup_installer.exe", "X" * 160_000)              # LARGE FILE (~156 KB)

# --- forgotten / ambiguous ---
write("download.tmp", "temporary junk\n" * 5)
write("Untitled document.txt", "half-finished idea about a study app\n" * 6)

print(f"Created {len(os.listdir(BASE))} files in {BASE}")
