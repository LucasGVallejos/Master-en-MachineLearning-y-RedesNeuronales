#Introduccion a la Regresion Lineal Simple

import matplotlib.pyplot as plt
import matplotlib.lines as lines
import numpy as np
plt.style.use("seaborn-dark")

#Supondremos que X contiene la cantidad de dinero a invertir
#E Y es el dinero que gano tras la inversion hecha
x = np.array([0, 6.5, 13.2, 18.1, 24.9, 28.2, 36.1])
y = np.array([5,  10,   17,   20,   25,   30,   35])

#Usaremos nuestro matplotlib para graficar
plt.figure(figsize=(7,7))
plt.scatter(x,y, s=60)
plt.ylim(bottom=0)
plt.title("Grafico de Inversion")
plt.xlabel("Dinero Invertido")
plt.ylabel("Dinero Ganado")
plt.grid()
plt.show()

#Simulemos futuras inversiones de 0 a 40
x2 = np.arange(0,40)
#Trataremos de obtener una respuesta similar en la ganancia
y2 = 0.2 * x2

#Usaremos nuestro matplotlib para graficar ambos problemas
plt.figure(figsize=(7,7))
plt.plot(x2,y2, color="red", label="Nuestra Prediccion")
plt.scatter(x,y, s=60)
plt.ylim(bottom=0)
plt.title("Grafico de Inversion")
plt.xlabel("Dinero Invertido")
plt.ylabel("Dinero Ganado")
plt.grid()
plt.show()

#Vemos que nuestra recta no es la adecuada para nuestro problema. 
#Habra que buscar otra funcion
y2 = 0.8 * x2 + 5

#Usaremos nuestro matplotlib para graficar ambos problemas
plt.figure(figsize=(7,7))
plt.plot(x2,y2, color="red", label="Nuestra Prediccion")
plt.scatter(x,y, s=60)
plt.ylim(bottom=0)
plt.title("Grafico de Inversion")
plt.xlabel("Dinero Invertido")
plt.ylabel("Dinero Ganado")
plt.grid()
plt.show()

def calcula_ganancia(x):
    y = 0.8 * x + 5
    return y

#Usaremos el ERROR CUADRATICO MEDIO (MSE)
#Para que nos diga que tan lejos estamos de nuestros valores originales.
#Es el promedio de la diferencia al cuadrado de nuestros valores reales con lo estimado.

#Luego deberemos saber la raiz cuadrada de nuestro MSE para llegar a dicha conclusion.

#Usaremos scikit-learn para calcular el MSE
#El modulo sklearn.metrics implementa la función mean_squared_error. 
#Esta función necesita dos argumentos:
#    y_true: los valores correctos
#    y_pred: nuestra predicción

from sklearn.metrics import mean_squared_error
y_true = x
y_pred = [ calcula_ganancia(d) for d in y_true ]

mse = mean_squared_error(y_true, y_pred)
print(np.sqrt(mse))