import sqlite3

def crear_tablas():
    conn = sqlite3.connect("../gestion_laboratorios.db")
    cursor = conn.cursor()

    cursor.execute("""
CREATE TABLE  Carrera(
id_carrera INTEGER PRIMARY KEY,
nombre_carrera TEXT NOT NULL
);""")

    cursor.execute("""
CREATE TABLE Estudiante(
id_est INTEGER PRIMARY KEY,
id_carrera INTEGER NOT NULL,
nombre TEXT NOT NULL,
apellido_pat TEXT NOT NULL,
apellido_mat TEXT NOT NULL,
ci INTEGER,
celular TEXT,
email_est TEXT NOT NULL UNIQUE,
FOREIGN KEY(id_carrera) REFERENCES Carrera(id_carrera)
);""")

    cursor.execute("""
CREATE TABLE Docente_lab(
id_doc INTEGER PRIMARY KEY,
nombre TEXT NOT NULL,
apellido_pat TEXT NOT NULL,
apellido_mat TEXT NOT NULL,
email_doc TEXT NOT NULL UNIQUE
);""")

    cursor.execute("""CREATE TABLE Materia(
sigla TEXT PRIMARY KEY,
nombre_materia TEXT NOT NULL
);""")

    cursor.execute("""CREATE TABLE Laboratorio(
id_lab INTEGER PRIMARY KEY,
capacidad INTEGER NOT NULL
);""")

    cursor.execute("""CREATE TABLE Horario_laboratorio(
id_horario INTEGER PRIMARY KEY,
sigla TEXT NOT NULL,
id_doc INTEGER NOT NULL,
id_lab INTEGER NOT NULL,
dia TEXT NOT NULL,
hora_inicio TEXT NOT NULL,
hora_fin TEXT NOT NULL,
FOREIGN KEY(sigla) REFERENCES Materia(sigla),
FOREIGN KEY(id_doc) REFERENCES Docente_lab(id_doc),
FOREIGN KEY(id_lab) REFERENCES Laboratorio(id_lab)
);""")

    cursor.execute("""CREATE TABLE Asignacion(
id_asig INTEGER PRIMARY KEY,
id_est INTEGER NOT NULL,
id_horario INTEGER NOT NULL,
estado TEXT NOT NULL,
fecha_modif DATETIME NOT NULL,
FOREIGN KEY(id_est) REFERENCES Estudiante(id_est),
FOREIGN KEY(id_horario) REFERENCES Horario_laboratorio(id_horario)
);""")

    conn.commit()
    conn.close()
    print("Tablas creadas correctamente.")

if __name__ == "__main__":
    crear_tablas()