import sqlite3
from pathlib import Path
from datetime import date

BASE_DIR = Path(__file__).resolve().parent.parent.parent
DB_PATH = BASE_DIR / "data" / "habitos.db"


def getConnection():
    return sqlite3.connect(DB_PATH)


def init_db():
    with getConnection() as conn:
        sql = (BASE_DIR / "data" / "init_db.sql").read_text()
        conn.executescript(sql)
