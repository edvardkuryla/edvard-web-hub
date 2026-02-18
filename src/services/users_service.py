from sqlalchemy.orm import Session
from fastapi import HTTPException
# Убрали лишний verify_password здесь
from config.security import create_access_token, create_refresh_token 
import src.repositories.users as repo 
from src.models.models import RefreshToken
from src.schemas.schemas import UserCreate # Импортируем схему для типизации
from config.config import settings

def authenticate_user(db: Session, email: str, password: str):
    user = repo.get_user_by_email(db, email)
    if not user:
        return None
    if not repo.verify_password(password, user.password_hash):
        return None
    return user

def login_user(user):
    access = create_access_token({"sub": str(user.id), "role": user.role})
    refresh = create_refresh_token({"sub": str(user.id), "role": user.role})
    return access, refresh

def save_refresh_token(db: Session, token: str, user_id: int):
    rt = RefreshToken(token=token, user_id=user_id)
    db.add(rt)
    db.commit()

def register_user(db: Session, user_data: UserCreate):
    existing_user = repo.get_user_by_email(db, user_data.email)
    if existing_user:
        raise HTTPException(status_code=400, detail="User already exists")

    user = repo.create_user(db, user_data)
    return user

def refresh_access_token(db: Session, refresh_token: str):
    # Ищем в базе
    db_token = repo.get_refresh_token(db, refresh_token)
    if not db_token:
        return None
    
    # Генерируем новый access
    user = db_token.user
    new_access = create_access_token({"sub": str(user.id), "role": user.role})
    return {"access_token": new_access, "token_type": "bearer"}