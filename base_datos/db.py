import sqlite3  # Librería para usar SQLite

# Paso 1: Crear la conexión a la base de datos
def create_connection():
    conn = sqlite3.connect("gestion_labs.db")
    return conn

# Paso 2: Crear las tablas necesarias
def create_tables():
    conn = create_connection()
    cursor = conn.cursor()

    # Tabla Estudiante
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Estudiante (
            id_est INTEGER PRIMARY KEY AUTOINCREMENT,
            nomb_est TEXT NOT NULL,
            ci TEXT NOT NULL,
            celular TEXT,
            email_est TEXT,
            carrera TEXT NOT NULL
        )
    ''')

    # Tabla Docente_lab
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Docente_lab (
            id_doc INTEGER PRIMARY KEY AUTOINCREMENT,
            nomb_doc TEXT NOT NULL,
            email_doc TEXT
        )
    ''')

    # Tabla Materia
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Materia (
            sigla TEXT PRIMARY KEY,
            nomb_materia TEXT NOT NULL,
            dia TEXT,
            hora TEXT,
            semestre TEXT
        )
    ''')

    # Tabla Laboratorio
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Laboratorio (
            id_lab INTEGER PRIMARY KEY AUTOINCREMENT,
            nomb_materia TEXT NOT NULL,
            sigla TEXT,
            capacidad INTEGER
        )
    ''')

    # Tabla Horario_laboratorio
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Horario_laboratorio (
            id_horario INTEGER PRIMARY KEY AUTOINCREMENT,
            sigla TEXT NOT NULL,
            id_doc INTEGER NOT NULL,
            id_lab INTEGER NOT NULL,
            dia TEXT,
            hora_inicio TEXT,
            hora_fin TEXT
        )
    ''')

    # Tabla Asignación
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Asignacion (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            id_est INTEGER NOT NULL,
            id_horario INTEGER NOT NULL,
            semestre TEXT,
            estado TEXT,
            fecha_modif TEXT
        )
    ''')

    conn.commit()
    conn.close()

# Paso 3: Ejecutar todo
if __name__ == "__main__":
    create_tables()
    print("✅ Base de datos y tablas creadas correctamente.")