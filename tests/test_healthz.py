from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health_check():
    response = client.get("/v1/healthz")
    assert response.status_code == 200
    assert response.json() == {"message": "Ok", "status": 200}
