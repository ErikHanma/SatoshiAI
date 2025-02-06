from fastapi import FastAPI
from src.api.routes import healthcheck, predictions, web

app = FastAPI(title="Crypto Forecast API")

app.include_router(healthcheck.router, prefix="/api/v1")
app.include_router(predictions.router, prefix="/api/v1")
app.include_router(web.router)

if __name__ == "__main__":
    import uvicorn
    from src.utils.config import settings
    uvicorn.run(app, host=settings.api_host, port=settings.api_port)
