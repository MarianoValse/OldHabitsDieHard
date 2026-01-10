from datetime import date
from fastapi.testclient import TestClient
from src.api.main import app
from src.services.db import getConnection

client = TestClient(app)


def test_habitos_hoy_marca_correctamente():
    
    x=1 
    fecha = date.today().isoformat()

    # limpiamos registros
    with getConnection() as conn:
        conn.execute("DELETE FROM Entries")

    # obtenemos hábitos
    resp = client.get("/habits")
    habits = resp.json()

    assert len(habits) > 0

    firstHabit = habits[0]

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

    find = False

    for h in data:
        if h["id"] == firstHabit["id"]:
            find = True
            assert h["hecho"] is True
        else:
            assert h["hecho"] is False

    assert find is True
