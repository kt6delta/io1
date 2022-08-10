# Paquetes necesarios

from PySide6 import QtCore, QtWidgets
from PySide6.QtCore import Signal, QSize

# Definimos la clase que será el widget izquierdo del widget principal
class leftWidget(QtWidgets.QWidget):

  # Definimos una señal a ser lanzada cuando ocurra un evento
    signal = Signal(int, int)

  # Definimos un método que emitirá la señal de la clase
    def sendData(self):
        self.signal.emit(self.first_spin.value(), self.second_spin.value())

  # Definimos el constructor de la clase
    def __init__(self, parentWidget):
        super().__init__()

      # Definimos el layout del elemento como un contenedor vertical
        self.layout = QtWidgets.QVBoxLayout(self)

      # Definimos un elemento input de la clase como QSpinBox
        self.first_spin = QtWidgets.QSpinBox()
      # Definimos el valor máximo del input a 10
        self.first_spin.setMaximum(10)
      # Definimos el alineamiento del input a tipo central
        self.first_spin.setAlignment(QtCore.Qt.AlignCenter)

      # Definimos un elemento input de la clase como QSpinBox
        self.second_spin = QtWidgets.QSpinBox()
      # Definimos el valor máximo del input a 10
        self.second_spin.setMaximum(10)
      # Definimos el alineamiento del input a tipo central
        self.second_spin.setAlignment(QtCore.Qt.AlignCenter)

      # Definimos un elemento boton de la clase como QPushButton
        self.button = QtWidgets.QPushButton("Generar matriz")

      # Conectamos la señal de la clase con el método call_generate del elemento parentWidget
        self.signal.connect(parentWidget.call_generate)

      # Conectamos el evento clicked del elemento button de la clase para que se llame al método sendData
        self.button.clicked.connect(self.sendData)

      # Agregamos el elemento botón al layout de la clase
        self.layout.addWidget(self.button)
      # Agregamos el primer elemento input al layout de la clase
        self.layout.addWidget(self.first_spin)
      # Agregamos el segundo elemento input al layout de la clase
        self.layout.addWidget(self.second_spin)

      # Definimos el tamaño máximo del elemento
        self.setFixedSize(QSize(300, 300))

      # Mostramos la clase
        self.show()
