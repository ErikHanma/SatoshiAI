import joblib
import pandas as pd
from datetime import datetime
from src.utils.config import settings
import os
from src.data_processing.data_loader import load_raw_data

def get_prediction(currency: str) -> dict:
    model_path = f"model_weights/{currency.lower()}_model.pkl"
    
    if not os.path.exists(model_path):
        raise FileNotFoundError(f"Model for {currency} not found at {model_path}")
    
    model = joblib.load(model_path)
    
    today = datetime.today()
    future_dates = pd.date_range(start=today, periods=30)
    future = pd.DataFrame({"ds": future_dates})
    
    # Подключаем исторические данные по валюте
    df = load_raw_data(symbol=currency)
    if "volume" in df.columns:
        future["volume"] = df["volume"].iloc[-30:].values
    
    forecast = model.predict(future)
    
    return {
        "currency": currency,
        "dates": forecast["ds"].astype(str).tolist(),
        "values": forecast["yhat"].tolist()
    }
