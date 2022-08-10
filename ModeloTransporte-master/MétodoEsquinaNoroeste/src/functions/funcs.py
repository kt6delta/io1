# Paquetes necesarios

import numpy as np

# Este método se encargará de crear la matriz solución mediante los pasos explicados en el método analítico de la práctica
def Solve(matrix):
  # Creamos un arreglo equivalente a las celdas de la matriz con los valores que se ingresaron y le cambiamos su dimensión de acuerdo a las
  # dimensiones de la matriz
    sol_arr = np.arange(matrix.shape[0]*matrix.shape[1]).reshape((matrix.shape[0], matrix.shape[1]))

  # Rellenamos de ceros toda la matriz
    sol_arr = np.zeros_like(sol_arr)

  # Definimos la celda noroeste
    cell = [0, 0]

  # Definimos la condición que será falsa cuando se haya terminado con el proceso de cambiar la esquina noroeste
    condition = True

  # Definimos la columna de las ofertas
    offer_column = matrix.shape[1]-1

  # Definimos la fila de las ofertas
    demand_row = matrix.shape[0]-1
    
    while condition:

      # Definimos la fila de la celda noroeste
        corner_row = cell[0]

      # Definimos la columna de la celda noroeste
        corner_column = cell[1]

      # Obtenemos el valor de la oferta para la fila de la celda noroeste
        offer_value = matrix[corner_row][offer_column]

      # Obtenemos el valor de la demanda para la columna de la celda noroeste
        demand_value = matrix[demand_row][corner_column]

      # Definimos el valor de las unidades como el mayor entre el valor de la demanda y el valor de la oferta
        units = offer_value if demand_value >= offer_value else demand_value

      # Definimos la casilla actual de la matriz solución como el valor de las unidades
        soBl_arr[corner_row][corner_column] = units

      # Restamos de la casilla actual de la oferta la cantidad de unidades
        matrix[corner_row][offer_column] -= units

      # Restamos de la casilla actual de la demanda la cantidad de unidades
        matrix[demand_row][corner_column] -= units

      # Verificamos si la celda noroeste se debe mover una casilla hacia abajo
        if (matrix[corner_row][offer_column] == 0 and matrix[demand_row][corner_column] == 0) or matrix[corner_row][offer_column] == 0:
            cell[0] += 1

      # Verificamos si la celda noroeste se debe mover una casilla hacia la derecha
        elif matrix[demand_row][corner_column] == 0:
            cell[1] += 1
            
      # En caso de que la fila o la columna de la celda noroeste sea equivalente a la última fila o columna de la matriz,
      # damos por finalizado el método
        if corner_row == matrix.shape[0]-1 or corner_column == matrix.shape[1]-1:
            condition = False
# Retornamos la matriz solución
    return sol_arr

# Este método recibe un array de una dimensión y lo devuelve como una matriz con las dimensiones recibidas
def listToNdarray(list, rows, columns):
    return np.reshape(list, (rows, columns))
