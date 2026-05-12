import sqlite3
from datetime import datetime

DATABASE_FILE = "taximetro.db"

def init_database():
    """
    Crea la base de datos y la tabla de trayectos si no existen.
    """
    with sqlite3.connect(DATABASE_FILE) as connection:
        cursor = connection.cursor()
        cursor.execute(
             """
            CREATE TABLE IF NOT EXISTS trips (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                finished_at TEXT NOT NULL,
                stopped_time REAL NOT NULL,
                moving_time REAL NOT NULL,
                stopped_rate REAL NOT NULL,
                moving_rate REAL NOT NULL,
                total_fare REAL NOT NULL
            )
            """
        )
        connection.commit()

def save_trip_to_database(stopped_time, moving_time, stopped_rate, moving_rate, total_fare):
    """
    Guarda un trayecto finalizado en la base de datos SQLite.
    """
    finished_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with sqlite3.connect(DATABASE_FILE) as connection:
        cursor = connection.cursor()
        cursor.execute(
            """
            INSERT INTO trips (
                finished_at,
                stopped_time,
                moving_time,
                stopped_rate,
                moving_rate,
                total_fare
            )
            VALUES (?, ?, ?, ?, ?, ?)
            """,
            (
                finished_at,
                stopped_time,
                moving_time,
                stopped_rate,
                moving_rate,
                total_fare,
            ),
        )
        connection.commit()

def get_recent_trips(limit=10):
    """
    Devuelve los ultimos trayectos guardados en la base de datos.
    """
    with sqlite3.connect(DATABASE_FILE) as connection:
        cursor = connection.cursor()
        cursor.execute(
            """
            SELECT
                id,
                finished_at,
                stopped_time,
                moving_time,
                stopped_rate,
                moving_rate,
                total_fare
            FROM trips
            ORDER BY id DESC
            LIMIT ?
            """,
            (limit,)
        )
        return cursor.fetchall()