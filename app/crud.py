from sqlalchemy.orm import Session
from app.models import Todo, User
from app.schemas import TodoCreate, UserCreate
from app.auth import get_password_hash, get_current_user_id
from fastapi import Depends

# 사용자 생성
def create_user(db: Session, user: UserCreate):
    hashed_password = get_password_hash(user.password)
    db_user = User(name=user.name, email=user.email, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# 새로운 Todo 추가 (JWT에서 user_id 추출)
def create_todo(db: Session, todo: TodoCreate, user_id: int = Depends(get_current_user_id)):
    db_todo = Todo(**todo.dict(), user_id=user_id)
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo

# Todo 목록 조회 (JWT에서 user_id 추출)
def get_todos(db: Session, user_id: int = Depends(get_current_user_id)):
    return db.query(Todo).filter(Todo.user_id == user_id).all()
