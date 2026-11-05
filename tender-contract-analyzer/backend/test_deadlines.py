from backend.deadlines import extract_deadlines

sample = """
Tender Publish Date : 01-06-2026

Pre-Bid Meeting : 10-06-2026

Last Date for Bid Submission : 20-06-2026

Technical Bid Opening : 22-06-2026

Financial Bid Opening : 25-06-2026
"""

result = extract_deadlines(sample)

for key, value in result.items():
    print(f"{key}: {value}")