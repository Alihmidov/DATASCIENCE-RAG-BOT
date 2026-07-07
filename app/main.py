from fastapi import FastAPI 
from app.routes.api import router 

app = FastAPI(title="DATASCIENCE RAG BOT API")

app.include_router(router)

@app.get("/health_check")
def health_check():
    return {"status": "online", "message": "API is running!"}