from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PAsswordBearer
from jose import jwt, JWTError
from config import settings

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")

def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORISED, detail="Invalid or expired token")
    user_id: int | None = payload.get("sub")
    role: str | None = payload.get("role") ## Need to finish