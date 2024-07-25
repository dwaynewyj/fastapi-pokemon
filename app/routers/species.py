from fastapi import APIRouter, Query, HTTPException
from typing import List, Optional
from app.services.species_service import fetch_species_details

router = APIRouter()

@router.get("/species")
async def get_species(count: int = Query(20, gt=0, le=100), index: int = Query(0, ge=0)):
    try:
        species_list = await fetch_species_details(count, index)
        return {"species": species_list}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
