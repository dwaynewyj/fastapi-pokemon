from fastapi import FastAPI
from app.routers import pokemon, healthz, species

app = FastAPI()

"""
**Healthz Router**

Endpoints for checking the health of the API.

- **GET /v1/healthz**: Returns the health status of the API.
    - **Response**: A JSON object with a status message, e.g., `{"status": "OK"}`.
"""
app.include_router(healthz.router, prefix="/v1", tags=["healthz"])

"""
**Pokemon Router**

Endpoints for interacting with Pokemon data.

- **GET /v1/pokemon**: Retrieve a list of Pokemon.
    - **Query Parameters**:
        - `skip` (int, optional): Number of items to skip (default 0).
        - `limit` (int, optional): Maximum number of items to return (default 10, max 100).
    - **Response**: A list of Pokemon objects.

- **GET /v1/pokemon/{pokemon_id}**: Retrieve details of a specific Pokemon by ID.
    - **Path Parameters**:
        - `pokemon_id` (int): The ID of the Pokemon.
    - **Response**: A JSON object with details of the specified Pokemon.

- **POST /v1/pokemon**: Create a new Pokemon entry.
    - **Request Body**: A Pokemon object with required fields.
    - **Response**: The created Pokemon object with an ID.
"""
app.include_router(pokemon.router, prefix="/v1", tags=["pokemon"])

"""
**Species Router**

Endpoints for interacting with Pokemon species data.

- **GET /v1/species**: Retrieve a list of Pokemon species.
    - **Query Parameters**:
        - `skip` (int, optional): Number of items to skip (default 0).
        - `limit` (int, optional): Maximum number of items to return (default 10, max 100).
    - **Response**: A list of Pokemon species objects.

- **GET /v1/species/{species_id}**: Retrieve details of a specific Pokemon species by ID.
    - **Path Parameters**:
        - `species_id` (int): The ID of the Pokemon species.
    - **Response**: A JSON object with details of the specified Pokemon species.
"""
app.include_router(species.router, prefix="/v1", tags=["species"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the Pokemon API"}
