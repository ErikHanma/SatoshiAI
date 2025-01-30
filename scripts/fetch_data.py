import pandas as pd
import requests
from datetime import datetime

def fetch_crypto_data(symbol: str = "BTCUSDT", interval: str = "1d", limit: int = 1000):
    url = f"https://api.binance.com/api/v3/klines?symbol={symbol}&interval={interval}&limit={limit}"
    response = requests.get(url)
    data = response.json()
    
    # Конвертация в DataFrame
    columns = ["timestamp", "open", "high", "low", "close", "volume", "close_time", "quote_asset_volume", 
               "trades", "taker_buy_base", "taker_buy_quote", "ignore"]
    df = pd.DataFrame(data, columns=columns)
    df["timestamp"] = pd.to_datetime(df["timestamp"], unit="ms")
    df.set_index("timestamp", inplace=True)
    return df[["open", "high", "low", "close", "volume"]]

if __name__ == "__main__":
    data = fetch_crypto_data()
    data.to_csv("data/raw/crypto_prices.csv")  # Создай папку data/raw/