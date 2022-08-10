
import pandas as pd  #<------------ libreria

if __name__ == '__main__':

#***************** llama a el archivo que contiene la tabla **************************************************
    metodo_costo_minimo = pd.read_csv('MétodoCosteMínimo/src/tabla.txt')
    metodo_costo_minimo.dropna(inplace=True)
    metodo_costo_minimo = metodo_costo_minimo.set_index('plantas')
    metodo_costo_minimo_solucion = metodo_costo_minimo.copy()
    
#***************** obtiene la matriz del archivo *************************************************************
    for i in range(metodo_costo_minimo.shape[0]-1):
        for j in range(len(metodo_costo_minimo.columns)-1):
            metodo_costo_minimo_solucion.iloc[i, j] = 0
    
#***************** Define un bucle *************************************************************************** 
    bandera = True
    funcion_total_objetivo = 0
    while bandera:
        minimos = metodo_costo_minimo.iloc[:-1, :-1].idxmin(axis=1)                    #<------ encuentra el indice de costo minimo por columna
        if minimos.shape[0] == 0:
            bandera = False                                                            #<------ cierra el bucle si el resultado es 0
            print('Proceso terminado')
            break
            
#***************** Encuentra el minimo en la matriz **********************************************************
        minimo = metodo_costo_minimo.loc[metodo_costo_minimo.index[0], minimos[0]]     #<------ encuentra el costo minimo en la primera fila
        count = 0
        fila = 0
        columna = minimos[0]                                                           # <------obtiene la columna con el costo minimo de la primera fila
        for i in  range(1, metodo_costo_minimo.shape[0]-1):                            # <----- recorre todas la columnas de la fila 1
            
            aux = metodo_costo_minimo.loc[metodo_costo_minimo.index[i], minimos[i]]    # <------- obtiene el costo minimo de la fila
            if aux < minimo:                                                           # <------- una comparacion entre el costo minimo de todas las filas con la inicial
                
                fila = i
                columna = minimos[i]                                                   #<-------- guarda la fila o columna con valor minimo
                minimo = aux

#***************** Encuentra la Oferta y Demanda de la Matriz *************************************************
        oferta = metodo_costo_minimo.iloc[fila, -1]
        demanda = metodo_costo_minimo.loc[metodo_costo_minimo.index[-1], columna]
        
#***************** Asignacion de la maxima cantidad dependiendo de las restricciones de oferta y demanda ******
        if demanda != 0 and oferta != 0:
            if oferta > demanda:                
                funcion_total_objetivo += (metodo_costo_minimo.loc[metodo_costo_minimo.index[fila], columna] * demanda)   #<----- multiplicacion de demanda por el costo minimo
                metodo_costo_minimo_solucion.loc[metodo_costo_minimo.index[fila], columna] = demanda
                metodo_costo_minimo.loc[metodo_costo_minimo.index[-1], columna] = 0
                metodo_costo_minimo.iloc[fila, -1] = metodo_costo_minimo.iloc[fila, -1] - demanda                         # <------- quita la oferta a la demanda
                metodo_costo_minimo.drop(columna, inplace=True, axis=1)                                                   #<------ elimina la columna completada
            else:                
                funcion_total_objetivo += (metodo_costo_minimo.loc[metodo_costo_minimo.index[fila], columna] * oferta)    #<----- multiplicacion de oferta por el costo minimo
                metodo_costo_minimo_solucion.loc[metodo_costo_minimo.index[fila], columna] = oferta
                metodo_costo_minimo.iloc[fila, -1] = 0
                metodo_costo_minimo.loc[metodo_costo_minimo.index[-1], columna] = metodo_costo_minimo.loc[metodo_costo_minimo.index[-1], columna] - oferta   # <------- quita la demanda de la oferta
                metodo_costo_minimo.drop(metodo_costo_minimo.index[fila], inplace=True, axis=0)                          #<------ elimina la fila completada
            if minimos.shape[0] == 0:
                bandera = False                                                                                          #<----------- cierra el bucle
                break
                print('Proceso terminado')
        else:
#***************** si la columna o fila tienen una demanda o oferta igual a 0 se elimina **********************
            if demanda == 0:
                metodo_costo_minimo.drop(columna, inplace=True, axis=1)
            else:
                metodo_costo_minimo.drop(metodo_costo_minimo.index[fila], inplace=True, axis=0)
                
#***************** imprime la matriz resultado y el total del costo minimo ************************************
    print('******************************')
    print(metodo_costo_minimo_solucion)
    print('******************************')
    print('Total del costo minimo: ', funcion_total_objetivo)
