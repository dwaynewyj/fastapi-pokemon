from fastapi import APIRouter

router = APIRouter()

@router.get("/healthz")
async def health_check():
    return {"message": "Ok", "status": 200}
