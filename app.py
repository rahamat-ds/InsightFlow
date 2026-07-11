import streamlit as st
import pandas as pd

from scripts.generate_dataset import generate_dataset
from modules.analytics import (
    get_kpis,
    sales_by_category,
    sales_by_region,
    top_products,
    courier_performance,
)
from utils.session import (
    initialize_session,
    set_dataset,
)

initialize_session()

st.set_page_config(
    page_title="InsightFlow",
    page_icon="%$",
    layout="wide"
)

st.title("InsightFlow")
st.subheader("Business Analytics Automation Platform")

st.write(
    "Welcome! This application will automate data cleaning, analysis and visualization."
)

# -------------------------------
# Sidebar
# -------------------------------

st.sidebar.title("InsightFlow")

source = st.sidebar.radio(
    "Choose Data Source",
    [
        "Upload CSV",
        "Generate Sample Dataset"
    ]
)

# DataFrame placeholder
df = None

# -------------------------------
# Upload CSV
# -------------------------------

if source == "Upload CSV":

    uploaded_file = st.file_uploader(
        "Upload your sales CSV",
        type=["csv"]
    )

    if uploaded_file is not None:

        df = pd.read_csv(uploaded_file)
        set_dataset(df)
        # st.write("HOME PAGE")
        # st.write(st.session_state.df.shape)
        st.success("CSV uploaded successfully!")

# -------------------------------
# Generate Sample Dataset
# -------------------------------

elif source == "Generate Sample Dataset":

    rows = st.sidebar.slider(
        "Number of Orders",
        min_value=100,
        max_value=10000,
        value=1000,
        step=100
    )

    if st.sidebar.button("Generate Dataset"):

        with st.spinner("Generating synthetic retail dataset..."):

            df = generate_dataset(rows)
            set_dataset(df)
        st.success(f"Generated {rows:,} orders successfully!")

# -------------------------------
# Display Dataset
# -------------------------------
if df is not None:
    kpis = get_kpis(df)
    st.subheader("Executive Dashboard")

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
        "Avg Order",
        f"₹{kpis['Average Order Value']:,.0f}"
    )

    c5.metric(
        "RTO %",
        f"{kpis['RTO Rate']:.2f}%"
    )

    st.divider()

    st.subheader("Dataset Summary")

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Rows",
        f"{df.shape[0]:,}"
    )

    col2.metric(
        "Columns",
        df.shape[1]
    )

    col3.metric(
        "Missing Values",
        int(df.isna().sum().sum())
    )


    st.divider()

    st.subheader("Dataset Preview")

    st.dataframe(
        df,
        use_container_width=True
    )

    csv = df.to_csv(index=False).encode("utf-8")

    st.download_button(
    label="⬇ Download CSV",
    data=csv,
    file_name="retail_orders.csv",
    mime="text/csv"
)


