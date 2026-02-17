from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm
from config.database.database import get_db
from src.services.users_service import authenticate_user, login_user, save_refresh_token, register_user
from src.schemas.schemas import UserOut, UserCreate

auth = APIRouter(prefix="/auth", tags=["Auth"])

@auth.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    # ДОБАВИЛИ db первым аргументом
    user = authenticate_user(db, form_data.username, form_data.password)
    
    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")
        
    access, refresh = login_user(user)
    
    # ДОБАВИЛИ db первым аргументом
    save_refresh_token(db, refresh, user.id)
    
    return {"access_token": access, "refresh_token": refresh, "token_type": "bearer"}

@auth.post("/register", response_model=UserOut)
def register(data: UserCreate, db: Session = Depends(get_db)):
    # ИСПРАВИЛИ: передаем db и весь объект data целиком
    user = register_user(db, data)
    return user