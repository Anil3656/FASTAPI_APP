# STEP 5 — schemas.py (Pydantic Models)

# IMPORTANT:
# Models = DB structure
# Schemas = Request/Response validation

from pydantic import BaseModel, Field

class UserCreate(BaseModel): # This is the schema for the request body when creating/updating a user
    name: str
    email: str
    password: str = Field(min_length=6, max_length=72)
    
class UserLogin(BaseModel): # This is the schema for the request body when logging in
    email: str
    password: str

class UserResponse(BaseModel): # This is the schema for the response when we return user data
    id: int
    name: str
    email: str

    class Config:
        model_config = {
                        "from_attributes": True # This allows Pydantic to read data from SQLAlchemy models
                        }