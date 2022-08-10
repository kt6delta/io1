# Paquetes necesarios

import sys
from PySide6 import QtWidgets
from PySide6.QtWidgets import QApplication, QMainWindow
from content.mainWidget import mainWidget

# Definimos la clase que será la ventana de la aplicación
class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
      # Definimos el título de la ventana
        self.setWindowTitle("Modelo de transporte")
      # Definimos las dimensiones de la ventana
        self.resize(1100, 400)
      # Definimos el widget central de la ventana
        self.setCentralWidget(mainWidget())


if __name__ == "__main__":
  # Inicializamos la aplicación
    app = QApplication(sys.argv)
  # Inicializamos la ventana
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
