Khoa Nguyen — Personal Portfolio

This repository contains a single-page portfolio website and the original resume PDF and extracted text.

Files
- `index.html` — The portfolio page (header, hero, About, Experience, Education, Skills, Contact).
- `Khoa-Nguyen-Resume-2025.pdf` — Resume PDF (downloadable from the site).
- `Khoa-Nguyen-Resume-2025-extracted.txt` — Plain-text extraction of the resume used to populate the About/Experience/Education sections.
- `extract_resume.py` — Small helper script (uses `pdfminer.six`) to extract text from the PDF into the `-extracted.txt` file.

How to view
1. Open `index.html` in your browser (double-click or File → Open).

How to regenerate the extracted text
1. Ensure you have Python available. A virtual environment is included at `.venv` for convenience.
2. Install dependencies (if not already):

   /Users/admin/Desktop/my-portfolio/.venv/bin/python -m pip install -r requirements.txt

   (or install `pdfminer.six` directly)
3. Run the extraction script:

   /Users/admin/Desktop/my-portfolio/.venv/bin/python extract_resume.py

This will overwrite `Khoa-Nguyen-Resume-2025-extracted.txt` with the latest text extracted from the PDF.

Notes
- The site is intentionally simple and self-contained (single `index.html`). Feel free to request additional features like a Projects section, LinkedIn links, or a contact form.
