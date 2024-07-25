import os
import httpx
from app.schemas.pokemon import Pokemon
from typing import Dict, Any, Optional
from pydantic import BaseModel
from dotenv import load_dotenv

load_dotenv()

POKEAPI_POKEMON_URL = os.getenv("POKEAPI_POKEMON_URL", "https://pokeapi.co/api/v2/pokemon")
POKEAPI_BASE_URL = os.getenv("POKEAPI_BASE_URL", "https://pokeapi.co/api/v2/pokemon")

# Define a custom exception for API fetch errors
class PokemonAPIException(Exception):
    def __init__(self, message: str):
        self.message = message
        super().__init__(self.message)

async def get_pokemon_by_id(pokemon_id: int) -> Optional[Pokemon]:
    if pokemon_id <= 0:
        raise ValueError("Pokemon ID must be a positive integer.")
        
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{POKEAPI_BASE_URL}/{pokemon_id}")
        if response.status_code != 200:
            return None  # Consider logging the error or raise a custom exception
        data = response.json()

        # Validate response data
        if not all(key in data for key in ["id", "name", "base_experience", "height", "weight", "order"]):
            raise ValueError("Invalid data format received from PokeAPI.")

        return Pokemon(
            id=data["id"],
            name=data["name"],
            base_experience=data["base_experience"],
            height=data["height"],
            weight=data["weight"],
            order=data["order"]
        )

async def get_pokemon_by_name(pokemon_name: str) -> Optional[Pokemon]:
    if not pokemon_name:
        raise ValueError("Pokemon name must be a non-empty string.")

    async with httpx.AsyncClient() as client:
        response = await client.get(f"{POKEAPI_BASE_URL}/{pokemon_name}")
        if response.status_code != 200:
            return None  # Consider logging the error or raise a custom exception
        data = response.json()

        # Validate response data
        if not all(key in data for key in ["id", "name", "base_experience", "height", "weight", "order"]):
            raise ValueError("Invalid data format received from PokeAPI.")

        return Pokemon(
            id=data["id"],
            name=data["name"],
            base_experience=data["base_experience"],
            height=data["height"],
            weight=data["weight"],
            order=data["order"]
        )

async def fetch_pokemon_details(name: str, max_moves: int) -> Dict[str, Any]:
    if not name:
        raise ValueError("Pokemon name must be a non-empty string.")
    if max_moves <= 0:
        raise ValueError("max_moves must be a positive integer.")
    
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{POKEAPI_POKEMON_URL}/{name}")
        if response.status_code != 200:
            raise PokemonAPIException(f"Failed to fetch pokemon details for {name}. Status code: {response.status_code}")
        data = response.json()

        # Validate response data
        if not all(key in data for key in ["name", "abilities", "base_experience", "forms", "height", "weight", "moves", "sprites"]):
            raise ValueError("Invalid data format received from PokeAPI.")

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
