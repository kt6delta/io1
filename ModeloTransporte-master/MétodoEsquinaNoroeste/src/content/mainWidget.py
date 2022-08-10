# Paquetes necesarios

from PySide6 import QtWidgets
from PySide6.QtCore import Signal, Slot
from .leftWidget import leftWidget
from .centralWidget import centralWidget
from .rightWidget import rightWidget

# Definimos la clase que será el widget principal de la ventana de la aplicación
class mainWidget(QtWidgets.QWidget):

  # Función llamada por un evento de otro componente que llama al método addWidgets
  # del elemento centralWidget
    @Slot(int, int)
    def call_generate(self, rows, columns):
        self.centralWidget.addWidgets(rows, columns, self)

  # Función llamada por un evento de otro componente que llama al método displayValues
  # del elemento rightWidget
    @Slot(list)
    def solve(self, matrix, rows, columns):
        self.rightWidget.displayValues(matrix, rows, columns)

  # Definimos el constructor de la clase
    def __init__(self):
        super().__init__()

      # Definimos el tamaño máximo del elemento
        self.setFixedSize(1100, 500)
      # Definimos el layout del elemento como un contenedor horizontal
        self.layout = QtWidgets.QHBoxLayout(self)

      # Definimos un atributo como leftWidget
        self.leftWidget = leftWidget(self)
      # Definimos un atributo como centralWidget
        self.centralWidget = centralWidget()
      # Definimos un atributo como rightWidget
        self.rightWidget = rightWidget()

      # Agregamos los elementos de la clase al layout de la misma
        self.layout.addWidget(self.leftWidget)
        self.layout.addWidget(self.centralWidget)
        self.layout.addWidget(self.rightWidget)

      # Mostramos la clase
        self.show()
