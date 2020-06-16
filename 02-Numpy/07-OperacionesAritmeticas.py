#Podemos realizar varias operaciones aritmeticas entre arrays
import numpy as np
print("Dado los sigguientes arrays: \n")
x = np.array([[111,112],[121,122]], dtype = np.int)
y = np.array([[211.1,212.1],[221.1,222.1]], dtype = np.float64)
print(x, "\n")
print(y,"\n")

#Resta
print("Resta: \n")
#Podemos restar directamente o usar el metodo np.subtract
print(x-y,"\n")
#print(np.subtract(x,y),"\n")

#Multiplicar
print("Multiplicar: \n")
#Podemos multiplicar directamente o usar el metodo np.multiply
print(x*y,"\n")
#print(np.multiply(x,y),"\n")

#Dividir
print("Dividir: \n")
#Podemos dividr directamente o usar el metodo np.divide
print(x/y,"\n")
#print(np.divide(x,y),"\n")

#Raiz Cuadrada
print("Raiz Cuadrada de x: \n")
print(np.sqrt(x),"\n")