import pandas as pd
from prophet import Prophet
import joblib

def train_model(data_path: str = "data/processed/train_data.csv"):
    df = pd.read_csv(data_path)
    df = df.rename(columns={"timestamp": "ds", "close": "y"})
    
    model = Prophet(
        yearly_seasonality=True,
        weekly_seasonality=True,
        daily_seasonality=False
    )
    model.add_regressor("volume")
    model.fit(df)
    
    joblib.dump(model, "model_weights/prophet_model.pkl")

if __name__ == "__main__":
    train_model()