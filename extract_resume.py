from pdfminer.high_level import extract_text

src = "Khoa Resume 2025.docx (1).pdf"
out = "Khoa-Nguyen-Resume-2025-extracted.txt"
text = extract_text(src)
with open(out, "w", encoding="utf-8") as f:
    f.write(text)
print(f"Wrote extracted text to {out}")
