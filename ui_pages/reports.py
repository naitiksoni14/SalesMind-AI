import streamlit as st
import pandas as pd

from modules.report_generator import generate_report
from modules.pdf_export import export_report


def show_reports():

    st.title("📄 Executive Report Generator")
    st.caption("Generate AI-powered executive business reports from your sales data.")

    uploaded_csv = st.file_uploader(
        "📂 Upload Sales CSV",
        type=["csv"]
    )

    if uploaded_csv is None:
        st.info("Upload a CSV file to generate an executive report.")
        return

    df = pd.read_csv(uploaded_csv)

    st.subheader("📊 Dataset Preview")
    st.dataframe(df, use_container_width=True)

    st.divider()

    if st.button("🚀 Generate Executive Report"):

        with st.spinner("🤖 AI is generating your report..."):

            report = generate_report(df)

        st.success("✅ Report Generated Successfully!")

        st.subheader("📋 Executive Report")

        st.text_area(
            "",
            report,
            height=350
        )

        pdf_path = export_report(report)

        with open(pdf_path, "rb") as pdf_file:

            st.download_button(
                label="📥 Download PDF Report",
                data=pdf_file,
                file_name="Executive_Report.pdf",
                mime="application/pdf"
            )