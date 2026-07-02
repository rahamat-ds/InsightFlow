import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="InsightFlow",
    page_icon="📊",
    layout="wide"
)

st.title("📊 InsightFlow")

st.subheader("Business Analytics Automation Platform")

st.write(
    "Welcome! This application will automate data cleaning, analysis, and visualization."
)

uploaded_file = st.file_uploader(
    "Upload your sales CSV",
    type=["csv"]
)
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.success("CSV uploaded successfully!")
    st.dataframe(df)

    st.subheader("Dataset Summary")

    col1, col2 = st.columns(2)
    col1.metric("Rows", df.shape[0])
    col2.metric("Columns", df.shape[1])

    st.write("Column Names:")
    st.write(list(df.columns))