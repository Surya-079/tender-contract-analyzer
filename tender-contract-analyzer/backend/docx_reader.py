from docx import Document


def extract_docx_text(docx_path: str) -> str:
    """
    Extract text from a DOCX file.

    Args:
        docx_path (str): Path to the DOCX file.

    Returns:
        str: Extracted text.
    """

    text = ""

    try:
        document = Document(docx_path)

        for paragraph in document.paragraphs:

            if paragraph.text.strip():
                text += paragraph.text.strip() + "\n"

        # Read tables as well
        for table in document.tables:

            for row in table.rows:

                row_text = []

                for cell in row.cells:

                    cell_text = cell.text.strip()

                    if cell_text:
                        row_text.append(cell_text)

                if row_text:
                    text += " | ".join(row_text) + "\n"

    except Exception as e:
        print(f"DOCX Extraction Error: {e}")

    return text