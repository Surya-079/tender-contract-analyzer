from backend.docx_reader import extract_docx_text

text = extract_docx_text("sample.docx")

print(text)