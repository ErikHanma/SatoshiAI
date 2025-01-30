import pandas as pd

def add_features(df: pd.DataFrame):
    # Скользящее среднее за 7 дней
    df["MA7"] = df["close"].rolling(window=7).mean()
    # RSI (упрощенная версия)
    delta = df["close"].diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=14).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=14).mean()
    df["RSI"] = 100 - (100 / (1 + gain / loss))
    return df