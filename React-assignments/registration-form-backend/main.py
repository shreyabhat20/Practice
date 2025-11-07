from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from sqlalchemy.exc import IntegrityError
from models import SessionLocal, User 

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class UserCreate(BaseModel):
    username: str
    password: str

@app.post("/register")
def register(user: UserCreate):
    db = SessionLocal()
    try:
        new_user = User(username=user.username, password=user.password)
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return {"success": True, "message": "User registered successfully"}
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=400, detail="Username already exists")
    finally:
        db.close()
