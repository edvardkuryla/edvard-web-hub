from sqlalchemy.orm import Session
from src.models import models
from src.schemas import schemas
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["argon2"], deprecated="auto")

def verify_password(plain_password: str, password_hashed: str) -> bool:
    return pwd_context.verify(plain_password, password_hashed)

def get_password_hash(password: str):
    return pwd_context.hash(password)

def get_user_by_email(db: Session, email:str):
    return db.query(models.User).filter(models.User.email == email).first()

def create_user(db: Session, user: schemas.UserCreate):
    existing = get_user_by_email(db, user.email)
    if existing:
        return None
    hashed = get_password_hash(user.password)

    db_user = models.User(name=user.name, email=user.email, password_hash=hashed)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_refresh_token(db: Session, token: str):
    return db.query(models.RefreshToken).filter(models.RefreshToken.token == token).first()

def clear_all_user_refresh_tokens(db: Session, user_id: int):
    db.query(models.RefreshToken).filter(models.RefreshToken.user_id == user_id).delete()
    db.commit()

def add_refresh_token(db: Session, token: str, user_id: int):
    db_token = models.RefreshToken(token=token, user_id=user_id)
    db.add(db_token)
    db.commit()