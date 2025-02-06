from pydantic import BaseSettings

class Settings(BaseSettings):
    api_host: str = "0.0.0.0"
    api_port: int = 8000
    model_path: str = "model_weights/prophet_model.pkl"
    data_path: str = "data/processed/train_data.csv"

    class Config:
        env_file = ".env"

settings = Settings()
