from fastapi import APIRouter, HTTPException, status, Depends
from pydantic import BaseModel, EmailStr
from db import get_connection
from auth import hash_password, verify_password, create_access_token

router = APIRouter()

class UserRegister(BaseModel):
    username: str
    email: EmailStr
    password: str

class UserLogin(BaseModel):
    email: EmailStr
    password: str

@router.post("/register")
def register(user: UserRegister):
    conn = get_connection()
    cur = conn.cursor()
    try:
        hashed_pw = hash_password(user.password)
        cur.execute(
            "INSERT INTO users (username, email, password) VALUES (%s, %s, %s) RETURNING id",
            (user.username, user.email, hashed_pw)
        )
        conn.commit()
        return {"msg": "User registered successfully"}
    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=400, detail="Email or username already exists")
    finally:
        cur.close()
        conn.close()

@router.post("/login")
def login(user: UserLogin):
    conn = get_connection()
    cur = conn.cursor()
    try:
        cur.execute("SELECT * FROM users WHERE email=%s", (user.email,))
        db_user = cur.fetchone()
        if not db_user or not verify_password(user.password, db_user["password"]):
            raise HTTPException(status_code=401, detail="Invalid credentials")
        token = create_access_token({"sub": db_user["email"]})
        return {"access_token": token, "token_type": "bearer"}
    finally:
        cur.close()
        conn.close()
