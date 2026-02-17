from sqlalchemy import create_engine
from os import getenv
from sqlalchemy.orm import sessionmaker, declarative_base, Session
from dotenv import load_dotenv
from typing import Generator

load_dotenv()

DATABASE_URL = getenv("DATABASE_URL")

print (f"DEBUG: Connecting to {DATABASE_URL}")

engine = create_engine(DATABASE_URL, pool_pre_ping=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db() -> Generator[Session, None, None]:
    db = SessionLocal()  
    try:                 
        yield db         
    finally:         
        db.close()      

Base = declarative_base()