from pydantic import BaseSettings

class Settings(BaseSettings):
    api_port: int = 8000
    model_path: str = "model_weights/prophet_model.pkl"
    data_path: str = "data/raw/crypto_prices.csv"

settings = Settings()