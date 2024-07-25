import os
import httpx
from typing import List, Dict, Any
from pydantic import BaseModel, ValidationError
from dotenv import load_dotenv

load_dotenv()

POKEAPI_SPECIES_URL = os.getenv("POKEAPI_SPECIES_URL", "https://pokeapi.co/api/v2/pokemon-species")
POKEMON_IMAGE_URL = os.getenv("POKEMON_IMAGE_URL", "https://assets.pokemon.com/assets/cms2/img/pokedex/full/{:03}.png")

# Define a custom exception for API fetch errors
class PokemonAPIException(Exception):
    def __init__(self, message: str):
        self.message = message
        super().__init__(self.message)

# Define a model to validate species data
class SpeciesDetail(BaseModel):
    id: int
    image: str
    name: str
    base_happiness: int
    capture_rate: int
    colors: List[str]
    growth_rates: List[str]
    habitats: List[str]
    is_legendary: str
    egg_groups: List[str]
    shapes: List[str]

async def fetch_species_details(count: int, index: int) -> List[Dict[str, Any]]:
    if count <= 0:
        raise ValueError("Count must be a positive integer.")
    if index < 0:
        raise ValueError("Index must be a non-negative integer.")
    
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{POKEAPI_SPECIES_URL}?offset={index}&limit={count}")
        if response.status_code != 200:
            raise PokemonAPIException(f"Failed to fetch species list from PokeAPI. Status code: {response.status_code}")
        
        species_data = response.json()
        
        species_list = []
        for species in species_data["results"]:
            species_details = await fetch_species_detail(client, species["url"])
            species_list.append(species_details)
        
        return species_list

async def fetch_species_detail(client: httpx.AsyncClient, url: str) -> Dict[str, Any]:
    if not url:
        raise ValueError("URL must be a non-empty string.")
    
    response = await client.get(url)
    if response.status_code != 200:
        raise PokemonAPIException(f"Failed to fetch species detail from PokeAPI. Status code: {response.status_code}")
    
    data = response.json()

    # Validate the structure of the response data
    try:
        species_detail = SpeciesDetail(
            id=data["id"],
            image=POKEMON_IMAGE_URL.format(data["id"]),
            name=data["name"].lower(),
            base_happiness=data["base_happiness"],
            capture_rate=data["capture_rate"],
            colors=[data["color"]["name"].lower()],
            growth_rates=[data["growth_rate"]["name"].lower()],
            habitats=[data["habitat"]["name"].lower()] if data["habitat"] else [],
            is_legendary=str(data["is_legendary"]).lower(),
            egg_groups=[egg_group["name"].lower() for egg_group in data["egg_groups"]],
            shapes=[data["shape"]["name"].lower()] if data["shape"] else []
        )
    except KeyError as e:
        raise ValueError(f"Missing expected key: {e}")

    return species_detail.dict()
