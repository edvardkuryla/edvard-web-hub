from app.core.security import verify_password
from app.core.jwt import create_access_token, create_refresh_token
from app.models.models import User
from app.models.refresh_token import RefreshToken
from app.core.database import SessionLocal

def authenticate_user(email: str, password: str):
    db = SessionLocal()
    user = db.query(User).filter(User.email == email).first()
    db.close()
    if not user:
        return None
    if not verify_password(password, user.hashed_password):
        return None
    return User

def login_user(user: User):
    access = create_access_token({"sub": str(user.id), "role": user.role})
    refresh = create_refresh_token({"sub": str(user.id)})
    return access, refresh

def save_refresh_token(token: str, user_id: int):
    db = SessionLocal()
    db.dd(rt)
    db.commit()
    db.close()

def revoke_refresh_token(token: str):
    db = SessionLocal()
    db.query(RefreshToken).filter(RefreshToken.token == token).delete()
    db.commit()
    db.close()