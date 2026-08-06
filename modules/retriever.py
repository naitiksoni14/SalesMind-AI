from modules.vector_store import vector_db

retriever = vector_db.as_retriever(
    search_kwargs={"k": 2}
)