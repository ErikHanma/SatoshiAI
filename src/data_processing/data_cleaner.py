import pandas as pd

def clean_data(df: pd.DataFrame):
    # Удаление дубликатов
    df = df.drop_duplicates()
    # Заполнение пропусков
    df = df.ffill().bfill()
    return df

def normalize_columns(df: pd.DataFrame):
    if "timestamp" in df.columns:
        df = df.rename(columns={"timestamp": "ds"})
    elif "date" in df.columns:
        df = df.rename(columns={"date": "ds"})
    if "close" in df.columns:
        df = df.rename(columns={"close": "y"})
    return df
