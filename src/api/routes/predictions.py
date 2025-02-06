from fastapi import APIRouter, HTTPException, Query
from fastapi.responses import JSONResponse
from src.models.predict import get_prediction
import matplotlib.pyplot as plt
import io
import base64

router = APIRouter()

@router.get("/predict")
async def predict(currency: str = Query(..., description="Название криптовалюты, например, BTC")):
    if not currency:
        raise HTTPException(status_code=400, detail="Currency parameter is missing")
    
    prediction_data = get_prediction(currency)
    
    fig, ax = plt.subplots()
    ax.plot(prediction_data['dates'], prediction_data['values'], label='Forecast')
    ax.set_title(f'Forecast for {currency}')
    ax.legend()
    
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    image_base64 = base64.b64encode(buf.getvalue()).decode('utf-8')
    plt.close(fig)
    
    return JSONResponse(content={'currency': currency, 'chart': image_base64})
