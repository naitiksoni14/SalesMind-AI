from modules.load_documents import load_company_documents
from modules.text_splitter import text_splitter
from modules.vector_store import vector_db

docs = load_company_documents()

chunks = text_splitter.split_documents(docs)

vector_db.add_documents(chunks)

print(f"Stored {len(chunks)} chunks successfully!")
