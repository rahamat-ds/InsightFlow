import pandas as pd


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


