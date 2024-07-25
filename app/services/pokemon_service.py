import httpx
from app.schemas.pokemon import Pokemon
from typing import Dict, Any

POKEAPI_POKEMON_URL = "https://pokeapi.co/api/v2/pokemon"
POKEAPI_BASE_URL = "https://pokeapi.co/api/v2/pokemon"

async def get_pokemon_by_id(pokemon_id: int) -> Pokemon:
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{POKEAPI_BASE_URL}/{pokemon_id}")
        if response.status_code != 200:
            return None
        data = response.json()
        return Pokemon(
            id=data["id"],
            name=data["name"],
            base_experience=data["base_experience"],
            height=data["height"],
            weight=data["weight"],
            order=data["order"]
        )

async def get_pokemon_by_name(pokemon_name: str) -> Pokemon:
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{POKEAPI_BASE_URL}/{pokemon_name}")
        if response.status_code != 200:
            return None
        data = response.json()
        return Pokemon(
            id=data["id"],
            name=data["name"],
            base_experience=data["base_experience"],
            height=data["height"],
            weight=data["weight"],
            order=data["order"]
        )

async def fetch_pokemon_details(name: str, max_moves: int) -> Dict[str, Any]:
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{POKEAPI_POKEMON_URL}/{name}")
        if response.status_code != 200:
            raise Exception("Failed to fetch pokemon details from PokeAPI")
        data = response.json()
        
        moves = [move["move"]["name"] for move in data["moves"][:max_moves]]
        
        sprites = {k: v for k, v in data["sprites"].items() if v is not None}
        
        return {
            "name": data["name"],
            "abilities": [ability["ability"]["name"] for ability in data["abilities"]],
            "base_experience": data["base_experience"],
            "forms": [form["name"] for form in data["forms"]],
            "height": data["height"],
            "weight": data["weight"],
            "moves": moves,
            "sprites": sprites
        }