from fastapi import APIRouter
from fastapi.responses import HTMLResponse
from pathlib import Path

router = APIRouter()

BASE_DIR = Path(__file__).resolve().parent.parent.parent
TEMPLATES_DIR = BASE_DIR / "templates"

@router.get("/", response_class=HTMLResponse)
def home():
    return (TEMPLATES_DIR / "index.html").read_text(encoding="utf-8")
