from modules.retriever import retriever

docs = retriever.invoke("Who is the CEO of SalesMind AI?")

for doc in docs:
    print("=" * 50)
    print(doc.page_content)