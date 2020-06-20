import pandas  as pd

#La mayoria de los datasets vienen en archivos de texto
#Vamos a leer el contenido de movies.csv, le indicamos el separador del csv y formara un dataframe
movies = pd.read_csv('movielens/movies.csv',sep=',')
tags = pd.read_csv('movielens/tags.csv',sep=',')
ratings = pd.read_csv('movielens/ratings.csv',sep=',')

del ratings['timestamp']
del tags['timestamp']

movies[['title','genres']].head()

#Una manera de ir a las ultimas 10 filas
ratings.tail(10)

#Cuenta la cantidad de veces aparecen los valores en la columna en particular
tag_counts = tags['tag'].value_counts()
tag_counts.head(100)

tag_counts[:10].plot(kind='bar', figsize=(7,7))