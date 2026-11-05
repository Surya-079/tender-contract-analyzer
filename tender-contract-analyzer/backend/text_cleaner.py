import re


def clean_text(text: str) -> str:
    """
    Clean and normalize extracted text from
    PDF, DOCX and OCR sources.

    Args:
        text (str): Raw extracted text.

    Returns:
        str: Cleaned text.
    """

    if not text:
        return ""

    # Replace tabs with spaces
    text = text.replace("\t", " ")

    # Replace multiple spaces with a single space
    text = re.sub(r"[ ]{2,}", " ", text)

    # Remove multiple blank lines
    text = re.sub(r"\n{2,}", "\n", text)

    # Remove unwanted special characters
    text = re.sub(r"[^\x20-\x7E\n₹]", "", text)

    # Remove spaces before punctuation
    text = re.sub(r"\s+([.,;:!?])", r"\1", text)

    # Remove spaces after opening brackets
    text = re.sub(r"([\(\[\{])\s+", r"\1", text)

    # Remove spaces before closing brackets
    text = re.sub(r"\s+([\)\]\}])", r"\1", text)

    return text.strip()