from backend.text_cleaner import clean_text

sample = """
Tender     Notice


EMD Amount     ₹2,00,000


GST      Required
"""

print(clean_text(sample))