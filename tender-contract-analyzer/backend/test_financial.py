from backend.financial import extract_financial_details

sample = """
Estimated Value : ₹12 Crore

EMD Amount : ₹2,00,000

Tender Fee : ₹5,000

Security Deposit : ₹50,000

Performance Guarantee : ₹1,00,000
"""

result = extract_financial_details(sample)

for key, value in result.items():
    print(f"{key}: {value}")