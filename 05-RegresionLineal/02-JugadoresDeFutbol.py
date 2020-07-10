import sqlite3
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split #Lo usaremos para nuestro entrenamiento
from sklearn.metrics import mean_squared_error
from math import sqrt
from sklearn import preprocessing

import matplotlib.pyplot as plt
import seaborn as sns #Nos ayuda a generar graficos mas complejos
from sklearn.metrics import accuracy_score #Estadisticas de precision
import numpy as np

plt.style.use("seaborn-dark")

#Usaremos una DB de futbol europeo, la cual tiene mas de 25.000 partidos
#y 10.000 jugadores para las temporadas de futbol profesional de 2008 a 2016

#Creamos una conexion a la DB
DB = sqlite3.connect('european_soccer/database.sqlite')
jugadores = pd.read_sql_query('SELECT * FROM Player_Attributes', DB)

jugadores.head()
jugadores.shape

jugadores.columns

#De todas las columnas determinaremos cual usaremos como "features"
#para alimentar nuestro modelo
features = ['potential', 'crossing', 'finishing', 'heading_accuracy',
       'short_passing', 'volleys', 'dribbling', 'curve', 'free_kick_accuracy',
       'long_passing', 'ball_control', 'acceleration', 'sprint_speed',
       'agility', 'reactions', 'balance', 'shot_power', 'jumping', 'stamina',
       'strength', 'long_shots', 'aggression', 'interceptions', 'positioning',
       'vision', 'penalties', 'marking', 'standing_tackle', 'sliding_tackle',
       'gk_diving', 'gk_handling', 'gk_kicking', 'gk_positioning',
       'gk_reflexes']

#Seleccionamos el target
target = ['overall_rating']

#Limpieamos los datos NaN
jugadores = jugadores.dropna()

#Separamos nuestros features en X y nuestro target en Y
x = jugadores[features] #Entrada, datos de entrenamiento
y = jugadores[target]  #Salida, objetivos

x.loc[3]
y.loc[3]
#A nuestro modelo le vamos a decir que para x.loc[3] tiene que devolver un y.loc[3]
#Y asi sucesivamente para cada una de las rows en x
#Por detras, sklearn va a ajustar nuestro modelo para descubrir los parámetros que miden la influencia de las variables x

#Graficando,
#En el eje X le paso una de las columnas, con sus valores
#En el eje Y le paso sus resultados para cada uno de sus valores
plt.scatter(x['reactions'], y, color='darkgreen', label='Data', alpha=.1)
#Aca podemos evaluar cada una de las columnas y ver si hay relacion o no entre los valores dados


#Vamos a tener 2 set de datos
#Uno sera el de entrenamiento y otro para probar nuestro entrenamiento
x_train, x_test, y_train, y_test = train_test_split(x,y, test_size=0.33, random_state=324)

scale = preprocessing.StandardScaler()
scale.fit(x_train)
x_train = scale.transform(x_train)
#Escalamos los datos. Es una buena practica

x_train

#Crearemos una instancia de regresion lineal
regressor = LinearRegression()
#Ajustamos el modelo a los datos de entrenamiento
regressor.fit(x_train,y_train)

#Llevamos a cabo una prediccion utilizando el set de testeo que reservamos antes
x_test = scale.transform(x_test)
y_prediction = regressor.predict(x_test)
y_result = y_prediction - y_test
y_prediction.shape

#Calcularemos el RMSE
RMSE = sqrt(mean_squared_error(y_true = y_test, y_pred = y_prediction))
regressor.score(x_test, y_test)

print(RMSE)

regressor.coef_ #los coeficientes que miden cada uno  de los valores de x