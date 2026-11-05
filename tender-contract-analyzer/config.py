import os
from dotenv import load_dotenv

load_dotenv()

# -----------------------------
# Project Information
# -----------------------------
APP_NAME = "Tender & Government Contract Analyzer"

# -----------------------------
# Upload Settings
# -----------------------------
UPLOAD_FOLDER = "uploads"

ALLOWED_EXTENSIONS = [
    ".pdf",
    ".docx",
    ".png",
    ".jpg",
    ".jpeg"
]

# -----------------------------
# OCR Configuration
# -----------------------------
# Windows Example:
# TESSERACT_PATH = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Linux:
# TESSERACT_PATH = "/usr/bin/tesseract"

# Set TESSERACT_PATH in your .env file, or leave blank if Tesseract is already on PATH.
TESSERACT_PATH = os.getenv("TESSERACT_PATH", "")
# -----------------------------
# Gemini API
# -----------------------------
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# -----------------------------
# Summary Settings
# -----------------------------
MAX_SUMMARY_LENGTH = 300

# -----------------------------
# Question Answering
# -----------------------------
QA_MODEL = "gemini-2.5-flash"

# -----------------------------
# Extraction Keywords
# -----------------------------
ELIGIBILITY_KEYWORDS = [
    "turnover",
    "experience",
    "similar project",
    "gst",
    "pan",
    "certificate",
    "registration",
    "qualification",
    "iso"
]

FINANCIAL_KEYWORDS = [
    "emd",
    "earnest money deposit",
    "tender fee",
    "security deposit",
    "performance guarantee"
]

DATE_KEYWORDS = [
    "publish date",
    "pre-bid",
    "last date",
    "bid submission",
    "technical bid",
    "financial bid"
]

COMPLIANCE_KEYWORDS = [
    "gst certificate",
    "pan card",
    "company registration",
    "audited financial statement",
    "bank solvency",
    "work order",
    "experience certificate"
]

# -----------------------------
# Create Upload Folder
# -----------------------------
os.makedirs(UPLOAD_FOLDER, exist_ok=True)