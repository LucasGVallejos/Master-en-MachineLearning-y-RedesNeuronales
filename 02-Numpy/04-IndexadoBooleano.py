import numpy as np
#Al indexado booleano Lo usaremos para filtrar los elementos
#El uso principal de este tipo de filtros es el de poder modificar los valores del array que cumplan con 
#cierto criterio

arrayB =  np.array([[11,12],[21,22],[31,32]])
print("La forma de nuestro nuevo array es de: ", arrayB.shape)
print(arrayB)

print("\nCrearemos un filtro de >15") 
filtro = (arrayB>15)
#Filtro sera una nueva matriz de igual forma que arrayB pero su composicion de valores sera booleanos
#Nos fijamos si cada uno de los elementos es mayor o menor que 15
#Coloca dicha comparacion en la nueva matriz Filtro
print(filtro)

print("\nCon el filtro anterior, podemos aplicar a nuestro array inicial dicho filtro.\nGenerando una nueva matriz que tiene solo los valores que cumplen con el filtro seleccionado")
filtrado = arrayB[filtro]
print(filtrado)

print("\nNo es necesario crear primero la condicion 'Filtro' y luego aplicarlo")
print(arrayB[arrayB % 2 == 0])

print("\nAhora podemos modificar los valores que cumplen con un criterio X")
print("Array antes de ser modificado")
print(arrayB)
print("\nArray despues de ser modificado")
arrayB[arrayB % 2 == 0] += 1000
print(arrayB)