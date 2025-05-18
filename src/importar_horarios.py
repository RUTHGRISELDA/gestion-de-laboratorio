import csv
import sqlite3
from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton, QFileDialog, QMessageBox
)

class ImportarHorarios(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Importar Horarios CSV")
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
                            INSERT INTO Horario_laboratorio (sigla, id_doc, id_lab, dia, hora_inicio, hora_fin)
                            VALUES (?, ?, ?, ?, ?, ?)
                        """, (
                            fila['sigla'],
                            fila['id_doc'],
                            fila['id_lab'],
                            fila['dia'],
                            fila['hora_inicio'],
                            fila['hora_fin']
                        ))
                conn.commit()
                conn.close()
                QMessageBox.information(self, "Éxito", "Horarios importados correctamente.")
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Error al importar: {e}")

if __name__ == "__main__":
    app = QApplication([])
    ventana = ImportarHorarios()
    ventana.show()
    app.exec()
