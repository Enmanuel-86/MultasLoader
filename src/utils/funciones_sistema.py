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


    def limpiar_inputs_de_qt(lista_qlineedits_y_qlabel: tuple, lista_qradiobuttons: tuple = (),
                             lista_qcombobox: tuple = (), lista_spinBox_y_doubleSpinBox: tuple = ()) -> None:
        
        """
            ### Este metodo sirve para limpiar los inputs mas relevante como los:
            
            * QLineEdit
            * QLabel
            * QRadioButton
            * QListWidget
            * QComboBox

            * lista normales de python
            
            
            Para usar la funcion solo haga una lista agrupando todos los QLabel y QLineEdit en una lista y los QRadioButton en otra.
            
            Ya que los QLabel y QLineEdit para limpiarse ambos usan .clear() y los QRadioButton no.
            
            
            
            **Ejemplo**
            
            
            lista_qlabel_qlineedit = [input_1, input_2, input_3, label_4, ......]
            
            lista_qradiobutton = [radiobuton_1, radiobuton_2, ........]
            
            limpiar_inputs_de_qt(lista_qlabel_qlineedit, lista_qradiobutton) 
            
            ### Limpia los inputs (usarlo para salir de una pantalla o terminar una tarea)
            
            
            Tambien este metodo sirve para restablecer los combobox a su indice 0 es decir, si el combobox tiene "seleccionar aqui" lo devuelve a esa posicion
            
            
        
        
        """
        
        
        try:
            # Limpiamos los QlineEdits
            for qlineedit_o_qlabel in lista_qlineedits_y_qlabel:
                qlineedit_o_qlabel.clear()
                #qlineedit_o_qlabel.setEnabled(True)
            
            # Limpiamos los RadioButtons
            if len(lista_qradiobuttons) > 0: 
                for radiobutton in lista_qradiobuttons:
                    radiobutton.setAutoExclusive(False)
                    radiobutton.setChecked(False)
                    radiobutton.setAutoExclusive(True)
                    
            # Limpiamos los combobox       
            if len(lista_qcombobox) > 0:
                for combobox in lista_qcombobox:
                    combobox.setCurrentIndex(0)
                    
            if len(lista_spinBox_y_doubleSpinBox) > 0:
                for spinbox in lista_spinBox_y_doubleSpinBox:
                    spinbox.setValue(0)
        except:            
            print("No se puedieron limpiar los campos, por favor colocar los para metroscorrepondientes")
        else:
            print("Todo se limpio correctamente")
        
