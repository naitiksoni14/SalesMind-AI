import streamlit as st

from modules.llm import ask_llm


def show_business_ai():

    st.title("💬 AI Business Analyst")
    st.caption("Ask AI to analyze your business data and provide strategic insights.")

    question = st.text_area(
        "Business Question",
        placeholder="Example: Which city generated the highest revenue and why?",
        height=150
    )

    if st.button("🚀 Analyze Business"):

        if not question.strip():
            st.warning("Please enter a question.")
            return

        with st.spinner("🤖 AI is analyzing your business..."):

            prompt = f"""
You are an expert Senior Business Analyst.

Answer the user's question professionally.

Question:
{question}

Give:
1. Summary
2. Business Insight
3. Recommendation
"""

            answer = ask_llm(prompt)

        st.success("Analysis Complete")

        st.markdown("## 📋 AI Report")

        st.write(answer)