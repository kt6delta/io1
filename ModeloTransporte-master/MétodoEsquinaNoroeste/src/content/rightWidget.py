# Paquetes necesarios

from PySide6 import QtCore, QtWidgets
from PySide6.QtCore import QSize, Slot, Qt
from functions import funcs as f

# Definimos la clase que será el widget derecho del widget principal
class rightWidget(QtWidgets.QWidget):

  # Definimos un método que limpiará el layout de la clase
    def cleanLayout(self):
        for i in reversed(range(self.layout.count())):
            self.layout.itemAt(i).widget().setParent(None)

  # Función llamada por un evento de otro componente que muestra los valores de la solución final del método
    @Slot(list, int, int)
    def displayValues(self, valuesMatrix, rows, columns):
      # Se llama al método cleanLayout de la clase
        self.cleanLayout()

      # Definimos una variable para el total resultante del método
        total = 0

      # Definimos el arreglo de valores ingresados en la representación matricial del problema
        valuesMatrix = [int(i) for i in valuesMatrix]

      # Invocamos al método listToNdarray del módulo de funciones `f` para obtener la matriz bi-dimensional con los valores ordenados
      # de la representación matricial
        valuesMatrix = f.listToNdarray(valuesMatrix, rows, columns)

      # Invocamos al método Solve del módulo de funciones `f` para obtener la matriz bi-dimensional con los valores
      # de la solución del método
        solveMatrix = f.Solve(f.listToNdarray(valuesMatrix, rows, columns))
        print(valuesMatrix)
        print(solveMatrix)

      # Creamos las posiciones para iterar en la matriz de soluciones
        positions = [(i, j) for i in range(rows) for j in range(columns)]

      # Creamos los elementos label de tipo QLabel para los títulos de la matriz de soluciones
        label_1 = QtWidgets.QLabel('Actividad variable')
        label_2 = QtWidgets.QLabel('Costo unitario')
        label_3 = QtWidgets.QLabel('Contribución')
      # Definimos el alineamiento horizontal de los elementos label a tipo central
        label_1.setAlignment(QtCore.Qt.AlignCenter)
        label_2.setAlignment(QtCore.Qt.AlignCenter)
        label_3.setAlignment(QtCore.Qt.AlignCenter)
      # Agregamos los elementos label al layout de la clase
        self.layout.addWidget(label_1, 0, 0)
        self.layout.addWidget(label_2, 0, 1)
        self.layout.addWidget(label_3, 0, 2)

      # Iteramos las posiciones creadas anteriormente
        for position in positions:
          # Definimos el valor de solución en la iteración actual
            solveValue = solveMatrix[position[0]][position[1]]
          # En caso de que el valor de solución sea distinto de 0 se entra en la condición
            if solveValue != 0:
              # Definimos el valor de la matriz de la representación matricial del problema correspondiente al valor
              # de solución solveValue
                matrixValue = valuesMatrix[position[0]][position[1]]

              # Creamos un nuevo label de tipo QLabel que tendrá el valor de la solución
                newLabel = QtWidgets.QLabel(str(solveValue))
              # Definimos el alineamiento horizontal del elemento a tipo central
                newLabel.setAlignment(QtCore.Qt.AlignCenter)
              # Agregamos el elemento label al layout de la clase
                self.layout.addWidget(newLabel)

              # Creamos un nuevo label de tipo QLabel que tendrá el valor de la solución
                newLabel2 = QtWidgets.QLabel(str(matrixValue))
              # Definimos el alineamiento horizontal del elemento a tipo central
                newLabel2.setAlignment(QtCore.Qt.AlignCenter)
              # Agregamos el elemento label al layout de la clase
                self.layout.addWidget(newLabel2)

              # Creamos un nuevo label de tipo QLabel que tendrá el valor de la solución
                newLabel3 = QtWidgets.QLabel(str(matrixValue * solveValue))
              # Definimos el alineamiento horizontal del elemento a tipo central
                newLabel3.setAlignment(QtCore.Qt.AlignCenter)
              # Agregamos el elemento label al layout de la clase
                self.layout.addWidget(newLabel3)

              # Agregamos a la variable total el valor resultante del producto entre el valor de la solución
              # y su valor en la representación matricial del problema
                total += matrixValue * solveValue

      # Creamos un nuevo label de tipo QLabel que servirá para simbolizar el valor de la solución del método
        label_1 = QtWidgets.QLabel('Total')
        label_2 = QtWidgets.QLabel('->')
      # Definimos el texto del label con la variable total
        label_3 = QtWidgets.QLabel(str(total))
      # Definimos el alineamiento horizontal de los elementos a tipo central
        label_1.setAlignment(QtCore.Qt.AlignCenter)
        label_2.setAlignment(QtCore.Qt.AlignCenter)
        label_3.setAlignment(QtCore.Qt.AlignCenter)
      # Agregamos los elementos al layout de la clase
        self.layout.addWidget(label_1)
        self.layout.addWidget(label_2)
        self.layout.addWidget(label_3)

  # Definimos el constructor de la clase
    def __init__(self):
        super().__init__()

      # Definimos un estilo para el borde de la clase
        self.setStyleSheet('border: 1px solid green;')

      # Definimos el layout de la clase como un grid layout
        self.layout = QtWidgets.QGridLayout(self)

      # Definimos el tamaño máximo del elemento
        self.setFixedSize(QSize(300, 400))

      # Mostramos la clase
        self.show()
