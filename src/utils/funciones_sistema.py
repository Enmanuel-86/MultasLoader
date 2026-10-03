import traceback
from PySide2.QtWidgets import QMessageBox, QListWidget, QListWidgetItem
from PySide2.QtCore import (QPropertyAnimation, QEasingCurve, QFile, QTextStream, QTime, Qt, QPoint)
from PySide2.QtGui import QIcon, QPixmap
import platform
import os
import io
from itertools import zip_longest


class FuncionesAplicacion:

    def cargar_estilos(app, ruta_archivo):
        """
            ### Este metodo sirve para cargar las hojas de estilo al sistema
            
            como todos los elementos de la pantalla tienen propiedades dinamicas, podemos usar hojas de estilos en archivos.qss para poder usarlo en el sistema
            
            Lo que se tiene que hacer es pasarle dos parametro:
            
            1. la variable que instacia toda la aplicacion.
            2. la ruta del archivo.qss (procurar que la hoja de estilo este en el archivo.qrc).
            
            **Ejemplo**
            
            
            si es para que los botones cambie entre estilos:
            ### Main.py
                
                
                ###
                if __name__ == "__main__":
                    app = QApplication(sys.argv)
                    window = MainWindow() # variable que instacia la aplicacion
                    FuncionSistema.cargar_estilos(window, ':/hojas_de_estilo/estilos/estilo_oscuro.qss')
                    window.show()
                    window.showMaximized()
                    sys.exit(app.exec_())
                    
            si es para que los botones cambie entre estilos:
            ### Desde donde tengas los botones
                
                ### 
                self.boton_tema_claro.clicked.connect(lambda: FuncionSistema.cargar_estilos(self, ':/hojas_de_estilo/estilos/estilo_default.qss'))
                self.boton_tema_oscuro.clicked.connect(lambda: FuncionSistema.cargar_estilos(self, ':/hojas_de_estilo/estilos/estilo_oscuro.qss'))
                
        """
        try:
            archivo = QFile(ruta_archivo)
            if archivo.open(QFile.ReadOnly | QFile.Text):
                stream = QTextStream(archivo)
                
                # Limpiamos primero el estilo
                app.setStyleSheet("")
                
                # asignamos el estilo
                app.setStyleSheet(stream.readAll())
                
                archivo.close()
        except Exception as e:
            print(f"Error al cargar estilos: {e}")
