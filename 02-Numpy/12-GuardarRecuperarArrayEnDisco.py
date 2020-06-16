import numpy as np
#Generamos un array
arrayAGuardar = np.array([23.23,24.24])

#Guardo el array en disco
np.save("arrayEnDisco",arrayAGuardar)

#Recupero el array
arrayRecuperado = np.load("arrayEnDisco.npy")
print("El array recuperado es: ", arrayRecuperado)