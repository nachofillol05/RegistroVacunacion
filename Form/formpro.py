# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'formpkbUru.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
from datetime import date, datetime

from PySide2.QtCore import *
from PySide2.QtWidgets import *


class Ui_form(object):
    def setupUi(self, form):
        if not form.objectName():
            form.setObjectName(u"form")
        form.resize(542, 150)
        self.centralwidget = QWidget(form)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayoutWidget = QWidget(self.centralwidget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(0, 0, 541, 151))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)

        self.dniline = QLineEdit(self.gridLayoutWidget)
        self.dniline.setObjectName(u"dniline")

        self.gridLayout.addWidget(self.dniline, 1, 0, 1, 1)

        self.nombreline = QLineEdit(self.gridLayoutWidget)
        self.nombreline.setObjectName(u"nombreline")
        self.gridLayout.addWidget(self.nombreline, 0, 0, 1, 1)

        self.apellidoline = QLineEdit(self.gridLayoutWidget)
        self.apellidoline.setObjectName(u"apellidoline")

        self.gridLayout.addWidget(self.apellidoline, 0, 1, 1, 1)

        self.ciudadseleccion = QComboBox(self.gridLayoutWidget)
        self.ciudadseleccion.addItem("")
        self.ciudadseleccion.addItem("")
        self.ciudadseleccion.addItem("")
        self.ciudadseleccion.addItem("")
        self.ciudadseleccion.setObjectName(u"ciudadseleccion")
        self.ciudadseleccion.setEditable(False)
        self.ciudadseleccion.setSizeAdjustPolicy(QComboBox.AdjustToContents)

        self.gridLayout.addWidget(self.ciudadseleccion, 7, 0, 1, 1)

        self.vacunaseleccion = QComboBox(self.gridLayoutWidget)
        self.vacunaseleccion.addItem("")
        self.vacunaseleccion.addItem("")
        self.vacunaseleccion.addItem("")
        self.vacunaseleccion.addItem("")
        self.vacunaseleccion.addItem("")
        self.vacunaseleccion.addItem("")
        self.vacunaseleccion.addItem("")
        self.vacunaseleccion.addItem("")
        self.vacunaseleccion.addItem("")
        self.vacunaseleccion.addItem("")
        self.vacunaseleccion.addItem("")
        self.vacunaseleccion.setObjectName(u"vacunaseleccion")

        self.gridLayout.addWidget(self.vacunaseleccion, 1, 1, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.botonborrar = QPushButton(self.gridLayoutWidget)
        self.botonborrar.setObjectName(u"botonborrar")

        self.horizontalLayout.addWidget(self.botonborrar)


        self.gridLayout.addLayout(self.horizontalLayout, 7, 1, 1, 1)

        today = date.today()
        anno = int(today.strftime("%Y"))
        mes = int(today.strftime("%m"))
        dia = int(today.strftime("%d"))
        self.fechaseleccion = QDateEdit(self.gridLayoutWidget)
        self.fechaseleccion.setObjectName(u"fechaseleccion")
        self.fechaseleccion.setMinimumDateTime(QDateTime(QDate( 2021, 1, 1), QTime(0, 0, 0)))
        self.fechaseleccion.setMaximumDate(QDate(anno, mes, dia))
        self.fechaseleccion.setDate(datetime.now().date())

        self.gridLayout.addWidget(self.fechaseleccion, 4, 0, 1, 1)

        self.botonagregar = QPushButton(self.gridLayoutWidget)
        self.botonagregar.setObjectName(u"botonagregar")

        self.gridLayout.addWidget(self.botonagregar, 4, 1, 1, 1)

        form.setCentralWidget(self.centralwidget)

        self.retranslateUi(form)
        self.botonborrar.clicked.connect(form.borrar)
        self.botonagregar.clicked.connect(form.agregar)

        QMetaObject.connectSlotsByName(form)
    # setupUi

    def retranslateUi(self, form):
        form.setWindowTitle(QCoreApplication.translate("form", u"MainWindow", None))
        self.label_3.setText(QCoreApplication.translate("form", u"Ingrese la fecha en la que fue vacunado", None))
        self.dniline.setText("")
        self.dniline.setPlaceholderText(QCoreApplication.translate("form", u"Ingrese el DNI", None))
        self.nombreline.setText("")
        self.nombreline.setPlaceholderText(QCoreApplication.translate("form", u"Ingrese el nombre", None))
        self.apellidoline.setInputMask("")
        self.apellidoline.setText("")
        self.apellidoline.setPlaceholderText(QCoreApplication.translate("form", u"Ingrese el apellido", None))
        self.ciudadseleccion.setItemText(0, QCoreApplication.translate("form", u"seleccione ciudad", None))
        self.ciudadseleccion.setItemText(1, QCoreApplication.translate("form", u"La calera", None))
        self.ciudadseleccion.setItemText(2, QCoreApplication.translate("form", u"Villa allende", None))
        self.ciudadseleccion.setItemText(3, QCoreApplication.translate("form", u"Narnia", None))

        self.ciudadseleccion.setCurrentText(QCoreApplication.translate("form", u"seleccione ciudad", None))
        self.vacunaseleccion.setItemText(0, QCoreApplication.translate("form", u"Seleccione la vacuna", None))
        self.vacunaseleccion.setItemText(1, QCoreApplication.translate("form", u"SPUTNIK V(1era dosis)", None))
        self.vacunaseleccion.setItemText(2, QCoreApplication.translate("form", u"SPUTNIK V(2da dosis)", None))
        self.vacunaseleccion.setItemText(3, QCoreApplication.translate("form", u"ASTRAZENECA(1era dosis)", None))
        self.vacunaseleccion.setItemText(4, QCoreApplication.translate("form", u"ASTRAZENECA(2da dosis)", None))
        self.vacunaseleccion.setItemText(5, QCoreApplication.translate("form", u"PFIZER(1era dosis)", None))
        self.vacunaseleccion.setItemText(6, QCoreApplication.translate("form", u"PFIZER(2da dosis)", None))
        self.vacunaseleccion.setItemText(7, QCoreApplication.translate("form", u"MODERNA(1era dosis)", None))
        self.vacunaseleccion.setItemText(8, QCoreApplication.translate("form", u"MODERNA(2da dosis)", None))
        self.vacunaseleccion.setItemText(9, QCoreApplication.translate("form", u"SINOPHARM(1era dosis) ", None))
        self.vacunaseleccion.setItemText(10, QCoreApplication.translate("form", u"SINOPHARM(2da dosis) ", None))

        self.botonborrar.setText(QCoreApplication.translate("form", u"Borrar", None))
        self.botonagregar.setText(QCoreApplication.translate("form", u"agregar", None))
    # retranslateUi

