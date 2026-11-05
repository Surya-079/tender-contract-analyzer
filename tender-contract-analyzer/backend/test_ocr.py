from backend.ocr_reader import extract_image_text

text = extract_image_text("sample.jpg")

print(text)