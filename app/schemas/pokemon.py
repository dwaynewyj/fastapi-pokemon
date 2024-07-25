from pydantic import BaseModel

class Pokemon(BaseModel):
    id: int
    name: str
    base_experience: int
    height: int
    weight: int
    order: int
