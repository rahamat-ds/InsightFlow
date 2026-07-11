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
    df = remove_duplicates(df)
    df = trim_text(df)
    df = convert_dates(df)
    df = fill_missing(df)

    return df