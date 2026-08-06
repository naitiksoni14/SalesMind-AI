from modules.pdf_loader import load_pdf

docs = load_pdf("knowledge/sample.pdf")

print(f"Total pages: {len(docs)}")

print("\nFirst Page:\n")

print(docs[0].page_content)