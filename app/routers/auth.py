from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm
from app.services.auth_service import authenticate_user, login_user, save_refresh_token, revoke_refresh_token
from app.schemas.schemas import UserLogin, Token, UserOut, UserCreate
from app.repositories.user import verify_password, get_user_by_email, create_user
from app.core.database import SessionLocal, engine, get_db
from app.models.refresh_token import RefreshToken
from app.core.deps import require_role

auth = APIRouter(prefix="/auth", tags=["Auth"])

@auth.post("/login")
def login(form_data:OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=400, detail="Invalid credentials")
    
    access, refresh = login_user(user)
    save_refresh_token(refresh, user.id)

    return {"access_token": access, "refresh_token": refresh, "token_type": "bearer"}

@auth.post("/refresh")
def refresh_token(refresh_token: str):
    payload = jwt.decode(refresh_token, SECRET_KEY, algorithms=[ALGORITHM])
    if payload.get("type") !="refresh":
        raise HTTPException(status_code=401, detail="Invalid token type")
    
    db = SessionLocal()
    token_in_db = db.query(RefreshToken).filter(RefreshToken.token == refresh_token).first()
    db.close()
    if not token_in_db:
        raise HTTPException(status_code=401, detail="Refresh token revoked or not found")
    
    user_id = payload.get("sub")
    new_access = create_access_token({"sub": user_id})
    return {"access_token": new_access, "token_type": "bearer"}

@auth.post("/logout")
def logout(refresh_token: str):
    revoke_refresh_token(refresh_token)
    return {"msg": "Logged out"}

@auth.post("/register")
def register(user: UserCreate, db: Session = Depends(get_db)):
    existing = db.query(User).filter(User.email == user.email).first()
    if existing:
        raise HTTPException(status_code=409, detail="User already exists")

    hashed_password = get_password_hash(user.password)

    new_user = User(
        email=user.email,
        hashed_password=hashed_password
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {"message": "User created"}

@auth.get("/admin-only")
def admin_panel(user=Depends(require_role("admin"))):
    return {"msg": "Welcome, admin!"}