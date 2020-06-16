import numpy as np
print("Dado los siguientes array:")
s1 = np.array(["escritorio","silla","mesa"])
print(s1,"\n")
s2 = np.array(["escritorio","silla","lampara"])
print(s2,"\n")

#Interseccion
print("Interseccion: ")
print(np.intersect1d(s1,s2))

#Union
print("\nUnion:")
print(np.union1d(s1,s2))

#Diferencia
print("\nDiferencia")
print(np.setdiff1d(s1,s2))

#Que elementos de S1 estan en S2
print("\nQue elementos de S1 estan en S2")
print(np.in1d(s1,s2))