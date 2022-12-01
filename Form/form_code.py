import json
from datetime import datetime
from PySide2.QtCore import QCoreApplication
from PySide2.QtWidgets import QMainWindow, QMessageBox, QTableWidgetItem

from Form.formpro import Ui_form


# funcion que verifica si es un numero
def isfloat(value):
    try:
        float(value)
        return True
    except ValueError:
        return False


class Formwindow(QMainWindow):
    def __init__(self, parent):
        super().__init__()
        self.ui = Ui_form()
        self.ui.setupUi(self)
        self.parent = parent

    def closeEvent(self, event):
        print('Exit Form')
        self.hide()
        self.parent.show()

    def agregar(self):
        # Toma los datos
        ciudad = self.ui.ciudadseleccion.currentText()
        vacuna = self.ui.vacunaseleccion.currentText()
        nombre = self.ui.nombreline.text()
        apellido = self.ui.apellidoline.text()
        dni = self.ui.dniline.text()
        fecha = str(self.ui.fechaseleccion.date())
        fecha = fecha.replace("PySide2.QtCore.QDate", "")
        nombre = nombre.title()
        apellido = apellido.title()

        # Verifica si es numero el dni
        if not isfloat(value=dni):
            message = QMessageBox()
            message.setText("Porfavor ingrese numeros en el DNI")
            message.exec()
            # Verifica el largo del dni
        elif len(dni) != 8:
            message = QMessageBox()
            message.setText("Porfavor ingrese un DNI correcto (8 digitos)")
            message.exec()
        # verifica si no hay algun campo vacio
        elif not vacuna == "Seleccione la vacuna" and not ciudad == "seleccione ciudad" and not nombre == "" and not apellido == "" and not dni == "":
            message = QMessageBox()
            message.setText("Se cargaron los datos correctamente")
            message.exec()
            persona = {
                'nombre': nombre,
                'apellido': apellido,
                'documento': dni,
                'centro': ciudad,
                'dosis': vacuna,
                'fecha': fecha,
            }

            self.addToTable(persona)
            self.ordenarTabla()
            self.parent.personas.append(persona)
            with open("data.json", "w") as f:
                json.dump(self.parent.personas, f, indent=6, default=str)
            self.borrar()
        else:
            message = QMessageBox()
            message.setText("Termine de ingresar los datos porfavor")
            message.exec()

    def ordenarTabla(self):
        self.parent.personas.sort(key=lambda item: item.get("apellido"))
        print(self.parent.personas)

    def actualizarTabla(self):
        self.ordenarTabla()
        if self.parent.validacion:
            for persona in self.parent.personas:
                self.addToTable(persona)

            print("se actualizo")

    # funcion para añadir los datos a la tabla
    def addToTable(self, persona):
        row = int(self.parent.tabla.ui.tableWidget.rowCount())
        self.parent.tabla.ui.tableWidget.insertRow(row)
        for i, key in enumerate(persona):
            item_to_add = str(persona[key])
            print(item_to_add)
            self.parent.tabla.ui.tableWidget.setItem(row, i, QTableWidgetItem(item_to_add))

    def borrar(self):
        # vuelve todos los datos a como estaban al principio(vacios)
        self.ui.nombreline.setText("")
        self.ui.nombreline.setPlaceholderText(QCoreApplication.translate("form", u"Ingrese el nombre", None))
        self.ui.apellidoline.setInputMask("")
        self.ui.apellidoline.setText("")
        self.ui.apellidoline.setPlaceholderText(QCoreApplication.translate("form", u"Ingrese el apellido", None))
        self.ui.dniline.setText("")
        self.ui.dniline.setPlaceholderText(QCoreApplication.translate("form", u"Ingrese el DNI", None))
        self.ui.botonborrar.setText(QCoreApplication.translate("form", u"Borrar", None))
        self.ui.botonagregar.setText(QCoreApplication.translate("form", u"agregar", None))
        self.ui.ciudadseleccion.setCurrentText(QCoreApplication.translate("form", u"seleccione ciudad", None))
        self.ui.vacunaseleccion.setCurrentText(QCoreApplication.translate("form", u"Seleccione la vacuna", None))
        self.ui.fechaseleccion.setDate(datetime.now().date())
