from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_healthcheck():
    response = client.get("/api/v1/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

def test_prediction():
    response = client.get("/api/v1/predict?currency=BTC")
    assert response.status_code == 200
    assert "currency" in response.json()
    assert "chart" in response.json()