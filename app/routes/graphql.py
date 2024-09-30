from fastapi import Depends
from sqlalchemy.orm import Session
from models import Todo
from database import get_db

@router.post("/graphql")
async def get_todos(user_id: int, db: Session = Depends(get_db)):
    todos = db.query(Todo).filter(Todo.user_id == user_id).all()
    return todos
