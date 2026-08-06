from langchain_chroma import Chroma
from modules.embeddings import embedding_model

vector_db = Chroma(
    persist_directory="vector_db",
    embedding_function=embedding_model
)