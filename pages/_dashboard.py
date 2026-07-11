import streamlit as st
import pandas as pd
import plotly.express as px
from utils.session import (
    initialize_session,
    get_dataset,
)
st.set_page_config(
    page_title="Dashboard",
    page_icon="📈",
    layout="wide"
)
st.title("📈Executive Dashboard")

initialize_session()
df = get_dataset()
st.write(df)

from modules.analytics import (
    get_kpis,
    sales_by_category,
    sales_by_region,
    top_products,
    courier_performance,
    monthly_revenue,
    overall_rto,
    rto_by_region,
    rto_reasons,
)



if df is None:

    st.warning(
        "Please upload or generate a dataset from the Home page."
    )
    st.stop()

st.sidebar.header("Filters")
    
selected_categories = st.sidebar.multiselect(
    "Category",
options=sorted(df["category"].unique()),
default=sorted(df["category"].unique())
)

selected_regions = st.sidebar.multiselect(
    "Region",
options=sorted(df["region"].unique()),
default=sorted(df["region"].unique())
)
    
selected_couriers = st.sidebar.multiselect(
    "Courier",
options=sorted(df["courier"].unique()),
default=sorted(df["courier"].unique())
)
    
filtered_df = df[
(df["region"].isin(selected_regions))
&
(df["category"].isin(selected_categories))
&
(df["courier"].isin(selected_couriers))
]

st.caption(
f"Showing {len(filtered_df):,} of {len(df):,} orders"
)

kpis = get_kpis(filtered_df)

c1, c2, c3, c4, c5 = st.columns(5)

c1.metric(
    "Revenue",
    f"₹{kpis['Revenue']:,.0f}"
)

c2.metric(
    "Profit",
    f"₹{kpis['Profit']:,.0f}"
)

c3.metric(
    "Orders",
    f"{kpis['Orders']:,}"
)

c4.metric(
    "Average Order",
    f"₹{kpis['Average Order Value']:,.0f}"
)

c5.metric(
    "RTO %",
    f"{kpis['RTO Rate']:.2f}"
)


left, right = st.columns(2)

with left:

    category_df = sales_by_category(filtered_df)

    fig = px.bar(
    category_df,
    x="category",
    y="revenue",
    title="Revenue by Category"
)

    st.plotly_chart(
    fig,
    use_container_width=True
)


with right:

    region_df = sales_by_region(filtered_df)

    fig = px.pie(
        region_df,
        names="region",
        values="revenue",
        title="Revenue by Region"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )
st.divider()

left, right = st.columns(2)

with left:

    top_df = top_products(filtered_df)

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

    monthly_df = monthly_revenue(filtered_df)

    fig = px.line(
    monthly_df,
    x="Month",
    y="revenue",
    markers=True,
    title="Monthly Revenue Trend"
    )

    fig.update_layout(
        template="plotly_white",
        height=450,
        title_x=0.5
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )
st.divider()

region_rto = rto_by_region(filtered_df)

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

reason_df = rto_reasons(filtered_df)

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