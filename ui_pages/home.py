import streamlit as st


def show_home():

    st.title("🤖 SalesMind AI Enterprise")
    st.caption("AI-Powered Business Intelligence Platform")

    st.markdown("---")

    col1, col2 = st.columns([2, 1])

    with col1:
        st.subheader("🚀 Features")

        st.markdown("""
- 📊 Interactive Sales Dashboard
- 💬 AI Business Analyst
- 📚 Company Knowledge Assistant (RAG)
- 📂 PDF Upload & Semantic Search
- 📄 Executive Report Generator
- 📥 PDF Report Export
- 🤖 Local AI using Ollama + Qwen3
""")

    with col2:
        st.info("""
### 🛠 Tech Stack

- Python
- Streamlit
- LangChain
- ChromaDB
- Ollama
- Qwen3
- Pandas
""")

    st.markdown("---")

    st.success("✅ Built by Naitik Soni | Generative AI Portfolio Project")