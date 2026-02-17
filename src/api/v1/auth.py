from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm
from config.database.database import get_db
from src.services.users_service import login_user
from src.services.users_service import authenticate_user, login_user, save_refresh_token

auth = APIRouter(prefix="/auth", tags=["Auth"])
@auth.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    access, refresh = login_user(user)
    save_refresh_token(refresh, user.id)
    return {"access_token": access, "refresh_token": refresh, "token_type": "bearer"}