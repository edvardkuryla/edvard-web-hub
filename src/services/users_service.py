from config.security import verify_password, create_access_token, create_refresh_token, hash_password
from src.models.models import User, RefreshToken
from config.database.database import SessionLocal

def authenticate_user(email: str, password: str):  # Исправлено: двоеточие вместо запятой
    db = SessionLocal()
    try:
        user = db.query(User).filter(User.email == email).first()
        if not user:
            return None
        if not verify_password(password, user.password_hash):
            return None
        return user
    finally:
        db.close()

def login_user(user: User):
    access = create_access_token({"sub": str(user.id), "role": user.role})
    refresh = create_refresh_token({"sub": str(user.id), "role": user.role})
    return access, refresh

def save_refresh_token(token: str, user_id: int):
    db = SessionLocal()
    try:
        # Добавлены отступы (4 пробела)
        rt = RefreshToken(token=token, user_id=user_id)
        db.add(rt)
        db.commit()
    except Exception as e:
        db.rollback()
        raise e
    finally:
        db.close()
