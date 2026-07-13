
import pandas as pd
from utils.session import (
    initialize_session,
    set_dataset,
    get_dataset
)

initialize_session()

df = get_dataset()

def get_kpis(df):

    revenue = df["revenue"].sum()

    profit = df["profit"].sum()

    orders = len(df)

    avg_order = df["revenue"].mean()

    rto_rate = df["rto"].mean() * 100

    return {
        "Revenue": revenue,
        "Profit": profit,
        "Orders": orders,
        "Average Order Value": avg_order,
        "RTO Rate": rto_rate,
    }

def sales_by_category(df):

    return (
        df.groupby("category", as_index=False)["revenue"]
        .sum()
        .sort_values("revenue", ascending=False)
    )

def sales_by_region(df):

    return (
        df.groupby("region", as_index=False)["revenue"]
        .sum()
    )

def top_products(df):

    return (
        df.groupby("product_name", as_index=False)["revenue"]
        .sum()
        .sort_values("revenue", ascending=False)
        .head(10)
    )

def courier_performance(df):

    return (
        df.groupby("courier")
        .agg(
            Orders=("courier", "count"),
            Revenue=("revenue", "sum"),
            RTO=("rto", "mean"),
        )
    )

def monthly_revenue(df):

    monthly_df = df.copy()

    monthly_df["order_date"] = pd.to_datetime(
        monthly_df["order_date"]
    )

    monthly_df["Month"] = (
        monthly_df["order_date"]
        .dt.to_period("M")
        .astype(str)
    )

    monthly_df = (
        monthly_df
        .groupby("Month", as_index=False)["revenue"]
        .sum()
    )

    return monthly_df

def overall_rto(df):

    return round(df["rto"].mean() * 100, 2)

def rto_by_region(df):

    region_df = (
        df.groupby("region", as_index=False)
        .agg(
            RTO=("rto", "mean")
        )
    )

    region_df["RTO"] *= 100

    return region_df

def rto_reasons(df):

    return (
        df[df["rto"]]
        .groupby("rto_reason", as_index=False)
        .size()
        .sort_values("size", ascending=False)
    )

def category_performance(df):

    return (
        df.groupby("category", as_index=False)
        .agg(
            Revenue=("revenue", "sum"),
            Profit=("profit", "sum"),
            Orders=("category", "count"),
            Quantity=("quantity", "sum"),
        )
        .sort_values(
            "Revenue",
            ascending=False
        )
    )

def region_performance(df):

    return (
        df.groupby("region", as_index=False)
        .agg(
            Revenue=("revenue", "sum"),
            Profit=("profit", "sum"),
            Orders=("region", "count"),
            Quantity=("quantity", "sum"),
        )
        .sort_values(
            "Revenue",
            ascending=False
        )
    )

def courier_performance(df):

    courier_df = (
        df.groupby("courier", as_index=False)
        .agg(
            Orders=("courier", "count"),
            Revenue=("revenue", "sum"),
            Profit=("profit", "sum"),
            RTO=("rto", "mean"),
        )
    )

    courier_df["RTO"] *= 100

    return courier_df.sort_values(
        "Revenue",
        ascending=False
    )

def gender_distribution(df):

    return (
        df.groupby("gender", as_index=False)
        .size()
        .rename(columns={"size": "Customers"})
    )

def loyalty_distribution(df):

    return (
        df.groupby("loyalty_tier", as_index=False)
        .size()
        .rename(columns={"size": "Customers"})
    )

def payment_distribution(df):

    return (
        df.groupby("payment_method", as_index=False)
        .size()
        .rename(columns={"size": "Orders"})
    )

def age_distribution(df):

    return (
        df.groupby("age", as_index=False)
        .size()
        .rename(columns={"size": "Customers"})
    )

def discount_analysis(df):

    return (
        df.groupby("category", as_index=False)
        .agg(
            Average_Discount=("discount_percent", "mean"),
            Revenue=("revenue", "sum"),
            Profit=("profit", "sum"),
        )
    )

def manufacturer_performance(df):

    return (
        df.groupby("manufacturer", as_index=False)
        .agg(
            Revenue=("revenue", "sum"),
            Profit=("profit", "sum"),
            Orders=("manufacturer", "count"),
        )
        .sort_values(
            "Revenue",
            ascending=False
        )
    )

def shipping_analysis(df):

    return (
        df.groupby("shipping_mode", as_index=False)
        .agg(
            Orders=("shipping_mode", "count"),
            Revenue=("revenue", "sum"),
            Profit=("profit", "sum"),
            Delivery_Days=("delivery_days", "mean"),
        )
    )

def profit_margin(df):

    margin_df = (
        df.groupby("category", as_index=False)
        .agg(
            Revenue=("revenue", "sum"),
            Profit=("profit", "sum"),
        )
    )
    margin_df["Profit Margin"] = (
        margin_df["Profit"]
        / margin_df["Revenue"]
    ) * 100

    return margin_df

#------------------------------

# def business_insights(df):

#     insights = []

#     # ------------------------
#     # Revenue Leader
#     # ------------------------

#     top_region = (
#         df.groupby("region")["revenue"]
#         .sum()
#         .idxmax()
#     )

#     top_region_rev = (
#         df.groupby("region")["revenue"]
#         .sum()
#         .max()
#     )

#     insights.append(
#         f"📈 {top_region} generated the highest revenue (₹{top_region_rev:,.0f})."
#     )

#     # ------------------------
#     # Best Category
#     # ------------------------

#     top_category = (
#         df.groupby("category")["revenue"]
#         .sum()
#         .idxmax()
#     )

#     insights.append(
#         f"🏆 {top_category} is the best-selling category."
#     )

#     # ------------------------
#     # Highest RTO
#     # ------------------------

#     rto = (
#         df.groupby("region")["rto"]
#         .mean()
#         * 100
#     )

#     worst_region = rto.idxmax()

#     insights.append(
#         f"⚠️ {worst_region} has the highest RTO rate ({rto.max():.1f}%)."
#     )

#     # ------------------------
#     # Best Courier
#     # ------------------------

#     courier = (
#         df.groupby("courier")["revenue"]
#         .sum()
#     )

#     insights.append(
#         f"🚚 {courier.idxmax()} generated the highest courier revenue."
#     )

#     # ------------------------
#     # Preferred Payment
#     # ------------------------

#     payment = (
#         df["payment_method"]
#         .value_counts()
#     )

#     insights.append(
#         f"💳 Most customers prefer {payment.idxmax()}."
#     )

#     # ------------------------
#     # Loyalty
#     # ------------------------

#     loyalty = (
#         df["loyalty_tier"]
#         .value_counts()
#     )

#     insights.append(
#         f"⭐ {loyalty.idxmax()} is the dominant loyalty tier."
#     )

#     return insights

def business_insights(df):

    insights = []

    # Revenue leader

    region_rev = (
        df.groupby("region")["revenue"]
        .sum()
        .sort_values(ascending=False)
    )

    insights.append(
        f"📈 {region_rev.index[0]} generated the highest revenue (₹{region_rev.iloc[0]:,.0f})."
    )

    # Category leader

    category_rev = (
        df.groupby("category")["revenue"]
        .sum()
        .sort_values(ascending=False)
    )

    insights.append(
        f"🏆 {category_rev.index[0]} is the best-selling category."
    )

    # Highest RTO

    rto = (
        df.groupby("region")["rto"]
        .mean()
        * 100
    )

    insights.append(
        f"⚠️ {rto.idxmax()} has the highest RTO rate ({rto.max():.1f}%)."
    )

    # Best courier

    courier_rev = (
        df.groupby("courier")["revenue"]
        .sum()
        .sort_values(ascending=False)
    )

    insights.append(
        f"🚚 {courier_rev.index[0]} generated the highest courier revenue."
    )

    # Payment method

    payment = df["payment_method"].value_counts()

    insights.append(
        f"💳 {payment.idxmax()} is the most used payment method."
    )

    # Loyalty

    loyalty = df["loyalty_tier"].value_counts()

    insights.append(
        f"⭐ {loyalty.idxmax()} customers dominate the customer base."
    )

    # Most profitable category

    profit_cat = (
        df.groupby("category")["profit"]
        .sum()
        .sort_values(ascending=False)
    )

    insights.append(
        f"💰 {profit_cat.index[0]} generates the highest profit."
    )

    # Highest margin category

    margin = (
        df.groupby("category")
        .agg(
            Revenue=("revenue", "sum"),
            Profit=("profit", "sum")
        )
    )

    margin["Margin"] = (
        margin["Profit"]
        / margin["Revenue"]
        * 100
    )

    insights.append(
        f"📊 {margin['Margin'].idxmax()} has the highest profit margin ({margin['Margin'].max():.1f}%)."
    )

    # Worst courier by RTO

    courier_rto = (
        df.groupby("courier")["rto"]
        .mean()
        * 100
    )

    insights.append(
        f"📦 {courier_rto.idxmax()} has the highest courier RTO ({courier_rto.max():.1f}%)."
    )

    # Fastest shipping

    shipping = (
        df.groupby("shipping_mode")["delivery_days"]
        .mean()
    )

    insights.append(
        f"⚡ {shipping.idxmin()} shipping is the fastest ({shipping.min():.1f} days average)."
    )

    return insights

#---------------------------

def revenue_concentration(df):

    temp = (
        df.groupby("category", as_index=False)
        .agg(
            Revenue=("revenue", "sum")
        )
    )

    total = temp["Revenue"].sum()

    temp["Revenue Share"] = (
        temp["Revenue"]
        / total
        * 100
    )

    return temp

def profit_contribution(df):

    temp = (
        df.groupby("category", as_index=False)
        .agg(
            Profit=("profit", "sum")
        )
    )

    total = temp["Profit"].sum()

    temp["Profit Share"] = (
        temp["Profit"]
        / total
        * 100
    )

    return temp

def worst_products(df):

    return (
        df.groupby("product_name", as_index=False)
        .agg(
            Revenue=("revenue", "sum")
        )
        .sort_values(
            "Revenue",
            ascending=True
        )
        .head(10)
    )
