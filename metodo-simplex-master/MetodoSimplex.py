import numpy as np
from scipy.optimize import linprog

print ("numero de filas de las restriciones")
m= int (input()) 
print("numero de columnas de las restriciones")
n=int  (input())
matri=np.zeros((m,(n+m)))
vector=np.zeros((n))
objetivo=np.zeros((n+m))
print ('intrduce la matriz de coheficientes')
for r in range(0,(m)):
    for c in range(0,n):
        matri[(r),(c)]=(input("Elemneto X"+str(r+1)+","+str(c+1)+": "))
    objetivo[(r)]=(input('P=X'+str(r+1)+': '))
print(matri)
print("dijita las igualdades de las restriciones")
for r in range(0,n):
    vector[(r)]=(input('F'+str(r)+': '))
print(vector)
print ("dijite la funcion objetivo")
#for r in range(0,n):
   # objetivo[(r)]=(input('X'+str(r+1)+': ')) 
#Result=linprog(objetivo,matri,vector,bounds=(0,None))
#print (Result)
##print ("Valor optimo: " +Result.fun+ "\nX: " +Result.x)
matri=np.insert(matri,(n+m), vector, axis=1)
print (matri)
objetivo=np.insert(objetivo,(n),0,0)
print(objetivo)
matri=np.insert(matri,0, objetivo, 0)
print("matriz unida")
print("     x1  x2  s1  s2  resu")
print(matri)
