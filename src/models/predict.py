import joblib
import pandas as pd

def make_prediction(periods: int = 24):
    model = joblib.load("model_weights/prophet_model.pkl")
    future = model.make_future_dataframe(periods=periods, freq="H")
    forecast = model.predict(future)
    return forecast[["ds", "yhat"]].tail(periods).to_dict()