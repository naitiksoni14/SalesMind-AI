from modules.pdf_ingestor import ingest_pdf

chunks = ingest_pdf("knowledge/sample.pdf")

print(f"Successfully added {chunks} chunks to ChromaDB!")