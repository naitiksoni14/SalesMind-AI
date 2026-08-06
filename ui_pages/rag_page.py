import streamlit as st

from modules.rag import ask_rag
from modules.pdf_ingestor import (
    save_uploaded_pdf,
    ingest_pdf
)


def show_rag():

    st.title("📚 Company Knowledge Assistant")
    st.caption("Upload company documents and ask AI questions using Retrieval-Augmented Generation (RAG).")

    st.subheader("📂 Upload Knowledge Base")

    uploaded_file = st.file_uploader(
        "Choose a PDF document",
        type=["pdf"]
    )

    if uploaded_file is not None:

        with st.spinner("📄 Processing and indexing PDF..."):

            pdf_path = save_uploaded_pdf(uploaded_file)
            chunks = ingest_pdf(pdf_path)

        st.success(f"✅ PDF indexed successfully! ({chunks} chunks)")

    st.divider()

    st.subheader("💬 Ask AI")

    question = st.text_area(
        "Question",
        placeholder="Example: Who is the CEO of the company?",
        height=150
    )

    if st.button("🚀 Ask Company AI"):

        if not question.strip():
            st.warning("Please enter a question.")
            return

        with st.spinner("🔍 Searching company knowledge..."):

            answer = ask_rag(question)

        st.success("Answer Found")

        st.markdown("## 📖 AI Answer")

        st.write(answer)