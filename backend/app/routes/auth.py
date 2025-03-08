from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
import bcrypt

router = APIRouter(prefix="/auth", tags=["Authentication"])

users_db = {"user@example.com": {"password": bcrypt.hashpw(b"password", bcrypt.gensalt())}}

class LoginData(BaseModel):
    email: str
    password: str

@router.post("/login")
def login(data: LoginData):
    user = users_db.get(data.email)
    if not user or not bcrypt.checkpw(data.password.encode(), user["password"]):
        raise HTTPException(status_code=400, detail="Invalid credentials")
    return {"message": "Login successful"}

@router.post("/logout")
def logout():
    return {"message": "Logged out successfully"}
