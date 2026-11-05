from datetime import datetime

from backend.eligibility import extract_eligibility
from backend.financial import extract_financial_details
from backend.deadlines import extract_deadlines


def analyze_risk(text: str) -> list:
    """
    Analyze tender document and identify possible risks.

    Args:
        text (str): Tender document text.

    Returns:
        list: Risk messages.
    """

    risks = []

    eligibility = extract_eligibility(text)
    financial = extract_financial_details(text)
    deadlines = extract_deadlines(text)

    # -------------------------
    # Turnover Requirement
    # -------------------------
    turnover = eligibility["Minimum Turnover"]

    if turnover != "Not Found":
        risks.append(
            f"Minimum turnover requirement detected ({turnover}). Ensure your company satisfies this requirement."
        )

    # -------------------------
    # Experience
    # -------------------------
    experience = eligibility["Experience"]

    if experience != "Not Found":
        risks.append(
            f"Experience requirement detected ({experience})."
        )

    # -------------------------
    # Similar Projects
    # -------------------------
    if eligibility["Similar Projects"] != "Not Found":
        risks.append(
            "Previous similar project experience is mandatory."
        )

    # -------------------------
    # ISO Certification
    # -------------------------
    if eligibility["ISO Certification"] != "Not Required":
        risks.append(
            f"{eligibility['ISO Certification']} certification is required."
        )

    # -------------------------
    # GST
    # -------------------------
    if eligibility["GST Required"] == "Yes":
        risks.append(
            "GST registration is mandatory."
        )

    # -------------------------
    # PAN
    # -------------------------
    if eligibility["PAN Required"] == "Yes":
        risks.append(
            "PAN is mandatory."
        )

    # -------------------------
    # EMD
    # -------------------------
    emd = financial["EMD Amount"]

    if emd != "Not Found":
        risks.append(
            f"Earnest Money Deposit required: {emd}"
        )

    # -------------------------
    # Tender Fee
    # -------------------------
    fee = financial["Tender Fee"]

    if fee != "Not Found":
        risks.append(
            f"Tender fee payable: {fee}"
        )

    # -------------------------
    # Submission Deadline
    # -------------------------
    deadline = deadlines["Bid Submission Deadline"]

    if deadline != "Not Found":

        formats = [
            "%d-%m-%Y",
            "%d/%m/%Y",
            "%d %B %Y",
            "%d %b %Y"
        ]

        for fmt in formats:

            try:

                deadline_date = datetime.strptime(deadline, fmt)

                remaining_days = (
                    deadline_date - datetime.today()
                ).days

                if remaining_days < 0:
                    risks.append(
                        "Tender submission deadline has already passed."
                    )

                elif remaining_days <= 3:
                    risks.append(
                        "Tender deadline is within 3 days."
                    )

                elif remaining_days <= 7:
                    risks.append(
                        "Tender deadline is within one week."
                    )

                break

            except ValueError:
                continue

    return risks