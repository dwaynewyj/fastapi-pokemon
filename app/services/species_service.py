import httpx
from typing import List, Dict, Any

POKEAPI_SPECIES_URL = "https://pokeapi.co/api/v2/pokemon-species"
POKEMON_IMAGE_URL = "https://assets.pokemon.com/assets/cms2/img/pokedex/full/{:03}.png"

async def fetch_species_details(count: int, index: int) -> List[Dict[str, Any]]:
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{POKEAPI_SPECIES_URL}?offset={index}&limit={count}")
        if response.status_code != 200:
            raise Exception("Failed to fetch species list from PokeAPI")
        species_data = response.json()
        
        species_list = []
        for species in species_data["results"]:
            species_details = await fetch_species_detail(client, species["url"])
            species_list.append(species_details)
        
        return species_list

async def fetch_species_detail(client: httpx.AsyncClient, url: str) -> Dict[str, Any]:
    response = await client.get(url)
    if response.status_code != 200:
        raise Exception("Failed to fetch species detail from PokeAPI")
    data = response.json()

    species_id = data["id"]
    image_url = POKEMON_IMAGE_URL.format(species_id)
    
    return {
        "id": species_id,
        "image": image_url,
        "name": data["name"].lower(),
        "base_happiness": data["base_happiness"],
        "capture_rate": data["capture_rate"],
        "colors": [data["color"]["name"].lower()],
        "growth_rates": [data["growth_rate"]["name"].lower()],
        "habitats": [data["habitat"]["name"].lower()] if data["habitat"] else [],
        "is_legendary": str(data["is_legendary"]).lower(),
        "egg_groups": [egg_group["name"].lower() for egg_group in data["egg_groups"]],
        "shapes": [data["shape"]["name"].lower()] if data["shape"] else []
    }
