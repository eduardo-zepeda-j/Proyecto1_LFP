# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainProyecto1.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ventana(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1250, 1006)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(280, 0, 601, 51))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnCargar = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btnCargar.setObjectName("btnCargar")
        self.horizontalLayout.addWidget(self.btnCargar)
        self.btnAnalizar = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btnAnalizar.setObjectName("btnAnalizar")
        self.horizontalLayout.addWidget(self.btnAnalizar)
        self.btnReportes = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btnReportes.setObjectName("btnReportes")
        self.horizontalLayout.addWidget(self.btnReportes)
        self.btnSalir = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btnSalir.setObjectName("btnSalir")
        self.horizontalLayout.addWidget(self.btnSalir)
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 80, 160, 171))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.btnOriginal = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btnOriginal.setObjectName("btnOriginal")
        self.verticalLayout.addWidget(self.btnOriginal)
        self.btnMirrorX = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btnMirrorX.setObjectName("btnMirrorX")
        self.verticalLayout.addWidget(self.btnMirrorX)
        self.btnMirrorY = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btnMirrorY.setObjectName("btnMirrorY")
        self.verticalLayout.addWidget(self.btnMirrorY)
        self.btnDblMirror = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btnDblMirror.setObjectName("btnDblMirror")
        self.verticalLayout.addWidget(self.btnDblMirror)
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(200, 70, 661, 41))
        self.comboBox.setObjectName("comboBox")
        self.visor = QtWidgets.QLabel(self.centralwidget)
        self.visor.setGeometry(QtCore.QRect(200, 130, 951, 981))
        self.visor.setText("")
        self.visor.setObjectName("visor")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(10, 290, 160, 80))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.btnCrear = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.btnCrear.setObjectName("btnCrear")
        self.verticalLayout_2.addWidget(self.btnCrear)
        

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btnCargar.setText(_translate("MainWindow", "Cargar"))
        self.btnAnalizar.setText(_translate("MainWindow", "Analizar"))
        self.btnReportes.setText(_translate("MainWindow", "Reportes"))
        self.btnSalir.setText(_translate("MainWindow", "Salir"))
        self.btnOriginal.setText(_translate("MainWindow", "Todas"))
        self.btnMirrorX.setText(_translate("MainWindow", "Mirror X"))
        self.btnMirrorY.setText(_translate("MainWindow", "Mirror Y"))
        self.btnDblMirror.setText(_translate("MainWindow", "Double Mirror"))
        self.btnCrear.setText(_translate("MainWindow", "Crear Imagenes"))
