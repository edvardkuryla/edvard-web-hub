from pyclbr import Class
from pydantic import BaseModel, EmailStr, Field


class UserCreate(BaseModel):
    name: str = Field(..., strip_whitespace=True, min_length=2,description="The name must be longer than 2 characters long")
    email: EmailStr
    password: str = Field(..., strip_whitespace=True, min_length=8, description="The password must be longer than 8 characteres long")

class UserLogin(BaseModel):
    email: EmailStr
    password: str = Field(..., strip_whitespace=True, min_length=8, description="The password must be longer than 8 characteres long")

class UserOut(BaseModel):
    id: int
    email: EmailStr

class Config:
    from_attributes = True
class Token(BaseModel):
    access_token: str
    token_type: str
    