from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.models.user import User
from app.models.todo import Todo
from ..database import get_db

router = APIRouter()

@router.post("/todos/")
def create_todo(title: str, description: str, completed: bool, db: Session = Depends(get_db)):
    todo = Todo(title=title, description=description, completed=completed)
    db.add(todo)
    db.commit()
    db.refresh(todo)
    return todo


@router.get("/todos/")
def read_todos(db: Session = Depends(get_db)):
    todos = db.query(Todo).all()
    return todos