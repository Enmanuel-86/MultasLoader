from views.pantalla_multados_view import Ui_PantallaMultasView
from PySide2.QtWidgets import (QWidget, QMessageBox)
from PySide2.QtCore import (QDate) 
from  utils.funciones_sistema import funciones_sistema
import datetime

class PantallaMultadosController(QWidget, Ui_PantallaMultasView):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self._lista_qlineEdits:tuple =  (self.lineEdit_nombre, self.lineEdit_apellido, self.lineEdit_residencia,
                                         self.lineEdit_lugar_acontecimiento,self.lineEdit_monto_cancelar, self.lineEdit_color_vehiculo,
                                         self.lineEdit_placa_vehiculo, self.lineEdit_modelo_vehiculo
                                         )

        self._lista_qcombobox:tuple = (self.comboBox_motivo_multa, self.comboBox_tipo_vehiculo)

        self.dateEdit_fecha_multa.setDate(QDate.currentDate())

        self.pushButton_buscar.clicked.connect(self._verificar_registros_previos)
        self.pushButton_agregar_registro.clicked.connect(self._validar_campos)

    def _verificar_registros_previos(self):

        try:
            dict_errores:dict = {}
            cedula = self.lineEdit_cedula.text().strip()
            if cedula == "":
                dict_errores["cedula"] = "El campo no debe estar vacio"
            elif not cedula.isdigit():
                dict_errores["cedula"] = "El campo no puede contener letras"

            if len(dict_errores) > 0:
                raise
            else:

                if cedula == "123456789":  # si la persona ya estaba multada anteriormente

                    for campos in self._lista_qlineEdits:
                        campos.setEnabled(True)

                    for campos in self._lista_qcombobox:
                        campos.setEnabled(True)
                                
                    self.dateEdit_fecha_multa.setEnabled(True)
                    self.dateEdit_fecha_multa.setReadOnly(False)

                    self.lineEdit_nombre.setReadOnly(True)
                    self.lineEdit_apellido.setReadOnly(True)
                    self.lineEdit_nombre.setText("Juan")
                    self.lineEdit_apellido.setText("Perez")

                    self.pushButton_agregar_registro.setEnabled(True)

                    QMessageBox.warning(self, "La persona ya esta registrada", "Esta persona ya fue multada")
                else:
                    funciones_sistema.limpiar_campos_formulario(
                                                                lista_qlineedits_y_qlabel= self._lista_qlineEdits,
                                                                lista_qcombobox= self._lista_qcombobox,
                                                                )

                    for campos in self._lista_qlineEdits:
                        campos.setEnabled(True)

                    for campos in self._lista_qcombobox:
                        campos.setEnabled(True)
                                
                    self.dateEdit_fecha_multa.setEnabled(True)
                    self.dateEdit_fecha_multa.setReadOnly(False)

                    self.lineEdit_nombre.setReadOnly(False)
                    self.lineEdit_apellido.setReadOnly(False)

                    self.pushButton_agregar_registro.setEnabled(True)
        except:
            mensaje = ""
            for i, clave in enumerate(dict_errores):
                mensaje += f"{i+1}) {clave.capitalize()}: {dict_errores[clave]}.\n"
            
            QMessageBox.critical(self,
                                 "Errores en el formulario",
                                 mensaje
                                 )
            print(mensaje)


    
    def _validar_campos(self):

        try:
            tipo_documento = self.comboBox_tipo_cedula.currentText()
            cedula = self.lineEdit_cedula.text().strip()
            nombre =  self.lineEdit_nombre.text().strip()
            apellido = self.lineEdit_apellido.text().strip()
            residencia = self.lineEdit_residencia.text().strip()
            lugar_acontecimiento = self.lineEdit_lugar_acontecimiento.text().strip()
            fecha_multa = self.dateEdit_fecha_multa.text().strip()
            monto_a_cancelar = self.lineEdit_monto_cancelar.text().strip()
            motivo_de_multa = self.comboBox_motivo_multa.currentText()
            #tipo_vehiculo = self.comboBox_tipo_vehiculo.text().strip()
        except ValueError as e:
            print("Hay un error en la funcion validar campos")
            print(e)
        
        
        
        try:
            dict_errores:dict = {}
            dict_datos_multado:dict = {
                                        "tipo_documento": None,
                                        "cedula": None,
                                        "nombre": None,
                                        "apellido": None,
                                        "residencia": None,
                                        "lugar_acontecimiento": None,
                                        "fecha_multa": None,
                                        "monto_cancelar": None,
                                        "motivo_multa": None
                                        }


            if cedula == "":
                dict_errores["cedula"] = "El campo no debe estar vacio"
            elif not cedula.isdigit():
                dict_errores["cedula"] = "El campo no puede contener letras"

            if nombre == "":
                dict_errores["nombre"] = "El campo no debe estar vacio"
            if any(caracter.isdigit() for caracter in nombre):
                dict_errores["nombre"] = "El campo no puede contener numeros"

            if apellido == "":
                    dict_errores["apellido"] = "El campo no debe estar vacio"
            if any(caracter.isdigit() for caracter in apellido):
                dict_errores["apellido"] = "El campo no puede contener numeros"

            if residencia == "":
                dict_errores["residencia"] = "El campo no debe estar vacio"

            if lugar_acontecimiento == "":
                dict_errores["lugar del acontecimiento"] = "El campo no debe estar vacio"

            if monto_a_cancelar == "":
                dict_errores["monto a cancelar"] = "El campo no debe estar vacio"
            if not monto_a_cancelar.isdigit():
                dict_errores["monto a cancelar"] = "El campo no puede contener letras"

            if self.comboBox_motivo_multa.currentIndex() == 0 or motivo_de_multa == "":
                dict_errores["motivo de la multa"] = "El campo no debe estar vacio"
                
            """
                        
            
                        
            
                        
            
                        if fecha_multa == "":
                            dict_errores["fecha de la multa"] = "El campo no debe estar vacio"
            
                        
                        
            
                        
            
                        if tipo_vehiculo == "":
                            dict_errores["tipo de vehiculo"] = "El campo no debe estar vacio"
                        if any(caracter.isdigit() for caracter in tipo_vehiculo):
                            dict_errores["tipo de vehiculo"] = "El campo no puede contener numeros"
            
            """

            if len(dict_errores) > 0:
                raise
            else:

                dict_datos_multado["tipo_documento"] = tipo_documento
                dict_datos_multado["cedula"] = cedula
                dict_datos_multado["nombre"] = nombre.capitalize()
                dict_datos_multado["apellido"] = apellido.capitalize()
                dict_datos_multado["residencia"] = residencia.capitalize()
                dict_datos_multado["lugar_acontecimiento"] = lugar_acontecimiento.capitalize()
                dict_datos_multado["fecha_multa"] = fecha_multa.capitalize()
                dict_datos_multado["monto_cancelar"] = monto_a_cancelar.capitalize()
                dict_datos_multado["motivo_multa"] = motivo_de_multa.capitalize()

                # Una vez ya verificado los campos y sin tener errores podemos
                # registrar al multado


                print("\nNo hay errores en los campos del formulario")
                for i, clave in enumerate(dict_datos_multado):
                    print(f"{i+1}) {clave}: {dict_datos_multado[clave]}.")


            
            
        except:
            mensaje = ""
            for i, clave in enumerate(dict_errores):
                mensaje += f"{i+1}) {clave.capitalize()}: {dict_errores[clave]}.\n"
                
            QMessageBox.critical(self,
                                 "Errores en el formulario",
                                 mensaje
                                 )
            print(mensaje)
            