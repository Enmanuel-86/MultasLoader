from views.pantalla_multados_view import Ui_PantallaMultasView
from PySide2.QtWidgets import (QWidget)

class PantallaMultadosController(QWidget, Ui_PantallaMultasView):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pushButton.clicked.connect(lambda: self._agregar())

    def _agregar(self):
        nombre = self.lineEdit_nombre.text()
        print(nombre)