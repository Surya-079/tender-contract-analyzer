import re


DOCUMENT_PATTERNS = {
    "GST Certificate": [
        r"\bgst\b",
        r"gst certificate",
        r"gst registration"
    ],

    "PAN Card": [
        r"\bpan\b",
        r"pan card"
    ],

    "Company Registration Certificate": [
        r"company registration",
        r"certificate of incorporation",
        r"incorporation certificate"
    ],

    "Previous Work Orders": [
        r"work order",
        r"previous work",
        r"completed project",
        r"similar project"
    ],

    "Audited Financial Statements": [
        r"audited financial",
        r"balance sheet",
        r"profit and loss",
        r"financial statement"
    ],

    "Bank Solvency Certificate": [
        r"bank solvency",
        r"solvency certificate"
    ],

    "ISO Certificate": [
        r"iso[- ]?\d+",
        r"iso certification"
    ],

    "Experience Certificate": [
        r"experience certificate",
        r"experience"
    ],

    "MSME Certificate": [
        r"\bmsme\b"
    ],

    "Income Tax Return": [
        r"income tax return",
        r"\bitr\b"
    ],

    "Power of Attorney": [
        r"power of attorney"
    ],

    "Affidavit": [
        r"affidavit"
    ],

    "Digital Signature Certificate": [
        r"digital signature",
        r"\bdsc\b"
    ]
}


def generate_checklist(text: str) -> list:
    """
    Generate compliance checklist from tender text.

    Args:
        text (str): Tender document text.

    Returns:
        list: Required documents.
    """

    checklist = []

    lower_text = text.lower()

    for document, patterns in DOCUMENT_PATTERNS.items():

        for pattern in patterns:

            if re.search(pattern, lower_text, re.IGNORECASE):
                checklist.append(document)
                break

    return sorted(list(set(checklist)))