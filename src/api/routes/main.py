from fastapi import APIRouter
from src.models.predict import make_prediction

router = APIRouter()

@router.get("/predict")
async def predict(periods: int = 24):
    return make_prediction(periods)