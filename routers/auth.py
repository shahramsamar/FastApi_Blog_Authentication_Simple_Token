from fastapi import APIRouter, status, HTTPException, Query, Path, Form, Body, File, UploadFile, Depends
from fastapi.responses import JSONResponse
from typing import Optional, List
from sqlalchemy.orm import Session
from database.database import get_db, initiate_database
# from models import StudentModel
from auth.utils import authenticate_user, generate_token


from schemas.schema import LoginResponseSchema, LoginRequestSchema



router = APIRouter(prefix="/api/v1", tags=["Auth"])


@router.post("/login", response_model=LoginResponseSchema, status_code=status.HTTP_200_OK)
async def login(request: LoginRequestSchema, db: Session = Depends(get_db)):

    user = authenticate_user(
        db, username=request.username, password=request.password)
    token = generate_token(db, user)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="username or password doesn't match")
    return {
        "detail": "successfully logged in",
        "token": token,
        "user_id": user.id
    }


