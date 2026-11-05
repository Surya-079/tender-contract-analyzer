from backend.pdf_reader import extract_pdf_text

text = extract_pdf_text("sample.pdf")

print(text)