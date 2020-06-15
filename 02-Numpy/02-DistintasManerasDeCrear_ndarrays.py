import numpy as np

print("Crear un array lleno de ceros")
ej1 = np.zeros((1080,1920))
print(ej1)
#Creamos un array del tamaño de una imagen full HD

print("\nCrearemos un array lleno de un valor determinado") 
ej2 = np.full((3,3),"f")
print(ej2)
#El primer parametro represanta la forma de nuestra nueva matriz, 3x3
#El segundo parametro representa el valor a rellenar, en este caso la letra 'f'

print("\nCrearemos un array identidad de 3x3") 
ej3 = np.eye(3,3)
print(ej3)

print("\nCreando un array llena de 1")
ej4 = np.ones((4,4))
print(ej4)

print("\nCreamos un array de flotantes aleatorios entre 0 y 1")
ej5 = np.random.random((5,5))
print(ej5)