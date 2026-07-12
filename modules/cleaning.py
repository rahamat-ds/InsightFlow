import pandas as pd


def dataset_summary(df):

    return {
        "Rows": len(df),
        "Columns": len(df.columns),
        "Duplicates": df.duplicated().sum(),
        "Missing Values": df.isna().sum().sum(),
        "Memory (MB)": round(
            df.memory_usage(deep=True).sum() / 1024**2,
            2
        ),
    }


def column_summary(df):

    summary = pd.DataFrame({

        "Column": df.columns,

        "Type": df.dtypes.astype(str),

        "Missing": df.isna().sum().values,

        "Unique": df.nunique().values,
    })

    return summary


def remove_duplicates(df):

    df = df.copy()

    df = df.drop_duplicates()

    return df


def trim_text(df):

    df = df.copy()

    text_columns = df.select_dtypes(include="object").columns

    for col in text_columns:

        df[col] = df[col].astype(str).str.strip()

    return df

def convert_dates(df):

    df = df.copy()

    date_columns = [
        "order_date",
        "dispatch_date",
        "delivery_date"
    ]

    for col in date_columns:

        if col in df.columns:

            df[col] = pd.to_datetime(
                df[col],
                errors="coerce"
            )

    return df



def fill_missing(df):

    import pandas as pd

    df = df.copy()

    for col in df.columns:

        if pd.api.types.is_string_dtype(df[col]):

            mode = df[col].mode()

            if not mode.empty:
                df[col] = df[col].fillna(mode.iloc[0])

        elif pd.api.types.is_numeric_dtype(df[col]):

            df[col] = df[col].fillna(df[col].median())

        elif pd.api.types.is_datetime64_any_dtype(df[col]):

            df[col] = df[col].ffill()

    return df



def clean_dataset(df):

    report = {}

    # ----------------------------
    # Initial Stats
    # ----------------------------

    report["Rows Before"] = len(df)

    report["Missing Before"] = int(df.isna().sum().sum())

    report["Duplicates Before"] = int(df.duplicated().sum())

    # ----------------------------
    # Remove Duplicates
    # ----------------------------

    df = remove_duplicates(df)

    report["Rows After"] = len(df)

    report["Duplicates Removed"] = (
        report["Rows Before"]
        - report["Rows After"]
    )

    # ----------------------------
    # Trim Text
    # ----------------------------

    text_columns = len(
        df.select_dtypes(include="object").columns
    )

    df = trim_text(df)

    report["Text Columns Cleaned"] = text_columns

    # ----------------------------
    # Convert Dates
    # ----------------------------

    date_columns = 0

    for col in [
        "order_date",
        "dispatch_date",
        "delivery_date"
    ]:

        if col in df.columns:
            date_columns += 1

    df = convert_dates(df)

    report["Date Columns Converted"] = date_columns

    # ----------------------------
    # Fill Missing
    # ----------------------------

    before = int(df.isna().sum().sum())

    df = fill_missing(df)

    after = int(df.isna().sum().sum())

    report["Missing Values Filled"] = before - after

    return df, report