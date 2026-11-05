import re

from backend.financial import extract_financial_details
from backend.deadlines import extract_deadlines
from backend.eligibility import extract_eligibility


def find_project_name(text: str) -> str:

    patterns = [
        r"Name of Work\s*[:\-]\s*([^\n\r]+)",
        r"Project Name\s*[:\-]\s*([^\n\r]+)",
        r"Work\s*[:\-]\s*([^\n\r]+)",
        r"Subject\s*[:\-]\s*([^\n\r]+)"
    ]

    for pattern in patterns:
        match = re.search(pattern, text, re.IGNORECASE)

        if match:
            return match.group(1).strip()

    return "Not Found"


def find_location(text: str) -> str:

    cities = [
        "Chennai",
        "Mumbai",
        "Delhi",
        "Bengaluru",
        "Hyderabad",
        "Kolkata",
        "Pune",
        "Ahmedabad"
    ]

    for city in cities:
        if re.search(rf"\b{city}\b", text, re.IGNORECASE):
            return city

    return "Not Found"


def generate_summary(text: str) -> str:
    """
    Generate tender summary.
    """

    eligibility = extract_eligibility(text)
    financial = extract_financial_details(text)
    deadlines = extract_deadlines(text)

    summary = []

    summary.append(
        f"Project Name : {find_project_name(text)}"
    )
   
    summary.append('\n')

    summary.append(
        f"Location : {find_location(text)}"
    )
    summary.append('\n')

    summary.append(
        f"Estimated Value : {financial['Estimated Tender Value']}"
    )
    summary.append('\n')

    summary.append(
        f"EMD Amount : {financial['EMD Amount']}"
    )
    summary.append('\n')

    summary.append(
        f"Tender Fee : {financial['Tender Fee']}"
    )
    summary.append('\n')

    summary.append(
        f"Submission Deadline : {deadlines['Bid Submission Deadline']}"
    )
    summary.append('\n')

    summary.append("\nEligibility Requirements")

    if eligibility["Minimum Turnover"] != "Not Found":
        summary.append(
            f"• Minimum Turnover : {eligibility['Minimum Turnover']}"
        )

    if eligibility["Experience"] != "Not Found":
        summary.append(
            f"• Experience : {eligibility['Experience']}"
        )

    if eligibility["Similar Projects"] != "Not Found":
        summary.append(
            f"• Similar Projects : {eligibility['Similar Projects']}"
        )

    if eligibility["GST Required"] == "Yes":
        summary.append("• GST Registration Required")

    if eligibility["PAN Required"] == "Yes":
        summary.append("• PAN Required")

    if eligibility["ISO Certification"] != "Not Required":
        summary.append(
            f"• {eligibility['ISO Certification']} Required"
        )

    return "\n".join(summary)