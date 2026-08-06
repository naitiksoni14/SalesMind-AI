import streamlit as st

from modules.analytics import (
    load_data,
    total_revenue,
    total_orders,
    total_customers,
    total_companies,
    revenue_by_service,
    revenue_by_city,
    top_customers,
    preview_data,
)


def show_dashboard():

    st.title("📊 Sales Dashboard")
    st.caption("AI-powered overview of your sales performance")

    df = load_data()

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "💰 Total Revenue",
        f"₹ {total_revenue(df):,.0f}"
    )

    col2.metric(
        "📦 Total Orders",
        total_orders(df)
    )

    col3.metric(
        "👥 Total Customers",
        total_customers(df)
    )

    col4.metric(
        "🏢 Total Companies",
        total_companies(df)
    )

    st.divider()

    left, right = st.columns(2)

    with left:
        st.subheader("📈 Revenue by Service")
        st.bar_chart(revenue_by_service(df))

    with right:
        st.subheader("🏙 Revenue by City")
        st.bar_chart(revenue_by_city(df))

    st.divider()

    st.subheader("🏆 Top Customers")
    st.bar_chart(top_customers(df))

    st.divider()

    st.subheader("📋 Dataset Preview")
    st.dataframe(
        preview_data(df),
        use_container_width=True
    )