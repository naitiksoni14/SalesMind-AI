from modules.load_documents import load_company_documents
from modules.text_splitter import text_splitter

docs = load_company_documents()

chunks = text_splitter.split_documents(docs)

print(f"Total chunks: {len(chunks)}")

for i, chunk in enumerate(chunks):
    print("=" * 40)
    print(f"Chunk {i+1}")
    print(chunk.page_content)
    