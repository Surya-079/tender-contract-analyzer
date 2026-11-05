from backend.risk import analyze_risk

sample = """
Minimum Turnover : ₹5 Crore

5 years of experience.

3 similar projects.

GST Registration Required.

PAN Required.

ISO9001 Certification Required.

EMD Amount : ₹2,00,000

Tender Fee : ₹5,000

Last Date : 15-07-2026
"""

risks = analyze_risk(sample)

for risk in risks:
    print("-", risk)