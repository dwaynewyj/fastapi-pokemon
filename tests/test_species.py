from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_get_species():
    response = client.get("/v1/species")
    assert response.status_code == 200
    assert "species" in response.json()
    assert len(response.json()["species"]) <= 20

def test_get_species_with_count():
    response = client.get("/v1/species?count=10")
    assert response.status_code == 200
    assert "species" in response.json()
    assert len(response.json()["species"]) <= 10

def test_get_species_with_count_and_index():
    response = client.get("/v1/species?count=10&index=10")
    assert response.status_code == 200
    assert "species" in response.json()
    assert len(response.json()["species"]) <= 10

def test_get_species_invalid_count():
    response = client.get("/v1/species?count=-1")
    assert response.status_code == 422  # Unprocessable Entity

def test_get_species_invalid_index():
    response = client.get("/v1/species?index=-1")
    assert response.status_code == 422  # Unprocessable Entity
