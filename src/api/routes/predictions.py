from fastapi import APIRouter
from datetime import datetime, timedelta
import pandas as pd
import joblib

router = APIRouter()

@router.post("/predict")
async def predict(future_hours: int = 24):
    # Загрузка модели
    model = joblib.load("model_weights/prophet_model.pkl")
    
    # Создание датафрейма для прогноза
    future = model.make_future_dataframe(periods=future_hours, freq="H")
    future["volume"] = 10000
    
    # Прогноз
    forecast = model.predict(future)
    return forecast[["ds", "yhat"]].tail(future_hours).to_dict()