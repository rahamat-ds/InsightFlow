import streamlit as st
import pandas as pd
import plotly.express as px
from utils.session import (
    initialize_session,
    get_dataset,
    set_dataset,
)
from modules.analytics import (
    category_performance,
    region_performance,
    courier_performance,
    gender_distribution,
    loyalty_distribution,
    payment_distribution,
    age_distribution,
    profit_margin,
    manufacturer_performance,
    discount_analysis,
    shipping_analysis,
    rto_by_region,
    rto_reasons,
    top_products,
    worst_products,
    business_insights,
    revenue_concentration,
    profit_contribution,
    get_kpis
)

st.set_page_config(
    page_title="Analytics",
    layout="wide"
)
st.title("🔎Analytics")

initialize_session()
df = get_dataset()
if df is None:
    st.warning(
        "⚠️Please upload or generate a dataset from the Home page."
    )
    st.stop()



intelligence_tab, sales_tab, customer_tab, logistics_tab, product_tab = st.tabs(
    [
        "🧠 Intelligence",
        "📊 Sales",
        "👥 Customers",
        "🚚 Logistics",
        "📦 Products"
    ]
)

with intelligence_tab:
    
    st.header("Automated Insights")
    insights = business_insights(df)
    with st.container(border=True):
        for insight in insights:
            st.markdown(f"- {insight}")

    st.divider()
    st.header("KPI Summery")
    kpis = get_kpis(df)
    c1, c2, c3, c4, c5 = st.columns(5)
    c1.metric("Revenue", f"₹{kpis['Revenue']:,.0f}")
    c2.metric("Profit", f"₹{kpis['Profit']:,.0f}")
    c3.metric("Orders", f"{kpis['Orders']:,}")
    c4.metric("Avg Order", f"₹{kpis['Average Order Value']:,.0f}")
    c5.metric("RTO", f"{kpis['RTO Rate']:.1f}%")

with sales_tab:
    left, right = st.columns(2)
    with left:
        st.header("Revenue Contribution")
        share_df = revenue_concentration(df)
        fig = px.pie(
            share_df,
            names="category",
            values="Revenue Share",
            title="Revenue Share by Category"
        )
        st.plotly_chart(
            fig,
            use_container_width=True
        )
    with right:
            st.header("Profit Contribution")
            profit_df = profit_contribution(df)
            fig = px.pie(
                profit_df,
                names="category",
                values="Profit Share",
                title="Profit Contribution by Category"
            )
            st.plotly_chart(
            fig,
            use_container_width=True
            )

    st.header("Profit Margin")
    margin_df = profit_margin(df)
    st.dataframe(
        margin_df,
        use_container_width=True
    )
    fig = px.bar(
        margin_df,
        x="category",
        y="Profit Margin",
        text="Profit Margin",
        title="Profit Margin by Category"
    )
    fig.update_traces(
        texttemplate="%{text:.1f}%"
    )
    st.plotly_chart(
        fig,
        use_container_width=True
    )
    st.divider()
    st.header("Region Performance")
    region_df = region_performance(df)

    st.dataframe(
        region_df,
        use_container_width=True
    )
    fig = px.bar(
        region_df,
        x="region",
        y="Revenue",
        color="Profit",
        title="Revenue by Region"
    )
    st.plotly_chart(
        fig,
        use_container_width=True
    )
    st.divider()
    st.header("Discount Analysis")
    left, right = st.columns(2)
    with left:
        discount_df = discount_analysis(df)
        st.dataframe(
            discount_df,
            use_container_width=True
        )
    with right:
        fig = px.scatter(
            discount_df,
            x="Average_Discount",
            y="Profit",
            size="Revenue",
            color="category",
            title="Discount vs Profit"
        )
        st.plotly_chart(
            fig,
            use_container_width=True
        )
    
with customer_tab:

    st.header("Customer Analytics")
    left, right = st.columns(2)
    with left:
        gender_df = gender_distribution(df)
        fig = px.pie(
            gender_df,
            names="gender",
            values="Customers",
            title="Gender Distribution"
        )
        st.plotly_chart(
            fig,
            use_container_width=True
        )
    with right:
        age_df = age_distribution(df)

        fig = px.histogram(
            df,
            x="age",
            nbins=12,
            title="Age Distribution"
        )
        st.plotly_chart(
            fig,
            use_container_width=True
        )

    left, right = st.columns(2)
    with left:
        payment_df = payment_distribution(df)
        fig = px.bar(
            payment_df,
            x="payment_method",
            y="Orders",
            title="Payment Methods"
        )
        st.plotly_chart(
            fig,
            use_container_width=True
        )
    with right:
        loyalty_df = loyalty_distribution(df)
        fig = px.bar(
            loyalty_df,
            x="loyalty_tier",
            y="Customers",
            title="Loyalty Tier"
        )
        st.plotly_chart(
            fig,
            use_container_width=True
        )

with logistics_tab:
    st.header("Logistics")
    courier_df = courier_performance(df)
    st.dataframe(
        courier_df,
        use_container_width=True
    )
    fig = px.bar(
        courier_df,
        x="courier",
        y="Revenue",
        color="RTO",
        title="Courier Revenue and RTO"
    )
    st.plotly_chart(
        fig,
        use_container_width=True
    )
    st.divider()

    st.header("Shipping Analysis")
    shipping_df = shipping_analysis(df)
    st.dataframe(
        shipping_df,
        use_container_width=True
    )
    fig = px.bar(
        shipping_df,
        x="shipping_mode",
        y="Delivery_Days",
        color="Profit",
        title="Average Delivery Time"
    )
    st.plotly_chart(
        fig,
        use_container_width=True
    )

    left, right = st.columns(2)
    with left:
        region_rto = rto_by_region(df)
        fig = px.bar(
            region_rto,
            x="region",
            y="RTO",
            text="RTO",
            title="RTO Rate by Region"
        )
        st.plotly_chart(
            fig,
            use_container_width=True
        )
    with right:
        reason_df = rto_reasons(df)
        fig = px.bar(
            reason_df,
            x="rto_reason",
            y="size",
            title="Top RTO Reasons"
        )
        st.plotly_chart(
            fig,
            use_container_width=True
        )

with product_tab:

    left, right = st.columns(2)
    with left:
        st.header("Top Products")
        top_df = top_products(df)
        fig = px.bar(
            top_df,
            x="revenue",
            y="product_name",
            orientation="h",
            title="Top 10 Products"
        )
        st.plotly_chart(
            fig,
            use_container_width=True
    )
    with right:
        st.header("Bottom Products")
        worst_df = worst_products(df)
        fig = px.bar(
            worst_df,
            x="Revenue",
            y="product_name",
            orientation="h"
        )
        st.plotly_chart(
            fig,
            use_container_width=True
        )

    st.header("Manufacturer Performance")
    manufacturer_df = manufacturer_performance(df)
    st.dataframe(
        manufacturer_df,
        use_container_width=True
    )
    fig = px.bar(
        manufacturer_df,
        x="manufacturer",
        y="Revenue",
        color="Profit",
        title="Revenue by Manufacturer"
    )
    st.plotly_chart(
        fig,
        use_container_width=True
    )
    st.header("Category Performance")
    category_df = category_performance(df)
    st.dataframe(
        category_df,
        use_container_width=True
    )
    fig = px.bar(
        category_df,
        x="category",
        y="Revenue",
        color="Profit",
        title="Revenue by Category"
    )
    st.plotly_chart(
        fig,
        use_container_width=True
    )



