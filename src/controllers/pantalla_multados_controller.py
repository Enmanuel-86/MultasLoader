from views.pantalla_multados_view import Ui_PantallaMultasView
from PySide2.QtWidgets import (QWidget)

class PantallaMultadosController(QWidget, Ui_PantallaMultasView):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self._lista_qlineEdits:tuple =  (self.lineEdit_nombre, self.lineEdit_apellido, self.lineEdit_residencia,
                                         self.lineEdit_lugar_acontecimiento,self.lineEdit_monto_cancelar, self.lineEdit_color_vehiculo,
                                         self.lineEdit_placa_vehiculo, self.lineEdit_modelo_vehiculo
                                         )

        self._lista_qcombobox:tuple = (self.comboBox_motivo_multa, self.comboBox_tipo_vehiculo)

        self.pushButton.clicked.connect(lambda: self._agregar())

    def _agregar(self):
        nombre = self.lineEdit_nombre.text()
        print(nombre)