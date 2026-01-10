from datetime import date
from fastapi.testclient import TestClient
from src.api.main import app
from src.services.db import get_connection

client = TestClient(app)


def test_habitos_hoy_marca_correctamente():
    
    x=1 
    hoy = date.today().isoformat()

    # limpiamos registros
    with get_connection() as conn:
        conn.execute("DELETE FROM registros")

    # obtenemos hábitos
    resp = client.get("/habitos")
    habitos = resp.json()

    assert len(habitos) > 0

    primer_habito = habitos[0]

    # marcamos uno como hecho hoy
    client.post(
        "/registro",
        json={
            "habito_id": primer_habito["id"],
            "valor": 1,
            "fecha": hoy
        }
    )

    # pedimos hábitos de hoy
    resp = client.get("/habitos/hoy")
    data = resp.json()

    encontrado = False

    for h in data:
        if h["id"] == primer_habito["id"]:
            encontrado = True
            assert h["hecho"] is True
        else:
            assert h["hecho"] is False

    assert encontrado is True
