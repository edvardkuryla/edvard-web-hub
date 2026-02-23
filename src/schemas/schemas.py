from pyclbr import Class
from pydantic import BaseModel, Field, EmailStr
from decimal import Decimal

class UserCreate(BaseModel):
    name: str = Field(..., strip_whitespace=True, min_length=2, description="The name must be longer than 2 characters")
    email: EmailStr
    password: str = Field(..., strip_whitespace=True, min_length=8, description="Password must be longer than 8 characters")

class UserLogin(BaseModel):
    email: EmailStr
    password: str = Field(..., strip_whitespace=True, min_length=8, description="Password must be longer than 8 characters")\
    
class UserOut(BaseModel):
    id: int
    email: EmailStr
    model_config = {"from_attributes": True}

class Config:
    from_attributes = True
    
class Token(BaseModel):
    access_token: str
    token_type: str

class RefreshRequest(BaseModel):
    refresh_token: str

class BalanceChange(BaseModel):
    amount: Decimal = Field(gt=0)

class BalanceResponse(BaseModel):
    balance: Decimal