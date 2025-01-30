from fastapi import FastAPI
from src.api.routes import healthcheck, predictions

app = FastAPI()
app.include_router(healthcheck.router)
app.include_router(predictions.router, prefix="/api/v1")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)