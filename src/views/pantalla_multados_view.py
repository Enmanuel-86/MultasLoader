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

import resources_rc

class Ui_PantallaMultasView(object):
    def setupUi(self, PantallaMultasView):
        if not PantallaMultasView.objectName():
            PantallaMultasView.setObjectName(u"PantallaMultasView")
        PantallaMultasView.resize(1040, 556)
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
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 1181, 537))
        self.verticalLayout_2 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_principal = QFrame(self.scrollAreaWidgetContents)
        self.frame_principal.setObjectName(u"frame_principal")
        self.frame_principal.setFrameShape(QFrame.StyledPanel)
        self.frame_principal.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_principal)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.frame_contenedor = QFrame(self.frame_principal)
        self.frame_contenedor.setObjectName(u"frame_contenedor")
        self.frame_contenedor.setMinimumSize(QSize(0, 381))
        self.frame_contenedor.setMaximumSize(QSize(16777215, 391))
        self.verticalLayout_5 = QVBoxLayout(self.frame_contenedor)
        self.verticalLayout_5.setSpacing(6)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_form = QFrame(self.frame_contenedor)
        self.frame_form.setObjectName(u"frame_form")
        self.frame_form.setMinimumSize(QSize(821, 221))
        self.frame_form.setMaximumSize(QSize(16777215, 221))
        self.frame_form.setFrameShape(QFrame.NoFrame)
        self.frame_form.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_form)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame_titulo_2 = QFrame(self.frame_form)
        self.frame_titulo_2.setObjectName(u"frame_titulo_2")
        self.frame_titulo_2.setMinimumSize(QSize(0, 51))
        self.frame_titulo_2.setMaximumSize(QSize(16777215, 51))
        self.horizontalLayout = QHBoxLayout(self.frame_titulo_2)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_icon_person = QLabel(self.frame_titulo_2)
        self.label_icon_person.setObjectName(u"label_icon_person")
        self.label_icon_person.setMinimumSize(QSize(41, 51))
        self.label_icon_person.setMaximumSize(QSize(61, 61))
        self.label_icon_person.setScaledContents(True)

        self.horizontalLayout.addWidget(self.label_icon_person)

        self.label_datos_multado = QLabel(self.frame_titulo_2)
        self.label_datos_multado.setObjectName(u"label_datos_multado")

        self.horizontalLayout.addWidget(self.label_datos_multado, 0, Qt.AlignLeft)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout_3.addWidget(self.frame_titulo_2)

        self.frame = QFrame(self.frame_form)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(701, 121))
        self.frame.setMaximumSize(QSize(16777215, 121))
        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(6)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.widget_form_nombre = QWidget(self.frame)
        self.widget_form_nombre.setObjectName(u"widget_form_nombre")
        self.widget_form_nombre.setMinimumSize(QSize(161, 0))
        self.widget_form_nombre.setMaximumSize(QSize(16777215, 55))
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
        self.lineEdit_nombre.setMaximumSize(QSize(16777215, 50))

        self.verticalLayout_6.addWidget(self.lineEdit_nombre)


        self.gridLayout.addWidget(self.widget_form_nombre, 0, 0, 1, 1)

        self.widget_form_apellido = QWidget(self.frame)
        self.widget_form_apellido.setObjectName(u"widget_form_apellido")
        self.widget_form_apellido.setMinimumSize(QSize(161, 0))
        self.widget_form_apellido.setMaximumSize(QSize(16777215, 55))
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
        self.lineEdit_apellido.setMaximumSize(QSize(16777215, 50))

        self.verticalLayout_7.addWidget(self.lineEdit_apellido)


        self.gridLayout.addWidget(self.widget_form_apellido, 0, 1, 1, 1)

        self.widget_form_residencia = QWidget(self.frame)
        self.widget_form_residencia.setObjectName(u"widget_form_residencia")
        self.widget_form_residencia.setMinimumSize(QSize(161, 0))
        self.widget_form_residencia.setMaximumSize(QSize(16777215, 55))
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
        self.lineEdit_residencia.setMaximumSize(QSize(16777215, 50))

        self.verticalLayout_8.addWidget(self.lineEdit_residencia)


        self.gridLayout.addWidget(self.widget_form_residencia, 0, 2, 1, 1)

        self.widget_form_5 = QWidget(self.frame)
        self.widget_form_5.setObjectName(u"widget_form_5")
        self.widget_form_5.setMinimumSize(QSize(161, 0))
        self.widget_form_5.setMaximumSize(QSize(16777215, 55))
        self.verticalLayout_9 = QVBoxLayout(self.widget_form_5)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.label_lugar_acontecimiento = QLabel(self.widget_form_5)
        self.label_lugar_acontecimiento.setObjectName(u"label_lugar_acontecimiento")

        self.verticalLayout_9.addWidget(self.label_lugar_acontecimiento, 0, Qt.AlignLeft)

        self.lineEdit_lugar_acontecimiento = QLineEdit(self.widget_form_5)
        self.lineEdit_lugar_acontecimiento.setObjectName(u"lineEdit_lugar_acontecimiento")
        self.lineEdit_lugar_acontecimiento.setMinimumSize(QSize(161, 31))
        self.lineEdit_lugar_acontecimiento.setMaximumSize(QSize(16777215, 50))

        self.verticalLayout_9.addWidget(self.lineEdit_lugar_acontecimiento)


        self.gridLayout.addWidget(self.widget_form_5, 0, 3, 1, 1)

        self.widget_form_6 = QWidget(self.frame)
        self.widget_form_6.setObjectName(u"widget_form_6")
        self.widget_form_6.setMinimumSize(QSize(161, 0))
        self.widget_form_6.setMaximumSize(QSize(16777215, 55))
        self.verticalLayout_10 = QVBoxLayout(self.widget_form_6)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.label_fecha_multa = QLabel(self.widget_form_6)
        self.label_fecha_multa.setObjectName(u"label_fecha_multa")

        self.verticalLayout_10.addWidget(self.label_fecha_multa, 0, Qt.AlignLeft)

        self.dateEdit_fecha_multa = QDateEdit(self.widget_form_6)
        self.dateEdit_fecha_multa.setObjectName(u"dateEdit_fecha_multa")
        self.dateEdit_fecha_multa.setMinimumSize(QSize(161, 31))
        self.dateEdit_fecha_multa.setMaximumSize(QSize(16777215, 50))
        self.dateEdit_fecha_multa.setCalendarPopup(True)

        self.verticalLayout_10.addWidget(self.dateEdit_fecha_multa)


        self.gridLayout.addWidget(self.widget_form_6, 1, 0, 1, 1)

        self.widget_form_7 = QWidget(self.frame)
        self.widget_form_7.setObjectName(u"widget_form_7")
        self.widget_form_7.setMinimumSize(QSize(161, 0))
        self.widget_form_7.setMaximumSize(QSize(16777215, 55))
        self.verticalLayout_11 = QVBoxLayout(self.widget_form_7)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.label_monto_cancelar = QLabel(self.widget_form_7)
        self.label_monto_cancelar.setObjectName(u"label_monto_cancelar")

        self.verticalLayout_11.addWidget(self.label_monto_cancelar, 0, Qt.AlignLeft)

        self.lineEdit_monto_cancelar = QLineEdit(self.widget_form_7)
        self.lineEdit_monto_cancelar.setObjectName(u"lineEdit_monto_cancelar")
        self.lineEdit_monto_cancelar.setMinimumSize(QSize(161, 31))
        self.lineEdit_monto_cancelar.setMaximumSize(QSize(16777215, 50))
        self.lineEdit_monto_cancelar.setFrame(True)
        self.lineEdit_monto_cancelar.setEchoMode(QLineEdit.Normal)

        self.verticalLayout_11.addWidget(self.lineEdit_monto_cancelar)


        self.gridLayout.addWidget(self.widget_form_7, 1, 1, 1, 1)

        self.widget_form_8 = QWidget(self.frame)
        self.widget_form_8.setObjectName(u"widget_form_8")
        self.widget_form_8.setMaximumSize(QSize(16777215, 55))
        self.verticalLayout_12 = QVBoxLayout(self.widget_form_8)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.label_motivo_multa = QLabel(self.widget_form_8)
        self.label_motivo_multa.setObjectName(u"label_motivo_multa")

        self.verticalLayout_12.addWidget(self.label_motivo_multa, 0, Qt.AlignLeft)

        self.comboBox_motivo_multa = QComboBox(self.widget_form_8)
        self.comboBox_motivo_multa.addItem("")
        self.comboBox_motivo_multa.addItem("")
        self.comboBox_motivo_multa.addItem("")
        self.comboBox_motivo_multa.addItem("")
        self.comboBox_motivo_multa.setObjectName(u"comboBox_motivo_multa")
        self.comboBox_motivo_multa.setMinimumSize(QSize(0, 31))
        self.comboBox_motivo_multa.setMaximumSize(QSize(16777215, 50))
        self.comboBox_motivo_multa.setEditable(True)

        self.verticalLayout_12.addWidget(self.comboBox_motivo_multa)


        self.gridLayout.addWidget(self.widget_form_8, 1, 2, 1, 2)


        self.verticalLayout_3.addWidget(self.frame)


        self.verticalLayout_5.addWidget(self.frame_form)

        self.frame_form_datos_vehiculo = QFrame(self.frame_contenedor)
        self.frame_form_datos_vehiculo.setObjectName(u"frame_form_datos_vehiculo")
        self.frame_form_datos_vehiculo.setMaximumSize(QSize(16777215, 146))
        self.frame_form_datos_vehiculo.setFrameShape(QFrame.NoFrame)
        self.frame_form_datos_vehiculo.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_form_datos_vehiculo)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.frame_titulo = QFrame(self.frame_form_datos_vehiculo)
        self.frame_titulo.setObjectName(u"frame_titulo")
        self.frame_titulo.setMinimumSize(QSize(0, 51))
        self.frame_titulo.setMaximumSize(QSize(16777215, 51))
        self.horizontalLayout_2 = QHBoxLayout(self.frame_titulo)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_icon_car = QLabel(self.frame_titulo)
        self.label_icon_car.setObjectName(u"label_icon_car")
        self.label_icon_car.setMinimumSize(QSize(41, 51))
        self.label_icon_car.setMaximumSize(QSize(61, 61))
        self.label_icon_car.setScaledContents(True)

        self.horizontalLayout_2.addWidget(self.label_icon_car, 0, Qt.AlignVCenter)

        self.label_datos_del_vehiculo = QLabel(self.frame_titulo)
        self.label_datos_del_vehiculo.setObjectName(u"label_datos_del_vehiculo")

        self.horizontalLayout_2.addWidget(self.label_datos_del_vehiculo, 0, Qt.AlignLeft)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.pushButton = QPushButton(self.frame_titulo)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(101, 31))
        self.pushButton.setMaximumSize(QSize(101, 31))

        self.horizontalLayout_2.addWidget(self.pushButton)


        self.verticalLayout_4.addWidget(self.frame_titulo)

        self.frame_2 = QFrame(self.frame_form_datos_vehiculo)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(0, 51))
        self.frame_2.setMaximumSize(QSize(16777215, 51))
        self.horizontalLayout_4 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_4.setSpacing(6)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.widget_form_vehiculo = QWidget(self.frame_2)
        self.widget_form_vehiculo.setObjectName(u"widget_form_vehiculo")
        self.widget_form_vehiculo.setMinimumSize(QSize(161, 0))
        self.widget_form_vehiculo.setMaximumSize(QSize(16777215, 55))
        self.verticalLayout_13 = QVBoxLayout(self.widget_form_vehiculo)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.label_tipo_vehiculo = QLabel(self.widget_form_vehiculo)
        self.label_tipo_vehiculo.setObjectName(u"label_tipo_vehiculo")

        self.verticalLayout_13.addWidget(self.label_tipo_vehiculo)

        self.comboBox_tipo_vehiculo = QComboBox(self.widget_form_vehiculo)
        self.comboBox_tipo_vehiculo.addItem("")
        self.comboBox_tipo_vehiculo.addItem("")
        self.comboBox_tipo_vehiculo.setObjectName(u"comboBox_tipo_vehiculo")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_tipo_vehiculo.sizePolicy().hasHeightForWidth())
        self.comboBox_tipo_vehiculo.setSizePolicy(sizePolicy)
        self.comboBox_tipo_vehiculo.setMinimumSize(QSize(161, 31))
        self.comboBox_tipo_vehiculo.setMaximumSize(QSize(16777215, 50))
        self.comboBox_tipo_vehiculo.setEditable(True)
        self.comboBox_tipo_vehiculo.setFrame(False)

        self.verticalLayout_13.addWidget(self.comboBox_tipo_vehiculo)


        self.horizontalLayout_4.addWidget(self.widget_form_vehiculo)

        self.widget_form_apellido_2 = QWidget(self.frame_2)
        self.widget_form_apellido_2.setObjectName(u"widget_form_apellido_2")
        self.widget_form_apellido_2.setMinimumSize(QSize(161, 0))
        self.widget_form_apellido_2.setMaximumSize(QSize(16777215, 55))
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
        self.lineEdit_modelo_vehiculo.setMaximumSize(QSize(16777215, 50))

        self.verticalLayout_14.addWidget(self.lineEdit_modelo_vehiculo)


        self.horizontalLayout_4.addWidget(self.widget_form_apellido_2)

        self.widget_form_placa = QWidget(self.frame_2)
        self.widget_form_placa.setObjectName(u"widget_form_placa")
        self.widget_form_placa.setMinimumSize(QSize(161, 0))
        self.widget_form_placa.setMaximumSize(QSize(16777215, 55))
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
        self.lineEdit_placa_vehiculo.setMaximumSize(QSize(16777215, 50))

        self.verticalLayout_15.addWidget(self.lineEdit_placa_vehiculo)


        self.horizontalLayout_4.addWidget(self.widget_form_placa)

        self.widget_form_color_vehiculo = QWidget(self.frame_2)
        self.widget_form_color_vehiculo.setObjectName(u"widget_form_color_vehiculo")
        self.widget_form_color_vehiculo.setMinimumSize(QSize(161, 0))
        self.widget_form_color_vehiculo.setMaximumSize(QSize(16777215, 55))
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
        self.lineEdit_color_vehiculo.setMaximumSize(QSize(16777215, 50))

        self.verticalLayout_16.addWidget(self.lineEdit_color_vehiculo)


        self.horizontalLayout_4.addWidget(self.widget_form_color_vehiculo)


        self.verticalLayout_4.addWidget(self.frame_2)


        self.verticalLayout_5.addWidget(self.frame_form_datos_vehiculo)


        self.gridLayout_2.addWidget(self.frame_contenedor, 0, 0, 1, 1)

        self.frame_lista_multados = QFrame(self.frame_principal)
        self.frame_lista_multados.setObjectName(u"frame_lista_multados")
        self.frame_lista_multados.setMinimumSize(QSize(334, 371))
        self.frame_lista_multados.setMaximumSize(QSize(399, 371))
        self.frame_lista_multados.setFrameShape(QFrame.StyledPanel)
        self.frame_lista_multados.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_lista_multados)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_icon_list = QLabel(self.frame_lista_multados)
        self.label_icon_list.setObjectName(u"label_icon_list")
        self.label_icon_list.setMinimumSize(QSize(41, 51))
        self.label_icon_list.setMaximumSize(QSize(61, 61))
        self.label_icon_list.setScaledContents(True)

        self.horizontalLayout_3.addWidget(self.label_icon_list)

        self.label_datos_multado_2 = QLabel(self.frame_lista_multados)
        self.label_datos_multado_2.setObjectName(u"label_datos_multado_2")

        self.horizontalLayout_3.addWidget(self.label_datos_multado_2)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)


        self.verticalLayout_17.addLayout(self.horizontalLayout_3)

        self.listWidget_multados_pendientes = QListWidget(self.frame_lista_multados)
        QListWidgetItem(self.listWidget_multados_pendientes)
        QListWidgetItem(self.listWidget_multados_pendientes)
        QListWidgetItem(self.listWidget_multados_pendientes)
        QListWidgetItem(self.listWidget_multados_pendientes)
        self.listWidget_multados_pendientes.setObjectName(u"listWidget_multados_pendientes")

        self.verticalLayout_17.addWidget(self.listWidget_multados_pendientes)


        self.gridLayout_2.addWidget(self.frame_lista_multados, 0, 1, 1, 1)

        self.frame_3 = QFrame(self.frame_principal)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)

        self.gridLayout_2.addWidget(self.frame_3, 1, 0, 1, 2)


        self.verticalLayout_2.addWidget(self.frame_principal)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.scrollArea)

        QWidget.setTabOrder(self.lineEdit_nombre, self.lineEdit_apellido)
        QWidget.setTabOrder(self.lineEdit_apellido, self.lineEdit_residencia)
        QWidget.setTabOrder(self.lineEdit_residencia, self.lineEdit_lugar_acontecimiento)
        QWidget.setTabOrder(self.lineEdit_lugar_acontecimiento, self.dateEdit_fecha_multa)
        QWidget.setTabOrder(self.dateEdit_fecha_multa, self.lineEdit_monto_cancelar)
        QWidget.setTabOrder(self.lineEdit_monto_cancelar, self.comboBox_motivo_multa)
        QWidget.setTabOrder(self.comboBox_motivo_multa, self.comboBox_tipo_vehiculo)
        QWidget.setTabOrder(self.comboBox_tipo_vehiculo, self.lineEdit_modelo_vehiculo)
        QWidget.setTabOrder(self.lineEdit_modelo_vehiculo, self.lineEdit_placa_vehiculo)
        QWidget.setTabOrder(self.lineEdit_placa_vehiculo, self.lineEdit_color_vehiculo)
        QWidget.setTabOrder(self.lineEdit_color_vehiculo, self.scrollArea)
        QWidget.setTabOrder(self.scrollArea, self.pushButton)
        QWidget.setTabOrder(self.pushButton, self.listWidget_multados_pendientes)

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
        self.label_lugar_acontecimiento.setText(QCoreApplication.translate("PantallaMultasView", u"Lugar del acontecimiento", None))
        self.label_lugar_acontecimiento.setProperty("tipo", QCoreApplication.translate("PantallaMultasView", u"titulo_qlineedit", None))
        self.lineEdit_lugar_acontecimiento.setText("")
        self.lineEdit_lugar_acontecimiento.setProperty("tipo", "")
        self.label_fecha_multa.setText(QCoreApplication.translate("PantallaMultasView", u"Fecha de la multa", None))
        self.label_fecha_multa.setProperty("tipo", QCoreApplication.translate("PantallaMultasView", u"titulo_qlineedit", None))
        self.dateEdit_fecha_multa.setDisplayFormat(QCoreApplication.translate("PantallaMultasView", u"MM/dd/yyyy", None))
        self.label_monto_cancelar.setText(QCoreApplication.translate("PantallaMultasView", u"Monto a cancelar", None))
        self.label_monto_cancelar.setProperty("tipo", QCoreApplication.translate("PantallaMultasView", u"titulo_qlineedit", None))
        self.lineEdit_monto_cancelar.setText("")
        self.lineEdit_monto_cancelar.setProperty("tipo", "")
        self.label_motivo_multa.setText(QCoreApplication.translate("PantallaMultasView", u"Motivo de la multa", None))
        self.label_motivo_multa.setProperty("tipo", QCoreApplication.translate("PantallaMultasView", u"titulo_qlineedit", None))
        self.comboBox_motivo_multa.setItemText(0, "")
        self.comboBox_motivo_multa.setItemText(1, QCoreApplication.translate("PantallaMultasView", u"Sin dispositivo de seguridad (sin casco)", None))
        self.comboBox_motivo_multa.setItemText(2, QCoreApplication.translate("PantallaMultasView", u"Sin dispositivo de seguridad (sin encerado)", None))
        self.comboBox_motivo_multa.setItemText(3, QCoreApplication.translate("PantallaMultasView", u"Transitar en lugar no permitido", None))

        self.frame_form_datos_vehiculo.setProperty("tipo", QCoreApplication.translate("PantallaMultasView", u"frame_form", None))
        self.label_icon_car.setText("")
        self.label_icon_car.setProperty("tipo", QCoreApplication.translate("PantallaMultasView", u"icon_person", None))
        self.label_datos_del_vehiculo.setText(QCoreApplication.translate("PantallaMultasView", u"Datos del vehiculo", None))
        self.label_datos_del_vehiculo.setProperty("tipo", QCoreApplication.translate("PantallaMultasView", u"titulo_form", None))
        self.pushButton.setText(QCoreApplication.translate("PantallaMultasView", u"agregar", None))
        self.label_tipo_vehiculo.setText(QCoreApplication.translate("PantallaMultasView", u"Tipo", None))
        self.label_tipo_vehiculo.setProperty("tipo", QCoreApplication.translate("PantallaMultasView", u"titulo_qlineedit", None))
        self.comboBox_tipo_vehiculo.setItemText(0, "")
        self.comboBox_tipo_vehiculo.setItemText(1, QCoreApplication.translate("PantallaMultasView", u"Moto", None))

        self.label_modelo.setText(QCoreApplication.translate("PantallaMultasView", u"Modelo", None))
        self.label_modelo.setProperty("tipo", QCoreApplication.translate("PantallaMultasView", u"titulo_qlineedit", None))
        self.lineEdit_modelo_vehiculo.setText("")
        self.lineEdit_modelo_vehiculo.setProperty("tipo", "")
        self.label_placa_vehiculo.setText(QCoreApplication.translate("PantallaMultasView", u"Placa", None))
        self.label_placa_vehiculo.setProperty("tipo", QCoreApplication.translate("PantallaMultasView", u"titulo_qlineedit", None))
        self.lineEdit_placa_vehiculo.setText("")
        self.lineEdit_placa_vehiculo.setProperty("tipo", "")
        self.label_9.setText(QCoreApplication.translate("PantallaMultasView", u"Color", None))
        self.label_9.setProperty("tipo", QCoreApplication.translate("PantallaMultasView", u"titulo_qlineedit", None))
        self.lineEdit_color_vehiculo.setText("")
        self.lineEdit_color_vehiculo.setProperty("tipo", "")
        self.frame_lista_multados.setProperty("tipo", QCoreApplication.translate("PantallaMultasView", u"frame_form", None))
        self.label_icon_list.setText("")
        self.label_datos_multado_2.setText(QCoreApplication.translate("PantallaMultasView", u"Datos del multado", None))
        self.label_datos_multado_2.setProperty("tipo", QCoreApplication.translate("PantallaMultasView", u"titulo_form", None))

        __sortingEnabled = self.listWidget_multados_pendientes.isSortingEnabled()
        self.listWidget_multados_pendientes.setSortingEnabled(False)
        ___qlistwidgetitem = self.listWidget_multados_pendientes.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("PantallaMultasView", u"Nuevo elemento", None));
        ___qlistwidgetitem1 = self.listWidget_multados_pendientes.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("PantallaMultasView", u"Nuevo elemento", None));
        ___qlistwidgetitem2 = self.listWidget_multados_pendientes.item(2)
        ___qlistwidgetitem2.setText(QCoreApplication.translate("PantallaMultasView", u"Nuevo elemento", None));
        ___qlistwidgetitem3 = self.listWidget_multados_pendientes.item(3)
        ___qlistwidgetitem3.setText(QCoreApplication.translate("PantallaMultasView", u"Nuevo elemento", None));
        self.listWidget_multados_pendientes.setSortingEnabled(__sortingEnabled)

        self.frame_3.setProperty("tipo", QCoreApplication.translate("PantallaMultasView", u"frame_form", None))
    # retranslateUi

