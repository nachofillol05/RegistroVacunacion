import json

from PySide2.QtWidgets import QMainWindow

from Tabla.table import Ui_tabla


class TableWindow(QMainWindow):
    def __init__(self, parent):
        super().__init__()
        self.ui = Ui_tabla()
        self.ui.setupUi(self)
        self.parent = parent

    def Dni_Sort(self,dni_input):
        with open("data.json", "r") as f:
            database = json.load(f)

        for i in database:
            if i['documento'] == dni_input:
                temp_list = {
                    "nombre": (i['nombre']),
                    "apellido": (i['apellido']),
                    "documento": (i["documento"]),
                    "centro": (i['centro']),
                    "dosis": (i['dosis']),
                    "fecha": (i['fecha'])
                }
                return temp_list


    def closeEvent(self, event):
        print('Exit table')
        self.hide()
        self.parent.show()