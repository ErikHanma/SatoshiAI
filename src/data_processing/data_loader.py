import pandas as pd
import os
from src.data_processing.data_cleaner import normalize_columns

df = normalize_columns(df)


def load_raw_data(symbol: str = "BTC-USD"):
    path = os.path.join("data", "raw", f"{symbol}_raw.csv")
    df = pd.read_csv(path)
    
    if "timestamp" in df.columns:
        df = df.rename(columns={"timestamp": "ds"})
    elif "date" in df.columns:
        df = df.rename(columns={"date": "ds"})
    
    return df
