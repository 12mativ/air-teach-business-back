from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from .utils import (
    db, authenticate_user, create_access_token, get_current_active_user,
    get_password_hash
)
from datetime import timedelta
import os
from dotenv import load_dotenv
from .models import UserCreate, Token, User, UserInDB


auth_router = APIRouter(
  prefix="/auth",
  tags=["auth"]
)

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 15))


@auth_router.post("/login", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    print(form_data)
    user = authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code = status.HTTP_401_UNAUTHORIZED,
                            detail = "Incorrect username or password", headers = {"WWW-Authenticate": "Bearer"})
    access_token_expires = timedelta(minutes = ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta = access_token_expires)
    return {"access_token": access_token, "token_type": "bearer"}

@auth_router.get("/users/me/", response_model = User)
async def read_users_me(current_user: User = Depends(get_current_active_user)):
    return current_user

@auth_router.post("/register", response_model=User)
async def register_user(user: UserCreate):
    if user.username in db:
        raise HTTPException(status_code = 400, detail="Username already registered")

    hashed_password = get_password_hash(user.password)
    db_user = UserInDB(
        username = user.username,
        email = user.email,
        full_name = user.full_name,
        hashed_password = hashed_password,
        disabled = False
    )
    db[user.username] = db_user.dict()
    return db_user