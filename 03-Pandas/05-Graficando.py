import pandas as pd
import matplotlib.pyplot as plt

#para usar fondo oscuro
plt.style.use('seaborn-dark-palette')

import pandas  as pd
#La mayoria de los datasets vienen en archivos de texto
#Vamos a leer el contenido de movies.csv, le indicamos el separador del csv y formara un dataframe
movies = pd.read_csv('movielens/movies.csv',sep=',')
tags = pd.read_csv('movielens/tags.csv',sep=',')
ratings = pd.read_csv('movielens/ratings.csv',sep=',')

#Un histograma es un grafico que nos indica con cuanta frecuencia aparecen los valores

ratings.hist(bins=10, column='rating',figsize=(5,5))
#bins -> en cuantas columnas/barras representamos nuestro histograma

#Un histograma es un grafico que nos indica con cuanta frecuencia aparecen los valores

ratings.hist(bins=10, column='rating',figsize=(5,5), normed = True)
#normed -> si queremos ver la 'probabilidad' de encontrar uno de estos valores 
#           en nuestro dataset

ratings.hist(bins=10, column='rating',figsize=(5,5), hysttype = 'step', color='red')
#hysttype -> cambiamos el tipo de histograma. En este caso de escalon
#color -> cambiar color

#Grafico boxplot
ratings.boxplot(column='rating', figsize=(5,5))