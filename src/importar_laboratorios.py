import csv
import sqlite3
from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton, QFileDialog, QMessageBox
)

class ImportarLaboratorios(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Importar Laboratorios CSV")
        self.setGeometry(100, 100, 300, 100)

        layout = QVBoxLayout()
        self.boton = QPushButton("Seleccionar archivo CSV")
        self.boton.clicked.connect(self.importar_csv)
        layout.addWidget(self.boton)
        self.setLayout(layout)

    def importar_csv(self):
        archivo, _ = QFileDialog.getOpenFileName(self, "Seleccionar CSV", "", "Archivos CSV (*.csv)")
        if archivo:
            try:
                conn = sqlite3.connect("gestion_labs.db")
                cursor = conn.cursor()
                with open(archivo, newline='', encoding='utf-8') as f:
                    lector = csv.DictReader(f)
                    for fila in lector:
                        cursor.execute("""
                            INSERT INTO Laboratorio (nomb_materia, sigla, capacidad)
                            VALUES (?, ?, ?)
                        """, (
                            fila['nomb_materia'],
                            fila['sigla'],
                            fila['capacidad']
                        ))
                conn.commit()
                conn.close()
                QMessageBox.information(self, "Éxito", "Laboratorios importados correctamente.")
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Error al importar: {e}")

if __name__ == "__main__":
    app = QApplication([])
    ventana = ImportarLaboratorios()
    ventana.show()
    app.exec()

