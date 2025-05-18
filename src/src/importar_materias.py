import sqlite3
import csv
from PySide6.QtWidgets import QApplication, QFileDialog, QWidget, QMessageBox

class ImportadorMaterias(QWidget):
    def __init__(self):
        super().__init__()
        self.importar_csv()

    def importar_csv(self):
        archivo, _ = QFileDialog.getOpenFileName(self, "Seleccionar archivo CSV de Materias", "", "Archivos CSV (*.csv)")
        if archivo:
            try:
                conn = sqlite3.connect("gestion_labs.db")
                cursor = conn.cursor()

                with open(archivo, newline='', encoding='utf-8') as csvfile:
                    lector = csv.reader(csvfile)
                    next(lector)  # Salta la cabecera
                    for fila in lector:
                        sigla, nombre_materia = fila
                        cursor.execute("INSERT INTO Materia (sigla, nombre_materia) VALUES (?, ?)", (sigla, nombre_materia))

                conn.commit()
                conn.close()
                QMessageBox.information(self, "Éxito", "Materias importadas correctamente.")
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Ocurrió un error: {str(e)}")

if __name__ == "__main__":
    app = QApplication([])
    ventana = ImportadorMaterias()
    ventana.show()
    app.exec()

