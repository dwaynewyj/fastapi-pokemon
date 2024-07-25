from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_read_pokemon():
    response = client.get("/v1/pokemon/1")
    assert response.status_code == 200
    assert response.json()["name"] == "bulbasaur"

def test_read_pokemon_by_name():
    response = client.get("/v1/pokemon/name/bulbasaur")
    assert response.status_code == 200
    assert response.json()["id"] == 1

def test_read_pokemon_not_found():
    response = client.get("/v1/pokemon/999999")
    assert response.status_code == 404

def test_get_pokemon_details():
    response = client.post("/v1/pokemon", json={"name": "bulbasaur", "max_moves": 5})
    assert response.status_code == 200
    json_response = response.json()
    assert json_response["name"] == "bulbasaur"
    assert len(json_response["moves"]) == 5
    assert all(k in json_response["sprites"] for k in ["back_default", "back_shiny", "front_default", "front_shiny"])

def test_get_pokemon_invalid_name():
    response = client.post("/v1/pokemon", json={"name": "InvalidName", "max_moves": 5})
    assert response.status_code == 422

def test_get_pokemon_invalid_max_moves():
    response = client.post("/v1/pokemon", json={"name": "bulbasaur", "max_moves": -1})
    assert response.status_code == 422  # Unprocessable Entity

def test_get_pokemon_name_not_lowercase():
    response = client.post("/v1/pokemon", json={"name": "Bulbasaur", "max_moves": 5})
    assert response.status_code == 422  # Unprocessable Entity