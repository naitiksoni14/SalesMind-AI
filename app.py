import streamlit as st

from ui_pages.home import show_home
from ui_pages.dashboard import show_dashboard
from ui_pages.business_ai import show_business_ai
from ui_pages.rag_page import show_rag
from ui_pages.reports import show_reports
from ui_pages.about import show_about

st.set_page_config(
    page_title="SalesMind AI Enterprise",
    page_icon="🤖",
    layout="wide"
)

st.sidebar.title("🤖 SalesMind AI")

page = st.sidebar.radio(
    "Navigation",
    [
        "🏠 Home",
        "📊 Dashboard",
        "💬 AI Business Analyst",
        "📚 Company Knowledge (RAG)",
        "📄 Executive Reports",
        "ℹ️ About"
    ]
)

if page == "🏠 Home":
    show_home()

elif page == "📊 Dashboard":
    show_dashboard()

elif page == "💬 AI Business Analyst":
    show_business_ai()

elif page == "📚 Company Knowledge (RAG)":
    show_rag()

elif page == "📄 Executive Reports":
    show_reports()

elif page == "ℹ️ About":
    show_about()