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
)

st.set_page_config(
    page_title="Analytics",
    page_icon="",
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
st.divider()

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

st.header("Courier Performance")

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