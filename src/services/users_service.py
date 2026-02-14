from ..config.security import verify_password, create_access_token, create_refresh_token, hash_passoword
from src.models.models import User, RefreshToken
from ..config.database.database import SessionLocal

def authenticate_user(email: str, password, str):
    db = SessionLocal()
    user = db.query(User).filter(User.email == email).first()
    db.close()
    if not user:
        return None
    if not verify_password(password, user.password_hash):
        return None
    return user

def login_user(user: User):
    access = create_access_token({"sub": str(user.id), "role": user.role})
    refresh = create_refresh_token({"sub": str(user.id), "role": user.role})
    return access, refresh

def save_refresh_token(token: str, user_id: int):
db = SessionLocal()
rt = RefreshToken(token=token, user_id=user_id)
db.add(rt)
db.commit()
db.close()