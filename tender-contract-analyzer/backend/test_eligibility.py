from backend.eligibility import extract_eligibility

sample = """
Minimum turnover should be ₹5 Crore.

The bidder should have 5 years of experience.

Completed 3 similar projects.

GST Registration is mandatory.

PAN card is mandatory.

ISO9001 certification required.

Only MSME firms are eligible.
"""

result = extract_eligibility(sample)

for key, value in result.items():
    print(f"{key}: {value}")