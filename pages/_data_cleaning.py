import streamlit as st
import pandas as pd

from utils.session import (
    initialize_session,
    get_dataset,
    update_dataset,
    set_dataset,
)

from modules.cleaning import (
    dataset_summary,
    column_summary,
    clean_dataset,
)

st.set_page_config(
    page_title="Data Cleaning",
    page_icon="🧹",
    layout="wide"
)

initialize_session()

df = get_dataset()
if df is None:
    st.warning("Generate or upload a dataset first.")
    st.stop()

st.title("🧹Data Cleaning")

summary = dataset_summary(df)
c1, c2, c3, c4, c5 = st.columns(5)
c1.metric("Rows", summary["Rows"])
c2.metric("Columns", summary["Columns"])
c3.metric("Duplicates", summary["Duplicates"])
c4.metric("Missing", summary["Missing Values"])
c5.metric("Memory", f"{summary['Memory (MB)']} MB")
st.subheader("Column Summary")
summary_df = column_summary(df)

st.dataframe(
    summary_df,
    use_container_width=True
)

st.divider()

st.write(
    "Run the automated cleaning pipeline on the current dataset."
)

if st.button("🧹Clean Dataset", use_container_width=True):
    cleaned_df = clean_dataset(df)
    update_dataset(cleaned_df)
    st.success("Dataset cleaned successfully!")
    st.dataframe(cleaned_df.head())


csv = df.to_csv(index=False).encode("utf-8")

st.download_button(
    "⬇ Download Current Dataset",
    csv,
    "clean_dataset.csv",
    "text/csv"
)

