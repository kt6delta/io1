import numpy as np


def minimoCosto(f, c, datos, oferta, demanda):
    datosO = datos.copy()
    fo = f
    co = c
    posiFo = [-1] * (f + c)
    posiCo = [-1] * (f + c)
    solu = np.zeros((f, c))

    oferta = oferta.tolist()  # si es manual quitar
    demanda = demanda.tolist()  # ""
    print(datos)
    print("oferta=", oferta, "demanda=", demanda)
    pruf = 1
    Tceros = False
    temp = []

    for i in oferta:
        if i == 0:
            pruf = pruf + 1

        if (pruf == c):
            Tceros = True

    for i in demanda:
        if i == 0:
            pruf = pruf + 1

        if (pruf == f):
            Tceros = True

    v = 0
    h = 0
    while len(datos) > 1 and (not Tceros):
        # calcula penalizacion
        penalV = np.arange(f)
        for i in range(f):
            fabrica = np.array(datos)[i]  # filas
            fabrica = sorted(fabrica)
            penalV[i] = abs(fabrica[0] - fabrica[1])

        penalH = np.arange(c)
        for i in range(c):
            fabrica = np.transpose(datos)[i]  # columna
            fabrica = sorted(fabrica)
            penalH[i] = abs(fabrica[0] - fabrica[1])

        # tomar la mayor penalizacion
        penalV = penalV.tolist()
        penalH = penalH.tolist()
        print("penalV=", penalV)
        print("penalH=", penalH)

        sortPV = penalV.copy()
        sortPH = penalH.copy()

        sortPV.sort()
        sortPH.sort()

        if sortPV[f - 1] < sortPH[c - 1]:  # escogo fila
            posiC = penalH.index(sortPH[c - 1])  # actualiza demanda
            datosC = np.transpose(datos)[posiC]
            datosC = datosC.tolist()
            temp = datosC.copy()
            temp.sort()
            posiF = datosC.index(temp[0])
            if oferta[posiF] < demanda[posiC]:  # elimino fila
                print("------fila-------")
                demanda[posiC] = demanda[posiC] - oferta[posiF]
                solu[posiF][posiC] = oferta[posiF]
                posiFo[h] = posiF
                oferta[posiF] = 0
                datos = np.delete(datos, posiF, axis=0)
                oferta.pop(posiF)
                penalV.pop(posiF)
                f = f - 1
                h = h + 1
            else:  # columna eliminada
                print("------columna-------------")
                oferta[posiF] = oferta[posiF] - demanda[posiC]
                solu[posiF][posiC] = demanda[posiC]
                demanda[posiC] = 0
                posiCo[v] = posiC
                datos = np.delete(datos, posiC, axis=1)
                demanda.pop(posiC)
                penalH.pop(posiC)
                c = c - 1
                v = v + 1
            print(datos)
            print("oferta=", oferta, "demanda", demanda)
        else:  # escoge columna
            posiF = penalV.index(sortPV[f - 1])  # actualiza demanda
            datosF = datos[posiF].tolist()
            temp = datosF.copy()
            temp.sort()
            posiC = datosF.index(temp[0])
            if oferta[posiF] <= demanda[posiC]:  # elimina fila
                print("------fila-------")
                demanda[posiC] = demanda[posiC] - oferta[posiF]
                solu[posiF][posiC] = oferta[posiF]
                oferta[posiF] = 0
                posiFo[h] = posiF
                datos = np.delete(datos, posiF, axis=0)
                oferta.pop(posiF)
                penalV.pop(posiF)
                f = f - 1
                h = h + 1
            else:  # elimina columna
                print("------columna-------------")
                oferta[posiF] = oferta[posiF] - demanda[posiC]
                solu[posiF][posiC] = demanda[posiC]
                demanda[posiC] = 0
                posiCo[v] = posiC
                datos = np.delete(datos, posiC, axis=1)
                demanda.pop(posiC)
                penalH.pop(posiC)
                c = c - 1
                v = v + 1
            print(datos)
            print("oferta=", oferta, "demanda", demanda)
    # columna final tega valores diferentes de 0
    pruf = 1
    TFila = False
    TColumna = False
    Tceros = False
    if len(oferta) == 1:
        for i in demanda:
            if i == 0:
                pruf = pruf+1

        if pruf == len(demanda):
            Tceros = True

        if oferta[0] != 0 and (not Tceros):
            TFila = True

    # fila final tenga valores diferentes de 0
    pruf = 1
    Tceros = False
    if len(demanda) == 1:
        for i in oferta:
            if i == 0:
                pruf = pruf+1

        if pruf == len(oferta):
            Tceros = True

        if demanda[0] != 0 and (not Tceros):
            TColumna = True

    if(TColumna or TFila):
        # colocar los valores sobrantes en matriz solu
        tempF = np.arange(fo)
        tempF = tempF.tolist()
        tempC = np.arange(co)
        tempC = tempC.tolist()

        for co in range(v):
            if (posiCo.count(posiCo[co]) != 1):
                del tempC[posiCo[co]]
            else:
                for t in range(posiCo.count(posiCo[co])):
                    del tempC[posiCo[co] + t]

        for fo in range(h):
            if (posiFo.count(posiFo[fo]) != 1):
                del tempF[posiFo[fo]]
            else:
                for t in range(posiCo.count(posiCo[co])):
                    if(len(tempF) != 1):
                        del tempF[posiFo[fo] + t]

        for i in range(len(tempF)):
            for j in range(len(tempC)):
                solu[tempF[i]][tempC[j]] = demanda[j]
        # calcula costo total
        x = 0
        for i in range(len(solu)):
            for j in range(len(solu[0])):
                x = x+solu[i][j]*datosO[i][j]

    print("------------solucion-----------")
    print(solu)
    if (x != 0):
        print("costo total:", x)
