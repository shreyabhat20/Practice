from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker
from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
DATABASE_URL = "postgresql+psycopg2://postgres:P%40ssword%401025@localhost:5432/registration_db"

engine = create_engine(DATABASE_URL)
Base = declarative_base()
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
db = SessionLocal()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    password = Column(String)

Base.metadata.create_all(bind=engine)

class UserCreate(BaseModel):
    username: str
    password: str

@app.post("/register")
def register(user: UserCreate):
    try:
        new_user = User(username=user.username, password=user.password)
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return {"success": True, "message": "User registered successfully"}

    except IntegrityError:
        db.rollback()  
        raise HTTPException(status_code=400, detail="Username already exists")
