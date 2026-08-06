from modules.vector_store import vector_db
from modules.llm import ask_llm


def ask_rag(question):
    # Search the vector database
    docs = vector_db.similarity_search(question, k=3)

    # Combine retrieved documents
    context = "\n\n".join([doc.page_content for doc in docs])

    # Create prompt
    prompt = f"""
You are an AI assistant for SalesMind AI.

Use ONLY the information below to answer.

Context:
{context}

Question:
{question}

Answer:
"""

    # Ask the LLM
    print("=" * 80)
    print(prompt)
    print("=" * 80)
    answer = ask_llm(prompt)

    return answer