# Paquetes necesarios

from PySide6 import QtCore, QtWidgets
from PySide6.QtWidgets import QLineEdit
from PySide6.QtGui import QIntValidator
from PySide6.QtCore import QSize, Slot, Signal

# Definimos la clase que será el widget con un layout grid
class gridWidget(QtWidgets.QWidget):

  # Definimos una señal a ser lanzada cuando ocurra un evento
    signal = Signal(list, int, int)

  # Definimos un método que limpiará el layout del elemento
    def cleanLayout(self):
        for i in reversed(range(self.layout.count())):
            self.layout.itemAt(i).widget().setParent(None)

  # Función llamada por un evento de otro componente para obtener los elementos ingresados en la
  # representación matricial del problema
    @Slot(int, int)
    def showValues(self, rows, columns):
      # Definimos un arreglo que contendrá a los elementos input de tipo QLineEdit   
        list = []
      # Definimos un arreglo que contendrá los valores de los elementos de list
        list2 = []
        positions = [(i, j) for i in range(rows) for j in range(columns)]
        for position in positions:
            temp = self.layout.itemAtPosition(position[0], position[1])
            if temp:
                list.append(temp.widget())
            else:
                list.append(None)
        for item in list:
            if item:
                list2.append(item.text())
            else:
                list2.append(0)
      # Emitimos la señal definida en la clase  
        self.signal.emit(list2, rows, columns)

  # Método que se encargará de crear la matriz de inputs para ingresar los valores de la representación
  # matricial del problema
    def createMatrix(self, rows, columns):
      # Se llama al método cleanLayout de la clase
        self.cleanLayout()
      # Se iteran las posiciones recibidas por los parámetros rows y columns
        positions = [(i, j) for i in range(rows) for j in range(columns)]
        for position in positions:
          # En caso de que se esté en la última iteración en donde el valor de i y j son el mismo,
          # no devolvemos un elemento de tipo QLineEdit dado que en la representación matricial nunca se tiene ese valor 
            if position[0] == rows-1 and position[1] == columns-1:
                break
          # Creamos el nuevo elemento input
            input = QtWidgets.QLineEdit()
          # Configuramos su alineamiento horizontal al tipo central
            input.setAlignment(QtCore.Qt.AlignCenter)
          # Agregamos el elemento al layout de la clase
            self.layout.addWidget(input, *position)

  # Definimos el constructor de la clase
    def __init__(self, rows, columns, parentWidget):
        super().__init__()

      # Definimos el layout de la clase como un grid layout
        self.layout = QtWidgets.QGridLayout(self)

      # Definimos el espacio entre elementos del layout
        self.layout.setSpacing(20)

      # Definimos el tamaño máximo del elemento
        self.setFixedSize(QSize(400, 350))

      # Conectamos la señal de la clase con el método solve del elemento parentWidget
        self.signal.connect(parentWidget.solve)

      # Se llama al método createMatrix con los parámetros rows y columns
        self.createMatrix(rows, columns)

      # Se muestra el elemento
        self.show()
