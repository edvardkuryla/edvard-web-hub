from fastapi import fastapi
from .config.database.database import Base. engine
from models.models import User

app = FastAPI()