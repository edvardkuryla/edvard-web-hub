from sqlalchemy.orm import Session

from app.users.repository import get_user_by_email, create_user
from app.users.repository import save_refresh_token, get_refresh_token, revoke_refresh_token
from app.core.security import verify_password, hash_password, create_access_token, create_refresh_token, decode_token
from app.schemas.schemas import UserCreate
from app.models.models import User

def register_user(db: Session, user_data: UserCreate):
    existing_user = get_user_by_email(db, user_data.email)
    if existing_user:
        raise ValueError("User already exists")
    password_hash = hash_password(user_data.password)
    user = create_user(db=db, name=user_data.name, email=user_data.email, password_hash=password_hash)
    return user

def login_user(db: Session, email: str, password: str):
    user = get_user_by_email(db, email)
    if not user:
        raise ValueError("Invalid credentials")
    access_token = create_access_token({"sub": str(user.id)})
    refresh_token = create_refresh_token({"sub": str(user.id)})
    save_refresh_token(db, refresh_token, user.id)
    return {"access_token": access_token, "refresh_token": refresh_token, "token_type": "bearer"}

