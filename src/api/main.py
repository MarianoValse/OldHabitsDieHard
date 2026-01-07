from fastapi import FastAPI
from src.api.routes import router
from src.services.db import init_db
# from src.api.views import router as views_router

app = FastAPI(
    title="Habitos API",
    version="0.1.0"
)

@app.on_event("startup")
def startup():
    init_db()

app.include_router(router)

# app.include_router(views_router)
