import sqlite3
from pathlib import Path
from datetime import date

BASE_DIR = Path(__file__).resolve().parent.parent.parent
DB_PATH = BASE_DIR / "data" / "habitos.db"


def get_connection():
    return sqlite3.connect(DB_PATH)


def init_db():
    with get_connection() as conn:
        conn.execute("""
        CREATE TABLE IF NOT EXISTS registros (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            habito_id INTEGER NOT NULL,
            fecha TEXT NOT NULL,
            valor INTEGER NOT NULL
        )
        """)
