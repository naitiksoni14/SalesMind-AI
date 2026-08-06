import streamlit as st


def show_about():

    st.title("ℹ️ About")

    st.markdown("""
# SalesMind AI Enterprise

An AI-powered Business Intelligence Platform.

### Features

- Sales Analytics Dashboard
- AI Business Analyst
- Company Knowledge Assistant (RAG)
- Executive Report Generator
- PDF Export

---

Built using

- Python
- Streamlit
- Ollama
- LangChain
- ChromaDB
- Pandas
""")