#REBANANDO ARRAYS (Slice)
#Hacer Slice a un array sirve para AISLAR una SUBREGION de la matriz de un ndArray
import numpy as np

arrayC = np.array([[11,12,13,14,15],[21,22,23,24,25],[31,32,33,34,35],[41,42,43,44,45]])
print("La forma de nuestro nuevo array es de: ", arrayC.shape)
print(arrayC)

print("\nCrearemos un slice de 2x2 a partir del array anterior")
unSlice = arrayC[0:2,1:3]
#El primer par de valores me indican la cantidad de filas que quiero seleccionar (0 y 1)
#El segundo par de valores me indican la cantidad de columnas que quiero seleccionar (1 y 2)
print(unSlice)

#Imprimimos el valor (0,0) del slice
print("Elemento (0,0) del slice es: ", unSlice[0,0])
#Como vemos en la salida, el slice genera un nuevo indice

print("\nAhora sumaremos 100 al valor de la posicion (0,0) del slice")
unSlice[0,0] += 100
print(unSlice)

print("\nAhora imprimimos la posicion (0,1) del array original")
print("Elemento (0,1) del array principal es: ", arrayC[0,1])

#ACABAMOS DE MODIFICAR EL VALOR DEL ARRAYC!
print("\nUn slice NO es un array nuevo e independiente, sino un puntero a los valores del arrayC")
print(arrayC)
#Nunca existio nuestro array Slice...

#IMPORTANTE
#¿Que pasaria si necesitaramos tener un nuevo array a partir de un slice?
nuevoArray = np.array(unSlice)
print(nuevoArray)