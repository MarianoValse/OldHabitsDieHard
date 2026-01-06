from fastapi import APIRouter
from pathlib import Path

from src.loaders.excel_loader import ExcelLoader

BASE_DIR = Path(__file__).resolve().parent.parent.parent
DATA_DIR = BASE_DIR / "data"

router = APIRouter()


@router.get("/habitos")
def listar_habitos():
    loader = ExcelLoader(DATA_DIR)
    habitos = loader.cargar_habitos()

    return [
        {
            "id": h.id,
            "nombre": h.nombre,
            "activo": h.activo,
            "dificultad": h.dificultad.nombre if h.dificultad else None,
            "peso": h.peso.nombre if h.peso else None
        }
        for h in habitos
        if h.activo
    ]
