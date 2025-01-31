import pandas as pd
import requests
import os
from datetime import datetime

def fetch_historical_data(symbol: str = "BTC-USD", interval: str = "1d"):
    url = f"https://api.coincap.io/v2/assets/{symbol}/history?interval={interval}"
    response = requests.get(url)
    data = response.json()["data"]
    
    df = pd.DataFrame(data)
    df["date"] = pd.to_datetime(df["date"])
    df.set_index("date", inplace=True)
    
    # Сохранение сырых данных
    raw_path = os.path.join("data", "raw", f"{symbol}_raw.csv")
    df.to_csv(raw_path)
    return df

if __name__ == "__main__":
    fetch_historical_data()