
from fastapi import APIRouter, HTTPException, Body
from pydantic import BaseModel, Field, validator
from app.schemas.pokemon import Pokemon
from app.services.pokemon_service import fetch_pokemon_details, get_pokemon_by_name, get_pokemon_by_id
from typing import Dict, Any


router = APIRouter()

class PokemonRequest(BaseModel):
    name: str = Field(..., example="bulbasaur")
    max_moves: int = Field(..., gt=0, example=5)
    
    @validator('name')
    def name_must_be_lowercase(cls, v):
        if not v.islower():
            raise ValueError('name must be lowercase')
        return v

@router.post("/pokemon")
async def get_pokemon_details(request: PokemonRequest = Body(...)) -> Dict[str, Any]:
    try:
        pokemon_details = await fetch_pokemon_details(request.name, request.max_moves)
        return pokemon_details
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@router.get("/pokemon/{pokemon_id}", response_model=Pokemon)
async def read_pokemon(pokemon_id: int):
    pokemon = await get_pokemon_by_id(pokemon_id)
    if not pokemon:
        raise HTTPException(status_code=404, detail="Pokemon not found")
    return pokemon

@router.get("/pokemon/name/{pokemon_name}", response_model=Pokemon)
async def read_pokemon_by_name(pokemon_name: str):
    pokemon = await get_pokemon_by_name(pokemon_name)
    if not pokemon:
        raise HTTPException(status_code=404, detail="Pokemon not found")
    return pokemon

