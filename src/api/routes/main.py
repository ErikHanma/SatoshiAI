from fastapi import APIRouter
from src.models.predict import make_prediction
from flask import Blueprint, render_template

router = APIRouter()

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def home():
    return render_template('index.html')

@router.get("/predict")
async def predict(periods: int = 24):
    return make_prediction(periods)


