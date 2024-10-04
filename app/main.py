from fastapi import FastAPI
from app.api import router as api_router  # api.py에서 라우터 가져오기

app = FastAPI()

# 라우터 등록 (api.py에 정의된 모든 라우터 등록)
app.include_router(api_router)

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}
