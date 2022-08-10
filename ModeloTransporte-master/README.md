# Manual de usuario

## Método de la esquina noroeste

### Paquetes requeridos:

* PySide6
* numpy

### Utilización:

Para el apartado de la solución de manera digital se tienen que realizar los siguientes pasos:

1. Habiendo ya descargado el repositorio y estando ubicado en la raiz del mismo, ejecutar el comando `python MétodoEsquinaNoroeste/src/window.py`
2. Ingresar el número de filas y columnas para el ingreso de valores de la representación matricial del problema y hacer click en el botón "Generar matriz"
3. Ingresar los valores de la representación matricial y seguido a esto hacer click en el botón "Solve"

De esta manera se desplegarán los valores de la solución obtenidos mediante el método en una nueva grilla con las columnas ***Actividad variable***,
***Costo unitario*** y ***Contribución***, equivalentes al valor de la solución, su equivalente en la matriz de la representación del problema, y el producto
entre estos 2 valores correspondientemente.

## Método de aproximación por Vogel

### Paquetes requeridos:

* numpy

### Utilización:

Para el apartado de la solución de manera digital se tienen que realizar los siguientes pasos:

1. Habiendo ya descargado el repositorio y estando ubicado en la raiz del mismo, ejecutar el comando `python MétodoAproximaciónPorVogel/src/main.py`
2. Ingresar los valores solicitados en la linea de comandos.

De esta manera se desplegarán los valores de la solución obtenidos en una matriz seguida del costo total requerido mediante este método.

## Método simplex o de costo mínimo

### Paquetes requeridos:

* pandas

### Utilización:

Para el apartado de la solución de manera digital se tienen que realizar los siguientes pasos:

1. Habiendo ya descargado el repositorio y estando ubicado en la raiz del mismo, ejecutar el comando `python MétodoCosteMínimo/src/Costo_Minimo_transporte_v2.py`

De esta manera se desplegarán los valores encontrados en el archivo tabla.txt seguidos del valor resultado obtenido mediante este método.