from fastapi import fastapi
from .database.database import Base, engine
from .api.users import auth
from .models.models import User
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.app_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(auth)