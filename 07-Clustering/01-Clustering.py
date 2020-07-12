#Clustering con sklearn
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import pandas as pd
import numpy as np
from itertools import cycle, islice
import matplotlib.pyplot as plt
from pandas.plotting import parallel_coordinates
import datetime

data = pd.read_csv('meteo/minuto.csv')
data.shape

#Nos quedamos con el 10% del dataset dado que es enorme
sample_df = data[(data['rowID'] % 10)==0]
sample_df.shape

#Estadisticas
sample_df.describe().transpose()

#Como la mayoria de los datos sobre la lluvia de mi nuevo dataset son ceros,
#Podemos eliminarlos para que sea mas ligero.
sample_df[sample_df['rain_duration']==0].shape
sample_df[sample_df['rain_accumulation']==0].shape
del sample_df['rain_accumulation']
del sample_df['rain_duration']

#Veamos cuantos NaN tenemos
rowsBeforeDeletedNaN = sample_df.shape[0]
sample_df = sample_df.dropna()
rowsAfterDeletedNaN = sample_df.shape[0]
rowsBeforeDeletedNaN - rowsAfterDeletedNaN

#Features
features = ['air_pressure', 'air_temp',
       'avg_wind_direction', 'avg_wind_speed', 'max_wind_direction',
       'max_wind_speed', 'min_wind_direction', 'min_wind_speed',
       'relative_humidity']
select_df = sample_df[features]

#Dado que estamos ante un caso de Aprendizaje no Supervisado, solo tenemos X
X = StandardScaler().fit_transform(select_df)

#Implementando K-Means
kmeans = KMeans(n_clusters=12)
#Ajustamos el modelo
model = kmeans.fit(X)
print("model\n",model)

#¿Cuales son los 12 grupos que formamos?
centers = model.cluster_centers_
print("centers\n",centers)

#Generamos una tabla que nos muestra los centos de cada columna
def pd_centers(featuresUsed, centers):
    colNames = list(featuresUsed)
    colNames.append('prediction')
    
    Z = [np.append(A,index) for index, A in enumerate(centers)]
    
    P = pd.DataFrame(Z, columns=colNames)
    P['prediction'] = P['prediction'].astype(int)
    
    return P

P = pd_centers(features, centers)

#Funcion para crear graficos Paralelos
def paralel_plot(data):
    my_colors = list(islice(cycle(['b','r','g','y','k']), None, len(data)))
    plt.style.use("seaborn-dark")
    plt.figure(figsize=(15,8)).gca().axes.set_ylim([-3,+3])
    parallel_coordinates(data, 'prediction', color = my_colors, marker='o')


#GRAFICOS
#Graficamos los dias secos
paralel_plot(P[P['relative_humidity']<-0.5])
#Graficamos los dias calidos
paralel_plot(P[P['air_temp']>0.5])
#Graficamos los dias frios
paralel_plot(P[(P['relative_humidity']>0.5) & (P['air_temp']<0.5)])