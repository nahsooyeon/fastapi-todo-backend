from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from models import User
from database import get_db

router = APIRouter()

@router.post("/auth/google")
async def google_login(google_id: str, email: str, name: str, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.google_id == google_id).first()
    if not user:
        # 사용자가 없다면 새로 등록
        user = User(google_id=google_id, email=email, name=name)
        db.add(user)
        db.commit()
        db.refresh(user)
    return user
