from fastapi import FastAPI
from app.routers import pokemon, healthz, species

app = FastAPI()

app.include_router(healthz.router, prefix="/v1", tags=["healthz"])
app.include_router(pokemon.router, prefix="/v1", tags=["pokemon"])
app.include_router(species.router, prefix="/v1", tags=["species"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the Pokemon API"}
