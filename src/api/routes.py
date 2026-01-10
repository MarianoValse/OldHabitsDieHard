from fastapi import APIRouter
from pathlib import Path
from datetime import date
from pydantic import BaseModel
from src.services.db import getConnection

from src.loaders.loader import cDDBBLoader

BASE_DIR = Path(__file__).resolve().parent.parent.parent
DATA_DIR = BASE_DIR / "data"

router = APIRouter()


class cEntrie(BaseModel):
    habit_id: int
    value: int = 1
    entrieDate: date | None = None


@router.get("/habits")
def getHabits():
    loader = cDDBBLoader(DATA_DIR) 
    habits = loader.getHabitsList() 

    return [
        {
            "id": h.id,
            "nombre": h.name,
            "activo": h.active,
            "dificultad": h.dificulty.name if h.dificulty else None,
            "peso": h.weigth.name if h.weigth else None
        }
        for h in habits
        if h.active
    ]

@router.post("/entries")
def createEntrie(entrie: cEntrie):
    # date = entrie.entrieDate or date.today().isoformat()

    with getConnection() as conn:
        conn.execute(
            "INSERT INTO Entries (ENTRY_fk_habits, ENTRY_fk_grade, ENTRY_date) VALUES (?,?,?)",           
            (entrie.habit_id, entrie.value, entrie.entrieDate)
            # "INSERT INTO Entries (ENTRY_fk_habits, ENTRY_fk_grade, ENTRY_date) VALUES (1, 2, '2025-01-10')", 
        )

    return {"status": "ok"}

@router.get("/habits/today")
def getEntriesList():

    fecha = date.today().isoformat()

    with getConnection() as conn:
        conn.execute(
            # aca vamos a hacer otra cosa una lista de los habitps y cuales estan y no hechos hoy
            # "SELECT ENTRY_fk_habits FROM Entries WHERE ENTRY_date = ? group by ENTRY_fk_habits ",
            "SELECT hab.HAB_name , entry.ENTRY_value FROM Habits hab LEFT JOIN Entries entry on entry.ENTRY_fk_habits = hab.HAB_ID WHERE hab.HAB_active = 1 and entry.ENTRY_date = ? ",            
            (fecha)
        )

    loader = cDDBBLoader(DATA_DIR)
    habitsToDay = loader.getHabitsList()

    return [
        {
            "id": h.id,
            "nombre": h.name,
            "activo": h.active,
            "dificultad": h.dificulty.name if h.dificulty else None,
            "peso": h.weigth.name if h.weigth else None
        }
        for h in habitsToDay
    ]