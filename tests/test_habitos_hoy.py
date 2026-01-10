from datetime import date
from fastapi.testclient import TestClient
from src.api.main import app
from src.services.db import getConnection

client = TestClient(app)


def test_habitos_hoy_marca_correctamente():
    
    fecha = date.today().isoformat()

    # limpiamos registros
    with getConnection() as conn:
        conn.execute("DELETE FROM Entries")

    # obtenemos hábitos
    resp = client.get("/habits")
    habits = resp.json()

    assert len(habits) > 0

    firstHabit = habits[2]

    # marcamos uno como hecho hoy
    client.post("/entries",
        json={
            "habit_id": firstHabit["id"],
            "value": 1,
            "entrieDate": fecha
        }
    )

    # pedimos hábitos de hoy
    resp = client.get("/habits/today")
    data = resp.json()

    for h in data:
        if h["id"] == firstHabit["id"]:
            assert h["grado"] > 0                             
        else:
            assert h["grado"] == None 

    
