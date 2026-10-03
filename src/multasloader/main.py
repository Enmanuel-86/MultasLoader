from PySide2.QtWidgets import (QMainWindow,  QTabWidget, QApplication)
from utils.funciones_sistema import FuncionesAplicacion
from controllers.pantalla_multados_controller  import PantallaMultadosController

import sys
import images_resources_rc
sys.modules["images_resources_rc"] = images_resources_rc


class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("MultasLoader")

        # 1. Crear el QTabWidget contenedor principal
        self.tabs = QTabWidget()
        self.setCentralWidget(self.tabs)

        self.tabs.addTab(PantallaMultadosController(), "Multados")
        self.tabs.addTab(PantallaMultadosController(), "Multados23")
       



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = VentanaPrincipal()
    FuncionesAplicacion.cargar_estilos(app, ruta_archivo=  ":/stylesheets/stylesheet/style_blue_dark.qss")
    window.show()
    window.showMaximized()
    sys.exit(app.exec_())
