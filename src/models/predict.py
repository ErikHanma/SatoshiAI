import joblib
import pandas as pd
from datetime import datetime, timedelta
from src.utils.config import settings

def get_prediction(currency: str) -> dict:
    model = joblib.load(settings.model_path)
    
    today = datetime.today()
    future_dates = pd.date_range(start=today, periods=30)
    future = pd.DataFrame({'ds': future_dates})
    
    forecast = model.predict(future)
    
    prediction_data = {
        'dates': forecast['ds'].astype(str).tolist(),
        'values': forecast['yhat'].tolist()
    }
    return prediction_data
