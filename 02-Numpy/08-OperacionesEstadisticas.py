import numpy as np
print("Dado un array aleatorio")
arr = 10 * np.random.randn(2,5)
print(arr)

#Calcular la media (promedio) de un array
print("\nLa media de nuestro array es: ")
print(arr.mean())

print("\nTambien podemos calcular el promedio pero fila por fila")
#Eje 1 = filas, Eje 0 = columnas
print(arr.mean(axis = 1))
print(arr.mean(axis = 0))

print("\nCreamos un array de 10 elementos aleatorios")
desordenado = np.random.randn(10)
print(desordenado)

print("\nCreamos una copia y la ordenamos")
ordenado = np.array(desordenado)
ordenado.sort()
print(ordenado)

print("\nTambien podemos, dado un nuevo array, buscar elementos unicos - no repetidos")
array = np.array([1,2,1,4,2,1,4,2,3])
print("Nuevo array")
print(array)
print("\nArray Unico")
print(np.unique(array))