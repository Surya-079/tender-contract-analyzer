# Tender & Government Contract Analyzer

A Streamlit application that reads tender documents (PDF/DOCX) and automatically extracts the information a bidder needs: eligibility criteria, financial requirements, key dates, a compliance checklist and a risk report. It replaces manual reading of long tender documents with a structured, tab-based dashboard.

## Features

| Tab | What it does |
|---|---|
| **Summary** | Project name, location, estimated value, EMD, tender fee, submission deadline and key eligibility points |
| **Eligibility** | Minimum turnover, experience, similar projects, GST, PAN, ISO, MSME/startup eligibility, technical qualification |
| **Financial** | EMD amount, tender fee, security deposit, estimated tender value |
| **Deadlines** | Publish date, document download start, bid submission start and deadline, pre-bid meeting, bid opening |
| **Compliance** | Checklist of documents the bidder must prepare (GST, PAN, registration, work orders, financial statements, etc.) |
| **Risk** | Flags turnover/experience requirements, mandatory certifications, fees payable and approaching or passed deadlines |

Other features:
- User registration and login with bcrypt-hashed passwords (SQLite)
- Text cleaning pipeline for extracted document text
- OCR module (OpenCV + Tesseract) for scanned images

## Tech Stack

- **Frontend:** Streamlit
- **Backend:** Python (modular `backend/` package)
- **Document parsing:** pdfplumber, python-docx
- **OCR:** OpenCV, Pillow, pytesseract (Tesseract OCR)
- **Extraction:** regular expressions and keyword-context matching
- **Auth and database:** SQLite, bcrypt

## Project Structure

```
├── app.py                # Streamlit app (login + analysis dashboard)
├── config.py             # Settings and keyword lists
├── requirements.txt
├── backend/
│   ├── pdf_reader.py     # PDF text extraction
│   ├── docx_reader.py    # DOCX text extraction
│   ├── ocr_reader.py     # Image OCR with preprocessing
│   ├── text_cleaner.py   # Text normalisation
│   ├── eligibility.py    # Eligibility extraction
│   ├── financial.py      # EMD, fee, deposit extraction
│   ├── deadlines.py      # Date extraction by context
│   ├── compliance.py     # Required-document checklist
│   ├── risk.py           # Risk analysis
│   ├── summary.py        # Tender summary
│   └── auth.py           # Register / login
├── datasets/             # Sample tender document
└── uploads/              # Sample tenders and runtime uploads
```

## Setup

1. Clone the repository
   ```
   git clone https://github.com/S-ry-007/tender-contract-analyzer.git
   cd tender-contract-analyzer
   ```
2. Install dependencies
   ```
   pip install -r requirements.txt
   ```
3. (Only for OCR) Install [Tesseract OCR](https://github.com/tesseract-ocr/tesseract). If it is not on your PATH, copy `.env.example` to `.env` and set `TESSERACT_PATH`.
4. Run the app
   ```
   streamlit run app.py
   ```
5. Register an account, log in and upload a tender PDF or DOCX.

## Limitations and Future Work

- Extraction is rule-based, so accuracy depends on how consistently a tender document is formatted.
- Scanned-image OCR is implemented in the backend but not yet connected to the upload screen.
- Planned: LLM-based question answering over tender text (Gemini), multi-language support and export of results to PDF/Excel.
