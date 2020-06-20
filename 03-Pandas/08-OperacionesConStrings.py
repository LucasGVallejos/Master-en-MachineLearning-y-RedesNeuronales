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

#Cada uno de los valores que spliteamos, aparece en una columna nueva gracias al expand=True
generos = movies['genres'].str.split('|', expand=True)
generos.head()

generos['esComedia'] = movies['genres'].str.contains('Comedy')
generos.head()

movies['year'] = movies['title'].str.extract('.*\((.*)\).*',expand=True)
movies.tail()

######################
#PARSEANDO TIMESTAMPS#
######################
#Tiempo Unix, recurso que se utiliza para calcular la diferencia de distintas fechas.
#Desde 01-01-1970 hasta 'ahora', en segundos
tags['parsed_time'] = pd.to_datetime(tags['timestamp'], unit = 's')
tags['parsed_time'].dtype

tags.head()

greater_than_t = tags['parsed_time'] > '2014-06-20'
selected_rows = tags[greater_than_t]
tags.shape, selected_rows.shape

#ordenamos por fecha
tags.sort_values(by="parsed_time",ascending=True).tail()

#Veamos las calificaciones que se hicieron a lo largo del tiempo
average_rating = ratings[['movieId','rating']].groupby('movieId', as_index=False).mean()
average_rating.tail()

joinedFilmsRating = movies.merge(average_rating, on='movieId', how='inner')
joinedFilmsRating.head()

yearlyAverage = joinedFilmsRating[['year','rating']].groupby('year',as_index=False).mean()
yearlyAverage.head()

yearlyAverage.plot(x='year',y='rating',figsize=(15,15),grid=True)