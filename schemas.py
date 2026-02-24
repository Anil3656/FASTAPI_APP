# STEP 5 — schemas.py (Pydantic Models)

# IMPORTANT:
# Models = DB structure
# Schemas = Request/Response validation

from pydantic import BaseModel

class UserCreate(BaseModel):
    name: str
    email: str
    password: str

class UserResponse(BaseModel):
    id: int
    name: str
    email: str

    class Config:
        model_config = {
                        "from_attributes": True
                        }