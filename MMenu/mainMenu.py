# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainMenuBhfGmA.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *




class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(181, 182)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 10, 160, 170))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.formBtn = QPushButton(self.verticalLayoutWidget)
        self.formBtn.setObjectName(u"formBtn")

        self.verticalLayout.addWidget(self.formBtn)

        self.listaBtn = QPushButton(self.verticalLayoutWidget)
        self.listaBtn.setObjectName(u"listaBtn")

        self.verticalLayout.addWidget(self.listaBtn)

        self.pushButton_2 = QPushButton(self.verticalLayoutWidget)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.verticalLayout.addWidget(self.pushButton_2)

        self.pushButton = QPushButton(self.verticalLayoutWidget)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout.addWidget(self.pushButton)

        self.exitBtn = QPushButton(self.verticalLayoutWidget)
        self.exitBtn.setObjectName(u"exitBtn")

        self.verticalLayout.addWidget(self.exitBtn)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.exitBtn.clicked.connect(MainWindow.salir)
        self.listaBtn.clicked.connect(MainWindow.abrirtabla)
        self.formBtn.clicked.connect(MainWindow.abrirForm)
        self.pushButton.clicked.connect(MainWindow.borrarTabla)
        self.pushButton_2.clicked.connect(MainWindow.abrirGrafico)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.formBtn.setText(QCoreApplication.translate("MainWindow", u"A\u00f1adir ciudadano", None))
        self.listaBtn.setText(QCoreApplication.translate("MainWindow", u"Registros", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"ver grafico", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Borrar Datos", None))
        self.exitBtn.setText(QCoreApplication.translate("MainWindow", u"Salir", None))
    # retranslateUi


