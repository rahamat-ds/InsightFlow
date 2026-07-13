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
    layout="wide"
)
st.title("🧹Data Cleaning")

initialize_session()

df = get_dataset()
if df is None:
    st.warning("⚠️Please upload or generate a dataset from the Home page.")
    st.stop()

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
    cleaned_df, report = clean_dataset(df)
    update_dataset(cleaned_df)

    st.subheader("Cleaning Report")
    c1, c2 = st.columns(2)
    with c1:
        st.metric(
            "Rows Before",
            report["Rows Before"]
        )
        st.metric(
            "Rows After",
            report["Rows After"]
        )
        st.metric(
            "Duplicates Removed",
            report["Duplicates Removed"]
        )

    with c2:
        st.metric(
            "Missing Values Filled",
            report["Missing Values Filled"]
        )
        st.metric(
            "Text Columns Cleaned",
            report["Text Columns Cleaned"]
        )
        st.metric(
            "Date Columns Converted",
            report["Date Columns Converted"]
        )

    st.divider()

    st.dataframe(
        cleaned_df.head(),
        use_container_width=True
    )
    st.success("Dataset cleaned successfully!")

current_df = get_dataset()
csv = current_df.to_csv(index=False).encode("utf-8")

st.download_button(
    "⬇ Download Cleaned Dataset",
    csv,
    "clean_dataset.csv",
    "text/csv"
)

