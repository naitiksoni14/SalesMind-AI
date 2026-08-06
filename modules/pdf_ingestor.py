import os
from modules.pdf_loader import load_pdf
from modules.text_splitter import split_documents
from modules.vector_store import vector_db


def ingest_pdf(pdf_path):
    documents = load_pdf(pdf_path)
    chunks = split_documents(documents)
    vector_db.add_documents(chunks)
    return len(chunks)


def save_uploaded_pdf(uploaded_file):
    os.makedirs("knowledge", exist_ok=True)

    file_path = os.path.join(
        "knowledge",
        uploaded_file.name
    )

    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    return file_path