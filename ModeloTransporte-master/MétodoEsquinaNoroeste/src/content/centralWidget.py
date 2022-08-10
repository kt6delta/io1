# Paquetes necesarios

from PySide6 import QtCore, QtWidgets
from PySide6.QtWidgets import QLineEdit
from PySide6.QtGui import QIntValidator
from PySide6.QtCore import QSize, Signal
from .gridWidget import gridWidget

# Definimos la clase que será el widget central del widget principal
class centralWidget(QtWidgets.QWidget):

  # Definimos una señal a ser lanzada cuando ocurra un evento
    signal = Signal(int, int)
  # Definimos una variable para almacenar el número de filas del widget
    rows = 0
  # Definimos una variable para almacenar el número de columnas del widget
    columns = 0

  # Definimos un método que emitirá la señal de la clase
    def sendData(self):
        self.signal.emit(self.rows, self.columns)

  # Definimos un método que limpiará el layout de la clase
    def cleanLayout(self):
        for i in reversed(range(self.layout.count())):
            self.layout.itemAt(i).widget().setParent(None)

  # Definimos un método que agregará elementos al layout de la clase
    def addWidgets(self, rows, columns, parentWidget):
      # Definimos el número de filas al parámetro rows
        self.rows = rows
      # Definimos el número de columnas al parámetro columns
        self.columns = columns
      # Llamamos al método cleanLayout de la clase
        self.cleanLayout()
      # Definimos el elemento grid de la clase como un nuevo objeto de la clase importada gridWidget
        self.grid = gridWidget(rows, columns, parentWidget)
      # Agregamos al layout de la clase el elemento grid
        self.layout.addWidget(self.grid)
      # Definimos el elemento botón de la clase de tipo QPushButton
        self.button = QtWidgets.QPushButton('Solve')
      # Conectamos la señal de la clase con el método showValues del elemento grid
        self.signal.connect(self.grid.showValues)
      # Agregamos al layout de la clase el elemento button
        self.layout.addWidget(self.button)
      # Conectamos el evento clicked del elemento button de la clase para que se llame al método sendData
        self.button.clicked.connect(self.sendData)

  # Definimos el constructor de la clase
    def __init__(self):
        super().__init__()

      # Definimos el layout del elemento como un contenedor vertical
        self.layout = QtWidgets.QVBoxLayout(self)

      # Definimos el espacio entre los elementos del layout
        self.layout.setSpacing(20)

      # Definimos el tamaño máximo del elemento
        self.setFixedSize(QSize(400, 400))

      # Mostramos la clase
        self.show()
