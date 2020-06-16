import numpy as np
print("\tEn estos casos python se encarga de asignar el tipo de datos")
ej1 = np.array([11,12])
print("El tipo de datos para el siguiente array es: ",ej1.dtype)
print(ej1)

ej2 = np.array([11.0,12.0])
print("\nEl tipo de datos para el siguiente array es: ",ej2.dtype)
print(ej2)

print("\n\tSin emabrgo, podemos forzar el tipo de datos expresandolo de la siguiente manera")
ej3 = np.array([11,21], dtype = np.float64)
print("El tipo de datos para el siguiente array es: ",ej3.dtype)
print(ej3)

ej4 = np.array([11.1, 21.7], dtype = np.int64)
print("\nEl tipo de datos para el siguiente array es: ",ej4.dtype)
print(ej4)