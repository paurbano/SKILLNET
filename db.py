import sqlite3
DATABASE_NAME = "citas.db"


def get_db():
    conn = sqlite3.connect(DATABASE_NAME)
    return conn


def create_tables():
    tables = [
        """ CREATE TABLE IF NOT EXISTS pacientes(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                tipoid TEXT NOT null,
                numid text not null,
                nombre TEXT NOT NULL,
                telefono TEXT
            )
        """,        
        """CREATE TABLE IF NOT EXISTS doctores(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombreDoctor TEXT not null,
                especialidad text NOT NULL
            )
        """,
        """CREATE TABLE IF NOT EXISTS citas(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            paciente_id INTEGER NOT NULL,
            doctor_id INTEGER NOT NULL,
            fecha TEXT not null,
            FOREIGN KEY (paciente_id) REFERENCES pacientes(id),
            FOREIGN KEY (doctor_id) REFERENCES doctores(id)
            )
        """
    ]
    db = get_db()
    cursor = db.cursor()
    for table in tables:
        cursor.execute(table)