from sqlalchemy import Column, Integer, String
from app.core.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=False, nullable=False, index=True)
    email = Column(String, unique=False, nullable=False, index=True)
    password_hash = Column(String, nullable=False)