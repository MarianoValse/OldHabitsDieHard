from fastapi import APIRouter
from pathlib import Path
from datetime import date
from pydantic import BaseModel
from src.services.db import get_connection

from src.loaders.excel_loader import ExcelLoader

BASE_DIR = Path(__file__).resolve().parent.parent.parent
DATA_DIR = BASE_DIR / "data"

router = APIRouter()


class RegistroIn(BaseModel):
    habito_id: int
    valor: int = 1
    fecha: date | None = None


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

@router.post("/registro")
def registrar_habito(registro: RegistroIn):
    fecha = registro.fecha or date.today().isoformat()

    with get_connection() as conn:
        conn.execute(
            "INSERT INTO registros (habito_id, fecha, valor) VALUES (?, ?, ?)",
            (registro.habito_id, fecha, registro.valor)
        )

    return {"status": "ok"}

