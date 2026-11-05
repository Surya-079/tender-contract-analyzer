import re


def search_amount(pattern: str, text: str) -> str:
    """
    Search for a monetary amount using the given pattern.
    """

    match = re.search(
        pattern,
        text,
        re.IGNORECASE | re.DOTALL
    )

    if match:
        return match.group(1).strip()

    return "Not Found"


def extract_financial_details(text: str) -> dict:
    """
    Extract financial details from tender document.

    Returns:
        Dictionary containing financial information.
    """

    financial = {}

    amount_pattern = (
        r"(₹\s?[\d,]+(?:\.\d+)?(?:\s*(?:Crore|Lakh|Lakhs|Crores))?"
        r"|Rs\.?\s?[\d,]+(?:\.\d+)?(?:\s*(?:Crore|Lakh|Lakhs|Crores))?)"
    )

    # -----------------------------
    # EMD Amount
    # -----------------------------
    financial["EMD Amount"] = search_amount(
        rf"(?:EMD\s+Amount|Earnest\s+Money\s+Deposit).{{0,60}}?({amount_pattern})",
        text
    )

    # -----------------------------
    # Tender Fee
    # -----------------------------
    financial["Tender Fee"] = search_amount(
        rf"(?:Tender\s+Fee|Cost\s+of\s+Tender|Document\s+Fee).{{0,60}}?({amount_pattern})",
        text
    )

    # -----------------------------
    # Security Deposit
    # -----------------------------
    financial["Security Deposit"] = search_amount(
        rf"(?:Security\s+Deposit).{{0,60}}?({amount_pattern})",
        text
    )

    # -----------------------------
    # Performance Guarantee
    # -----------------------------
    financial["Performance Guarantee"] = search_amount(
        rf"(?:Performance\s+Guarantee|Performance\s+Security).{{0,60}}?({amount_pattern})",
        text
    )

    # -----------------------------
    # Estimated Tender Value
    # -----------------------------
    financial["Estimated Tender Value"] = search_amount(
        rf"(?:Estimated\s+Value|Tender\s+Value|Project\s+Cost).{{0,60}}?({amount_pattern})",
        text
    )

    return financial