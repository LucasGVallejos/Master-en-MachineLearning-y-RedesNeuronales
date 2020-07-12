#Clasificacion usando Scikit-learn
import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

data = pd.read_csv('meteo/diario.csv')

data.columns
data.head()

#Sabiendo el clima de la mañana (9am), veremos cual vendria a ser el clima de la tarde (3pm)

#Eliminamos los Ids dado que no son de nuestra incumbencia
del data['number']

beforeDeletedNaN = data.shape[0]
print(beforeDeletedNaN)

data = data.dropna()
afterDeletedNaN = data.shape[0]
print(afterDeletedNaN)

#Podemos observar que la humedad de la tarde esta expresada en porcentaje.
#En vez de crear una clase para cada uno de los porcentajes 1%,2%,3%... etc,
#Creamos dos clases para vez si esta o no humedo

#(Binarizamos 'relative_humidity_3pm' a 0 o 1)
dataCopied = data.copy() #Copiamos un dataframe en uno nuevo
dataCopied['high_humidity_label'] = (dataCopied['relative_humidity_3pm'] > 24.99)*1
print(dataCopied['high_humidity_label'])

#Guardamos nuestro objetivo en Y
y = dataCopied[['high_humidity_label']].copy()

#Generamos nuestras Features
morningsFeatures = ['air_pressure_9am', 'air_temp_9am', 'avg_wind_direction_9am',
       'avg_wind_speed_9am', 'max_wind_direction_9am', 'max_wind_speed_9am',
       'rain_accumulation_9am', 'rain_duration_9am']
X = dataCopied[morningsFeatures].copy()

#Ahora partiremos nuestro set de datos
X_train, X_test, Y_train, Y_test = train_test_split(X,y, test_size=0.33, random_state=324)

#Ajustamos
humidity_clasifier = DecisionTreeClassifier(max_leaf_nodes=10, random_state=0)
#Le paso los valores a entrenar
humidity_clasifier.fit(X_train, Y_train)

#Predecimos para nuestros casos de prueba
predictions = humidity_clasifier.predict(X_test)

#Vemos a simple ojo como nos fue
predictions[:20]
Y_test['high_humidity_label'][:20]

#Medimos la prediccion
accuracy_score(y_true= Y_test, y_pred= predictions)

#Si le agregamos o quitamos hojas al arbol, puede modificar nuestro score final