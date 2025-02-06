import pandas as pd
from prophet import Prophet
import joblib
from src.utils.config import settings

def train_model(data_path: str = None):
    if data_path is None:
        data_path = settings.data_path
    
    df = pd.read_csv(data_path)
    df = df.rename(columns={"timestamp": "ds", "close": "y"})
    
    model = Prophet(
        yearly_seasonality=True,
        weekly_seasonality=True,
        daily_seasonality=False
    )
    if "volume" in df.columns:
        model.add_regressor("volume")
    
    model.fit(df)
    
    joblib.dump(model, settings.model_path)
    print("Model trained and saved to", settings.model_path)

if __name__ == "__main__":
    train_model()
