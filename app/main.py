from fastapi import FastAPI
from .database import Base, engine
from .routes import todo

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(todo.router, prefix="/api/v1")
