from backend.compliance import generate_checklist

sample = """
GST Registration is mandatory.

PAN Card should be submitted.

ISO9001 Certificate is compulsory.

Bank Solvency Certificate should be attached.

Previous Work Orders of similar projects are required.

Audited Financial Statements of last three years are required.
"""

documents = generate_checklist(sample)

for document in documents:
    print(document)