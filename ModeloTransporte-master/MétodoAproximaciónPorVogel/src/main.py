import numpy as np
import logic

# pedir datos y validar
f = int(input("ingrese numero de fabricas: "))
c = int(input("ingrese numero de almacenes: "))

datos = np.zeros((f, c))

for i in range(f):
    print("ingrese los costos de la fabrica", i+1)
    for j in range(c):
        print(" a la bodegas", j+1)
        a = input()
        while a.isdigit() == False:
            print("ingrese un valor numerico")
            a = input()
        if a.isdigit():
            a = int(a)
        datos[i, j] = a

demanda = np.arange(c)
for i in range(c):
    print("ingrese la demanda de la fabrica", i)
    temp = input()
    while temp.isdigit() == False:
        print("ingrese un valor numerico")
        temp = input()
    if temp.isdigit():
        demanda[i] = int(temp)

oferta = np.arange(f)
for i in range(f):
    print("ingrese la oferta del almacen", i)
    temp = input()
    while temp.isdigit() == False:
        print("ingrese un valor numerico")
        temp = input()
    if temp.isdigit():
        oferta[i] = int(temp)

logic.minimoCosto(f, c, datos, oferta, demanda)
