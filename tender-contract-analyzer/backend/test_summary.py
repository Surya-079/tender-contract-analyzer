from backend.summary import generate_summary

sample = """
Project Name : Construction of Rural Road

Department : Highways Department

Estimated Value : ₹12 Crore

EMD Amount : ₹2,00,000

Tender Fee : ₹5,000

Last Date : 20-06-2026

Minimum Turnover : ₹5 Crore

5 years of experience.

3 similar projects.

GST Registration Required.

PAN Card Required.

ISO9001 certification required.
"""

print(generate_summary(sample))