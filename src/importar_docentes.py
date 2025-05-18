import sqlite3
import csv
from PySide6.QtWidgets import QApplication, QFileDialog, QWidget, QMessageBox

class ImportadorDocentes(QWidget):
    def __init__(self):
        super().__init__()
        self.importar_csv()

    def importar_csv(self):
        archivo, _ = QFileDialog.getOpenFileName(self, "Seleccionar archivo CSV", "", "Archivos CSV (*.csv)")
        if archivo:
            try:
                conn = sqlite3.connect("gestion_labs.db")
                cursor = conn.cursor()
                with open(archivo, newline='', encoding='utf-8') as f:
                    lector = csv.DictReader(f)
                    for fila in lector:
                        cursor.execute("""
                            INSERT INTO Docente_lab (nomb_doc, email_doc)
                            VALUES (?, ?)
                        """, (
                            fila["nomb_doc"],
                            fila["email_doc"]
                        ))
                conn.commit()
                conn.close()
                QMessageBox.information(self, "Éxito", "Datos de docentes importados correctamente.")
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Error al importar: {e}")

if __name__ == "__main__":
    app = QApplication([])
    ventana = ImportadorDocentes()
    ventana.show()
    app.exec()
