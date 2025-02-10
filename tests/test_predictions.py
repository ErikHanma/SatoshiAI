from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_prediction():
    response = client.get("/api/v1/predict?currency=BTC")
    assert response.status_code == 200
    json_data = response.json()
    assert "currency" in json_data
    assert "dates" in json_data
    assert "values" in json_data
