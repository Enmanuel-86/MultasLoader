# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pantalla_multados_view.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import images_resources_rc

class Ui_PantallaMultasView(object):
    def setupUi(self, PantallaMultasView):
        if not PantallaMultasView.objectName():
            PantallaMultasView.setObjectName(u"PantallaMultasView")
        PantallaMultasView.resize(978, 713)
        PantallaMultasView.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(PantallaMultasView)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.scrollArea = QScrollArea(PantallaMultasView)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 976, 711))
        self.verticalLayout_2 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_principal = QFrame(self.scrollAreaWidgetContents)
        self.frame_principal.setObjectName(u"frame_principal")
        self.frame_principal.setFrameShape(QFrame.StyledPanel)
        self.frame_principal.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_principal)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.frame_form = QFrame(self.frame_principal)
        self.frame_form.setObjectName(u"frame_form")
        self.frame_form.setMinimumSize(QSize(821, 221))
        self.frame_form.setMaximumSize(QSize(911, 251))
        self.frame_form.setFrameShape(QFrame.StyledPanel)
        self.frame_form.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_form)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_icon_person = QLabel(self.frame_form)
        self.label_icon_person.setObjectName(u"label_icon_person")
        self.label_icon_person.setMinimumSize(QSize(41, 51))
        self.label_icon_person.setMaximumSize(QSize(61, 61))
        self.label_icon_person.setScaledContents(True)

        self.horizontalLayout.addWidget(self.label_icon_person)

        self.label_datos_multado = QLabel(self.frame_form)
        self.label_datos_multado.setObjectName(u"label_datos_multado")

        self.horizontalLayout.addWidget(self.label_datos_multado, 0, Qt.AlignLeft)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.frame = QFrame(self.frame_form)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(701, 121))
        self.frame.setMaximumSize(QSize(871, 171))
        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(6)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.widget_form_nombre = QWidget(self.frame)
        self.widget_form_nombre.setObjectName(u"widget_form_nombre")
        self.widget_form_nombre.setMinimumSize(QSize(161, 0))
        self.widget_form_nombre.setMaximumSize(QSize(201, 55))
        self.verticalLayout_6 = QVBoxLayout(self.widget_form_nombre)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_nombre = QLabel(self.widget_form_nombre)
        self.label_nombre.setObjectName(u"label_nombre")

        self.verticalLayout_6.addWidget(self.label_nombre, 0, Qt.AlignLeft)

        self.lineEdit_nombre = QLineEdit(self.widget_form_nombre)
        self.lineEdit_nombre.setObjectName(u"lineEdit_nombre")
        self.lineEdit_nombre.setMinimumSize(QSize(161, 31))
        self.lineEdit_nombre.setMaximumSize(QSize(201, 50))

        self.verticalLayout_6.addWidget(self.lineEdit_nombre)


        self.gridLayout.addWidget(self.widget_form_nombre, 0, 0, 1, 1)

        self.widget_form_apellido = QWidget(self.frame)
        self.widget_form_apellido.setObjectName(u"widget_form_apellido")
        self.widget_form_apellido.setMinimumSize(QSize(161, 0))
        self.widget_form_apellido.setMaximumSize(QSize(201, 55))
        self.verticalLayout_7 = QVBoxLayout(self.widget_form_apellido)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.label_apellido = QLabel(self.widget_form_apellido)
        self.label_apellido.setObjectName(u"label_apellido")

        self.verticalLayout_7.addWidget(self.label_apellido, 0, Qt.AlignLeft)

        self.lineEdit_apellido = QLineEdit(self.widget_form_apellido)
        self.lineEdit_apellido.setObjectName(u"lineEdit_apellido")
        self.lineEdit_apellido.setMinimumSize(QSize(161, 31))
        self.lineEdit_apellido.setMaximumSize(QSize(201, 50))

        self.verticalLayout_7.addWidget(self.lineEdit_apellido)


        self.gridLayout.addWidget(self.widget_form_apellido, 0, 1, 1, 1)

        self.widget_form_residencia = QWidget(self.frame)
        self.widget_form_residencia.setObjectName(u"widget_form_residencia")
        self.widget_form_residencia.setMinimumSize(QSize(161, 0))
        self.widget_form_residencia.setMaximumSize(QSize(201, 55))
        self.verticalLayout_8 = QVBoxLayout(self.widget_form_residencia)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.label_residencia = QLabel(self.widget_form_residencia)
        self.label_residencia.setObjectName(u"label_residencia")

        self.verticalLayout_8.addWidget(self.label_residencia, 0, Qt.AlignLeft)

        self.lineEdit_residencia = QLineEdit(self.widget_form_residencia)
        self.lineEdit_residencia.setObjectName(u"lineEdit_residencia")
        self.lineEdit_residencia.setMinimumSize(QSize(161, 31))
        self.lineEdit_residencia.setMaximumSize(QSize(201, 50))

        self.verticalLayout_8.addWidget(self.lineEdit_residencia)


        self.gridLayout.addWidget(self.widget_form_residencia, 0, 2, 1, 1)

        self.widget_form_5 = QWidget(self.frame)
        self.widget_form_5.setObjectName(u"widget_form_5")
        self.widget_form_5.setMinimumSize(QSize(161, 0))
        self.widget_form_5.setMaximumSize(QSize(201, 55))
        self.verticalLayout_9 = QVBoxLayout(self.widget_form_5)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.widget_form_5)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_9.addWidget(self.label_2, 0, Qt.AlignLeft)

        self.lineEdit_2 = QLineEdit(self.widget_form_5)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setMinimumSize(QSize(161, 31))
        self.lineEdit_2.setMaximumSize(QSize(201, 50))

        self.verticalLayout_9.addWidget(self.lineEdit_2)


        self.gridLayout.addWidget(self.widget_form_5, 0, 3, 1, 1)

        self.widget_form_6 = QWidget(self.frame)
        self.widget_form_6.setObjectName(u"widget_form_6")
        self.widget_form_6.setMinimumSize(QSize(161, 0))
        self.widget_form_6.setMaximumSize(QSize(201, 55))
        self.verticalLayout_10 = QVBoxLayout(self.widget_form_6)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.widget_form_6)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_10.addWidget(self.label_3, 0, Qt.AlignLeft)

        self.dateEdit = QDateEdit(self.widget_form_6)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setMinimumSize(QSize(161, 31))
        self.dateEdit.setMaximumSize(QSize(201, 50))
        self.dateEdit.setCalendarPopup(True)

        self.verticalLayout_10.addWidget(self.dateEdit)


        self.gridLayout.addWidget(self.widget_form_6, 1, 0, 1, 1)

        self.widget_form_7 = QWidget(self.frame)
        self.widget_form_7.setObjectName(u"widget_form_7")
        self.widget_form_7.setMinimumSize(QSize(161, 0))
        self.widget_form_7.setMaximumSize(QSize(201, 55))
        self.verticalLayout_11 = QVBoxLayout(self.widget_form_7)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.widget_form_7)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_11.addWidget(self.label_4, 0, Qt.AlignLeft)

        self.lineEdit_3 = QLineEdit(self.widget_form_7)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setMinimumSize(QSize(161, 31))
        self.lineEdit_3.setMaximumSize(QSize(201, 50))

        self.verticalLayout_11.addWidget(self.lineEdit_3)


        self.gridLayout.addWidget(self.widget_form_7, 1, 1, 1, 1)

        self.widget_form_8 = QWidget(self.frame)
        self.widget_form_8.setObjectName(u"widget_form_8")
        self.widget_form_8.setMaximumSize(QSize(16777215, 55))
        self.verticalLayout_12 = QVBoxLayout(self.widget_form_8)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.widget_form_8)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_12.addWidget(self.label_5, 0, Qt.AlignLeft)

        self.comboBox = QComboBox(self.widget_form_8)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setMinimumSize(QSize(0, 31))
        self.comboBox.setMaximumSize(QSize(16777215, 50))
        self.comboBox.setEditable(True)

        self.verticalLayout_12.addWidget(self.comboBox)


        self.gridLayout.addWidget(self.widget_form_8, 1, 2, 1, 2)


        self.verticalLayout_3.addWidget(self.frame)


        self.verticalLayout_5.addWidget(self.frame_form)

        self.frame_form_2 = QFrame(self.frame_principal)
        self.frame_form_2.setObjectName(u"frame_form_2")
        self.frame_form_2.setMinimumSize(QSize(821, 151))
        self.frame_form_2.setMaximumSize(QSize(911, 181))
        self.frame_form_2.setFrameShape(QFrame.StyledPanel)
        self.frame_form_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_form_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_icon_car = QLabel(self.frame_form_2)
        self.label_icon_car.setObjectName(u"label_icon_car")
        self.label_icon_car.setMinimumSize(QSize(41, 51))
        self.label_icon_car.setMaximumSize(QSize(61, 61))
        self.label_icon_car.setScaledContents(True)

        self.horizontalLayout_2.addWidget(self.label_icon_car)

        self.label_datos_del_vehiculo = QLabel(self.frame_form_2)
        self.label_datos_del_vehiculo.setObjectName(u"label_datos_del_vehiculo")

        self.horizontalLayout_2.addWidget(self.label_datos_del_vehiculo, 0, Qt.AlignLeft)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.pushButton = QPushButton(self.frame_form_2)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(101, 31))
        self.pushButton.setMaximumSize(QSize(101, 31))

        self.horizontalLayout_2.addWidget(self.pushButton)


        self.verticalLayout_4.addLayout(self.horizontalLayout_2)

        self.frame_2 = QFrame(self.frame_form_2)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMaximumSize(QSize(871, 171))
        self.gridLayout_2 = QGridLayout(self.frame_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setHorizontalSpacing(6)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.widget_form_apellido_2 = QWidget(self.frame_2)
        self.widget_form_apellido_2.setObjectName(u"widget_form_apellido_2")
        self.widget_form_apellido_2.setMinimumSize(QSize(161, 0))
        self.widget_form_apellido_2.setMaximumSize(QSize(201, 55))
        self.verticalLayout_14 = QVBoxLayout(self.widget_form_apellido_2)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.label_modelo = QLabel(self.widget_form_apellido_2)
        self.label_modelo.setObjectName(u"label_modelo")

        self.verticalLayout_14.addWidget(self.label_modelo, 0, Qt.AlignLeft)

        self.lineEdit_modelo_vehiculo = QLineEdit(self.widget_form_apellido_2)
        self.lineEdit_modelo_vehiculo.setObjectName(u"lineEdit_modelo_vehiculo")
        self.lineEdit_modelo_vehiculo.setMinimumSize(QSize(161, 31))
        self.lineEdit_modelo_vehiculo.setMaximumSize(QSize(201, 50))

        self.verticalLayout_14.addWidget(self.lineEdit_modelo_vehiculo)


        self.gridLayout_2.addWidget(self.widget_form_apellido_2, 0, 1, 1, 1)

        self.widget_form_vehiculo = QWidget(self.frame_2)
        self.widget_form_vehiculo.setObjectName(u"widget_form_vehiculo")
        self.widget_form_vehiculo.setMinimumSize(QSize(161, 0))
        self.widget_form_vehiculo.setMaximumSize(QSize(201, 55))
        self.verticalLayout_13 = QVBoxLayout(self.widget_form_vehiculo)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.label_tipo_vehiculo = QLabel(self.widget_form_vehiculo)
        self.label_tipo_vehiculo.setObjectName(u"label_tipo_vehiculo")

        self.verticalLayout_13.addWidget(self.label_tipo_vehiculo, 0, Qt.AlignLeft)

        self.comboBox_tipo_vehiculo = QComboBox(self.widget_form_vehiculo)
        self.comboBox_tipo_vehiculo.addItem("")
        self.comboBox_tipo_vehiculo.addItem("")
        self.comboBox_tipo_vehiculo.setObjectName(u"comboBox_tipo_vehiculo")
        self.comboBox_tipo_vehiculo.setMinimumSize(QSize(161, 31))
        self.comboBox_tipo_vehiculo.setMaximumSize(QSize(201, 50))
        self.comboBox_tipo_vehiculo.setEditable(True)
        self.comboBox_tipo_vehiculo.setFrame(False)

        self.verticalLayout_13.addWidget(self.comboBox_tipo_vehiculo)


        self.gridLayout_2.addWidget(self.widget_form_vehiculo, 0, 0, 1, 1)

        self.widget_form_placa = QWidget(self.frame_2)
        self.widget_form_placa.setObjectName(u"widget_form_placa")
        self.widget_form_placa.setMinimumSize(QSize(161, 0))
        self.widget_form_placa.setMaximumSize(QSize(201, 55))
        self.verticalLayout_15 = QVBoxLayout(self.widget_form_placa)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.label_placa_vehiculo = QLabel(self.widget_form_placa)
        self.label_placa_vehiculo.setObjectName(u"label_placa_vehiculo")

        self.verticalLayout_15.addWidget(self.label_placa_vehiculo, 0, Qt.AlignLeft)

        self.lineEdit_placa_vehiculo = QLineEdit(self.widget_form_placa)
        self.lineEdit_placa_vehiculo.setObjectName(u"lineEdit_placa_vehiculo")
        self.lineEdit_placa_vehiculo.setMinimumSize(QSize(161, 31))
        self.lineEdit_placa_vehiculo.setMaximumSize(QSize(201, 50))

        self.verticalLayout_15.addWidget(self.lineEdit_placa_vehiculo)


        self.gridLayout_2.addWidget(self.widget_form_placa, 0, 2, 1, 1)

        self.widget_form_color_vehiculo = QWidget(self.frame_2)
        self.widget_form_color_vehiculo.setObjectName(u"widget_form_color_vehiculo")
        self.widget_form_color_vehiculo.setMinimumSize(QSize(161, 0))
        self.widget_form_color_vehiculo.setMaximumSize(QSize(201, 55))
        self.verticalLayout_16 = QVBoxLayout(self.widget_form_color_vehiculo)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.label_9 = QLabel(self.widget_form_color_vehiculo)
        self.label_9.setObjectName(u"label_9")

        self.verticalLayout_16.addWidget(self.label_9, 0, Qt.AlignLeft)

        self.lineEdit_color_vehiculo = QLineEdit(self.widget_form_color_vehiculo)
        self.lineEdit_color_vehiculo.setObjectName(u"lineEdit_color_vehiculo")
        self.lineEdit_color_vehiculo.setMinimumSize(QSize(161, 31))
        self.lineEdit_color_vehiculo.setMaximumSize(QSize(201, 50))

        self.verticalLayout_16.addWidget(self.lineEdit_color_vehiculo)


        self.gridLayout_2.addWidget(self.widget_form_color_vehiculo, 0, 3, 1, 1)


        self.verticalLayout_4.addWidget(self.frame_2)


        self.verticalLayout_5.addWidget(self.frame_form_2)


        self.gridLayout_3.addLayout(self.verticalLayout_5, 0, 0, 1, 2)

        self.horizontalSpacer_3 = QSpacerItem(124, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_3, 0, 2, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 302, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer, 1, 1, 1, 1)


        self.verticalLayout_2.addWidget(self.frame_principal)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.scrollArea)


        self.retranslateUi(PantallaMultasView)

        QMetaObject.connectSlotsByName(PantallaMultasView)
    # setupUi

    def retranslateUi(self, PantallaMultasView):
        PantallaMultasView.setWindowTitle(QCoreApplication.translate("PantallaMultasView", u"Form", None))
        self.frame_principal.setProperty("tipo", QCoreApplication.translate("PantallaMultasView", u"frame_principal", None))
        self.frame_form.setProperty("tipo", QCoreApplication.translate("PantallaMultasView", u"frame_form", None))
        self.label_icon_person.setText("")
        self.label_datos_multado.setText(QCoreApplication.translate("PantallaMultasView", u"Datos del multado", None))
        self.label_datos_multado.setProperty("tipo", QCoreApplication.translate("PantallaMultasView", u"titulo_form", None))
        self.label_nombre.setText(QCoreApplication.translate("PantallaMultasView", u"Nombre", None))
        self.label_nombre.setProperty("tipo", QCoreApplication.translate("PantallaMultasView", u"titulo_qlineedit", None))
        self.lineEdit_nombre.setText("")
        self.lineEdit_nombre.setProperty("tipo", "")
        self.label_apellido.setText(QCoreApplication.translate("PantallaMultasView", u"Apellido", None))
        self.label_apellido.setProperty("tipo", QCoreApplication.translate("PantallaMultasView", u"titulo_qlineedit", None))
        self.lineEdit_apellido.setText("")
        self.lineEdit_apellido.setProperty("tipo", "")
        self.label_residencia.setText(QCoreApplication.translate("PantallaMultasView", u"Residencia", None))
        self.label_residencia.setProperty("tipo", QCoreApplication.translate("PantallaMultasView", u"titulo_qlineedit", None))
        self.lineEdit_residencia.setText("")
        self.lineEdit_residencia.setProperty("tipo", "")
        self.label_2.setText(QCoreApplication.translate("PantallaMultasView", u"Lugar del acontecimiento", None))
        self.label_2.setProperty("tipo", QCoreApplication.translate("PantallaMultasView", u"titulo_qlineedit", None))
        self.lineEdit_2.setText("")
        self.lineEdit_2.setProperty("tipo", "")
        self.label_3.setText(QCoreApplication.translate("PantallaMultasView", u"Fecha de la multa", None))
        self.label_3.setProperty("tipo", QCoreApplication.translate("PantallaMultasView", u"titulo_qlineedit", None))
        self.dateEdit.setDisplayFormat(QCoreApplication.translate("PantallaMultasView", u"MM/dd/yyyy", None))
        self.label_4.setText(QCoreApplication.translate("PantallaMultasView", u"Monto a cancelar", None))
        self.label_4.setProperty("tipo", QCoreApplication.translate("PantallaMultasView", u"titulo_qlineedit", None))
        self.lineEdit_3.setText("")
        self.lineEdit_3.setProperty("tipo", "")
        self.label_5.setText(QCoreApplication.translate("PantallaMultasView", u"Motivo de la multa", None))
        self.label_5.setProperty("tipo", QCoreApplication.translate("PantallaMultasView", u"titulo_qlineedit", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("PantallaMultasView", u"Sin dispositivo de seguridad (sin casco)", None))
        self.comboBox.setItemText(1, "")
        self.comboBox.setItemText(2, QCoreApplication.translate("PantallaMultasView", u"Sin dispositivo de seguridad (sin encerado)", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("PantallaMultasView", u"Transitar en lugar no permitido", None))

        self.frame_form_2.setProperty("tipo", QCoreApplication.translate("PantallaMultasView", u"frame_form", None))
        self.label_icon_car.setText("")
        self.label_icon_car.setProperty("tipo", QCoreApplication.translate("PantallaMultasView", u"icon_person", None))
        self.label_datos_del_vehiculo.setText(QCoreApplication.translate("PantallaMultasView", u"Datos del vehiculo", None))
        self.label_datos_del_vehiculo.setProperty("tipo", QCoreApplication.translate("PantallaMultasView", u"titulo_form", None))
        self.pushButton.setText(QCoreApplication.translate("PantallaMultasView", u"agregar", None))
        self.label_modelo.setText(QCoreApplication.translate("PantallaMultasView", u"Modelo", None))
        self.label_modelo.setProperty("tipo", QCoreApplication.translate("PantallaMultasView", u"titulo_qlineedit", None))
        self.lineEdit_modelo_vehiculo.setText("")
        self.lineEdit_modelo_vehiculo.setProperty("tipo", "")
        self.label_tipo_vehiculo.setText(QCoreApplication.translate("PantallaMultasView", u"Tipo", None))
        self.label_tipo_vehiculo.setProperty("tipo", QCoreApplication.translate("PantallaMultasView", u"titulo_qlineedit", None))
        self.comboBox_tipo_vehiculo.setItemText(0, "")
        self.comboBox_tipo_vehiculo.setItemText(1, QCoreApplication.translate("PantallaMultasView", u"Moto", None))

        self.label_placa_vehiculo.setText(QCoreApplication.translate("PantallaMultasView", u"Placa", None))
        self.label_placa_vehiculo.setProperty("tipo", QCoreApplication.translate("PantallaMultasView", u"titulo_qlineedit", None))
        self.lineEdit_placa_vehiculo.setText("")
        self.lineEdit_placa_vehiculo.setProperty("tipo", "")
        self.label_9.setText(QCoreApplication.translate("PantallaMultasView", u"Color", None))
        self.label_9.setProperty("tipo", QCoreApplication.translate("PantallaMultasView", u"titulo_qlineedit", None))
        self.lineEdit_color_vehiculo.setText("")
        self.lineEdit_color_vehiculo.setProperty("tipo", "")
    # retranslateUi

