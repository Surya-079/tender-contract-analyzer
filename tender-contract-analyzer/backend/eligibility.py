import re


def search_pattern(pattern, text):
    """
    Search a regex pattern and return the first match.
    """
    match = re.search(pattern, text, re.IGNORECASE)

    if match:
        return match.group(1).strip()

    return "Not Found"


def extract_eligibility(text: str) -> dict:
    """
    Extract eligibility criteria from tender text.

    Returns:
        Dictionary containing extracted eligibility information.
    """

    eligibility = {}

    # -------------------------
    # Minimum Turnover
    # -------------------------
    turnover_pattern = (
        r"(?:minimum\s+turnover|annual\s+turnover|turnover)"
        r".{0,40}?(₹\s?[\d,]+(?:\.\d+)?\s*(?:crore|lakh)?)"
    )

    eligibility["Minimum Turnover"] = search_pattern(
        turnover_pattern,
        text
    )

    # -------------------------
    # Experience
    # -------------------------
    experience_pattern = (
        r"(\d+\s+years?\s+of\s+experience)"
    )

    eligibility["Experience"] = search_pattern(
        experience_pattern,
        text
    )

    # -------------------------
    # Similar Projects
    # -------------------------
    similar_project_pattern = (
        r"(\d+\s+similar\s+projects?)"
    )

    eligibility["Similar Projects"] = search_pattern(
        similar_project_pattern,
        text
    )

    # -------------------------
    # GST
    # -------------------------
    eligibility["GST Required"] = (
        "Yes"
        if re.search(r"\bgst\b", text, re.IGNORECASE)
        else "No"
    )

    # -------------------------
    # PAN
    # -------------------------
    eligibility["PAN Required"] = (
        "Yes"
        if re.search(r"\bpan\b", text, re.IGNORECASE)
        else "No"
    )

    # -------------------------
    # ISO Certification
    # -------------------------
    iso_match = re.search(
        r"(ISO[- ]?\d+)",
        text,
        re.IGNORECASE
    )

    if iso_match:
        eligibility["ISO Certification"] = iso_match.group(1)
    else:
        eligibility["ISO Certification"] = "Not Required"

    # -------------------------
    # MSME
    # -------------------------
    eligibility["MSME Eligible"] = (
        "Yes"
        if re.search(r"\bmsme\b", text, re.IGNORECASE)
        else "No"
    )

    # -------------------------
    # Startup
    # -------------------------
    eligibility["Startup Eligible"] = (
        "Yes"
        if re.search(r"\bstartup\b", text, re.IGNORECASE)
        else "No"
    )

    # -------------------------
    # Technical Qualification
    # -------------------------
    technical_keywords = [
        "b.e",
        "b.tech",
        "engineering",
        "diploma",
        "qualification",
        "technical"
    ]

    eligibility["Technical Qualification"] = "Not Mentioned"

    for keyword in technical_keywords:

        if keyword.lower() in text.lower():
            eligibility["Technical Qualification"] = "Required"
            break

    return eligibility