import sys
from PySide2.QtWidgets import QMainWindow, QApplication, QMessageBox
import json

from MMenu.mainMenu import Ui_MainWindow
from Tabla.table_code import TableWindow
from Form.form_code import Formwindow
from Grafico.graficos import Graphic
from Busqueda.buscarGente import BuscarWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.main = MainWindow
        self.ui.setupUi(self)
        self.graphic = Graphic(parent=self)

        with open("data.json", "r") as f:
            personas = json.load(f)
        self.personas = personas  # almacena los datos del json que contiene las personas vacunadas
        self.tabla = TableWindow(self)
        self.form = Formwindow(self)
        self.busqueda = BuscarWindow()
        self.validacion = True  # es una variable para que una funcion se realice una vez

    def salir(self):
        self.tabla.close()
        self.form.close()  # se cierran las ventanas, primero las demas y finalmente el menu(boton salir)
        self.main.close(self)
        self.busqueda.close()
    def buscar(self):
        self.busqueda.show()
    def closeEvent(self, event):
        self.salir()  # (para la cruz de la ventana)

    def abrirtabla(self):
        self.form.actualizarTabla()
        self.tabla.show()  # actualiza la tabla solo la primera vez que se abre para tomar los datos del json
        self.validacion = False

    def abrirForm(self):
        self.form.show()

    def abrirGrafico(self):
        self.graphic.grafico()

    def borrarTabla(self):
        reply = QMessageBox.question(self, "Mensaje", "Seguro quiere borrar todos los datos", QMessageBox.Yes,
                                     QMessageBox.No)
        # borra los datos de la tabla y del json primero confirmando
        if reply == QMessageBox.Yes:
            row = int(self.tabla.ui.tableWidget.rowCount())
            for i in range(row + 1):
                self.tabla.ui.tableWidget.removeRow(i)
            with open("data.json", "w") as f:
                vacio = []
                json.dump(vacio, f, indent=0)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())
