import pandas as pd
import os

def load_raw_data(symbol: str = "BTC-USD"):
    path = os.path.join("data", "raw", f"{symbol}_raw.csv")
    return pd.read_csv(path, index_col="date", parse_dates=True)