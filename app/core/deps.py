from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from app.core.config import settings

oauth2_scheme = Oauth2PasswordBearer(tokenUrl="auth/login")

def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORISED, detail="Invalid or expired token")
    user_id: int | None = payload.get("sub")
    role: str | None = payload.get("role")
    if user_id is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORISED, detail="Invalid tokenpayload")
    return {"user_id": user_id, "role": role}
def require_role(required_role: str):
    def role_checker(user: dict = Depends(get_current_user)):
        if user["role"] != required_role:
            raise HTTPException(status_code=status.HTTP_403_FROBIDDEN, detail="Forbidden")
        return user
    return role_checker