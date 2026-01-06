from fastapi import FastAPI
from src.api.routes import router

app = FastAPI(
    title="Habitos API",
    version="0.1.0"
)

app.include_router(router)
