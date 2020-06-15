#A veces es util preparar de antemano un array de indices para luego operarlos en otro array
import numpy as np

arrayA = np.array([[11,12,13],[21,22,23],[31,32,33],[41,42,43]])
print("La forma de nuestro nuevo array es de: ", arrayA.shape)
print(arrayA)

print("\nCreamos dos arrays con numeros enteros que usaremos como indices")
cols = np.array([0,1,2,0])
print("Elegimos estos indices para las columnas: ", cols)
rows = np.arange(4)
#np.arange nos crea un array de rango 1 con los valores de 0 a n-1
print("Elegimos estos indices par a las filas: ", rows)

print("\nImprimimos los indices tomando uno de cada array, de a pares.")
for row, col in zip(rows,cols): 
    print("(",row,",",col,")")

#Conclusion: 
print("\nCon los indices antes creados, podemos acceder a los valores de nuestro arrayA")
print("Los valores contenidos en los indices son: ", arrayA[rows,cols])

#Vamos a operar con los valores seleccionados
print("\nNuestro array antes de ser modificado")
print(arrayA)
arrayA[rows, cols] += 1000
print("\nNuestro array despues de ser modificado")
print(arrayA)