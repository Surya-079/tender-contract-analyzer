import re

DATE_PATTERN = re.compile(
    r"\d{1,2}[./-]\d{1,2}[./-]\d{2,4}"
    r"(?:\s*(?:at)?\s*\d{1,2}[:.]\d{2}\s*(?:A\.?M\.?|P\.?M\.?|AM|PM)?)?",
    re.IGNORECASE
)


def extract_deadlines(text):

    deadlines = {
        "Tender Publish Date": "Not Found",
        "Document Download Start": "Not Found",
        "Bid Submission Start": "Not Found",
        "Bid Submission Deadline": "Not Found",
        "Pre-Bid Meeting": "Not Found",
        "Bid Opening Date": "Not Found"
    }

    for match in DATE_PATTERN.finditer(text):

        date = match.group()

        start = max(0, match.start() - 200)
        end = min(len(text), match.end() + 200)

        context = text[start:end].lower()

        if (
            "publish" in context
            or "published" in context
            or "media publish" in context
        ):
            deadlines["Tender Publish Date"] = date

        elif (
            "document download" in context
            or "sale start" in context
        ):
            deadlines["Document Download Start"] = date

        elif (
            "bid submission start" in context
            or "submission start" in context
        ):
            deadlines["Bid Submission Start"] = date

        elif (
            "last date" in context
            or "due date" in context
            or "submission end" in context
            or "last date and time" in context
            or "e-submission" in context
            or "bid submission" in context
        ):
            deadlines["Bid Submission Deadline"] = date

        elif (
            "pre bid" in context
            or "pre-bid" in context
        ):
            deadlines["Pre-Bid Meeting"] = date

        elif (
            "opened on" in context
            or "bid opening" in context
            or "opening date" in context
            or "technical bid opening" in context
            or "tenders will be opened" in context
        ):
            deadlines["Bid Opening Date"] = date

    return deadlines