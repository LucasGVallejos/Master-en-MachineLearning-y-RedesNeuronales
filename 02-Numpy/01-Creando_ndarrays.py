import numpy as np
####################################################
#Crearemos nuestro primer array de rango 1     RECTA
####################################################

unArray = np.array([7,77,777])
print("Tipo de dato de nuestro array -> ",type(unArray))

#Vemos cuantos elementos hay en nuestro array de rango 1
print("Cantidad de elementos de nuestro array ->",unArray.shape)
print("Tipo de dato de la cantidad de elementos -> ",type(unArray.shape))

#Podemos ver que el tipo de dato es una tupla. Ahora, ¿que representa el valor retornado de -unArray.shape-
#Bueno, nuestra variable unArray representa una recta con x valores, 
#donde x es la cantidad de elementos de nuestro array

####################################################
#Crearemos nuestro primer array de rango 2     PLANO
####################################################
dosArray = np.array([[7,77,777],[2,22,222]])

#Vemos cuantos elementos hay en nuestro array de rango 2
print("\nCantidad de elementos de nuestro nuevo array ->",dosArray.shape)
print("Tipo de dato de la cantidad de elementos -> ",type(dosArray.shape))

#El tipo de datos sigue siendo una tupla, en la cual podemos observar:
#1- El numero de rango en el cual nos encontramos (2)
#2- La cantidad de elementos por columna
#Conclusion: Es una matriz de 2x3

#######################################################
#Accediendo a los valores de nuestros Array de Rango 1
#######################################################

print("\nEl primer valor del array 1 es: ",unArray[0])
print("El segundo valor del array 1 es: ",unArray[1])
print("El tercer valor del array 1 es: ",unArray[2],"\n")
print(unArray,"\n")

#Tambien podemos modificar los valores de dicha manera
print("Actualizamos el ultimo valor por 111\n")
unArray[2] = 111
print(unArray,"\n")

#Como crear un array multidimensional
arrayMultidimensional = np.array([[11,21,31],[12,22,32],[13,23,33]])
print("\nNuestro Array multidies de forma: ", arrayMultidimensional.shape)
print(arrayMultidimensional)

#Acceder a un valor de nuestro array multidimensional
print("\nAsi accedemos a un valor de nuestro array de dos dimensiones, ", arrayMultidimensional[2,0]," -> pos (2,0)")
#siendo 2 el num de fila y 0 el num de la columna