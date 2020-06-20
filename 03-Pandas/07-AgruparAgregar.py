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
del ratings['timestamp']
del tags['timestamp']

filtro_mejores = ratings['rating']>4.0
ratings[filtro_mejores]

filtro_animados = movies['genres'].str.contains('Animation')
animados = movies[filtro_animados]
animados.head()

rating_count = ratings[['movieId','rating']].groupby('rating').count()
rating_count

average_rating = ratings[['movieId','rating']].groupby('movieId').mean()
average_rating.head()

############
#  JOIN    #
############
#1PARAMETER: Columna que quiero unir
#2PARAMETER: key de relacion
#3PARAMETER: con que metodo quiero mergear
full = movies.merge(tags, on='movieId',how='inner')
full.head()

avg_ratings = ratings[['movieId','rating']].groupby('movieId').mean()
avg_ratings.head()

taquilla = movies.merge(avg_ratings, on='movieId',how='inner')
taquilla.tail()

bestsFilmsFilter = taquilla['rating'] >= 4.0
bestFilms = taquilla[bestsFilmsFilter]
bestFilms.head()

comedias = taquilla['genres'].str.contains('Comedy')
taquilla[comedias].head()