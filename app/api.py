from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List  # List를 추가합니다.
from app import crud, schemas, auth
from app.database import get_db

router = APIRouter()

@router.post("/users/", response_model=schemas.UserOut)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db, user)

@router.post("/todos/", response_model=schemas.TodoOut)
def create_todo(todo: schemas.TodoCreate, db: Session = Depends(get_db), user_id: int = Depends(auth.get_current_user_id)):
    return crud.create_todo(db, todo, user_id)

@router.get("/todos/", response_model=List[schemas.TodoOut])  # 여기도 List를 사용
def get_todos(db: Session = Depends(get_db), user_id: int = Depends(auth.get_current_user_id)):
    return crud.get_todos(db, user_id)
