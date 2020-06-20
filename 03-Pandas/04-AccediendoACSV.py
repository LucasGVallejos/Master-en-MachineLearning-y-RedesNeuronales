import pandas  as pd
#La mayoria de los datasets vienen en archivos de texto
#Vamos a leer el contenido de movies.csv, le indicamos el separador del csv y formara un dataframe
movies = pd.read_csv('movielens/movies.csv',sep=',')
tags = pd.read_csv('movielens/tags.csv',sep=',')
ratings = pd.read_csv('movielens/ratings.csv',sep=',')

#Vemos las primeras 15 filas del dataframe movies
movies.head(15)

#Si no le pasamos ningun parametro a head(), vemos las primeras 5
tags.head()
ratings.head()

del ratings['timestamp']
del tags['timestamp']

#####################
#OPERANDO CON SERIES
####################

#Extraemos una fila y confirmamos que de hecho es un serie
row0 = tags.iloc[0]
type(row0)

print(row0)

#########################
#OPERANDO CON DATAFRAMES
#########################
ratings.columns

#Ofrece una descripcion de como se estan comportando los datos en dicha columna
ratings['rating'].describe()

#################################
#ANALIZANDO LA ESTADISTICA BASICA
#################################

#Podemos calcular el promedio de una columna.
ratings['rating'].mean()
#Pero tambien podemos calcular el promedio de todo el dataframe
ratings.mean()

#Tambien, individualmente podemos obtener el valor minimo de una columna
ratings['rating'].min()
#O, podemos obtener el valor minimo de todo un dataframe
ratings.min()

#Tambien, individualmente podemos obtener el valor maximo de una columna
ratings['rating'].max()
#O, podemos obtener el valor minimo de todo un dataframe
ratings.max()

#Tambien, podemos calcular la desviacion estandar de una columna
ratings['rating'].std()
#O, podemos calcular la desviacion estandar de todo un dataframe
ratings.std()

#El valor que aparece más veces
ratings['rating'].mode()

#El siguiente metodo nos muestra las posibles correlaciones de una columna
#de un dataframe con respecto a las otras. (cuanto influye el valor de una columna sobre otra)
ratings.corr()
#una correlacion negativa, nos indica una correlacion inversa
#una correlacion positiva, nos indica una correlacion directa

#Usaremos nuestros datasets para alimentar nuestro sistema de machine learning
#Para eso hay que entregarle informacion no erronea. ¿El dataset que presentamos tiene toda informacion correcta?
print("¿Sabemos que nuestro sistema de rating solo tiene 5 puntos?\n")
filter1 = ratings['rating'] > 5
print(filter1.any())


#################
# DATA CLEANING
#################

#Buscaremos valores nulos para ver si debemos borrar algo erroneo
movies.isnull().any()
ratings.isnull().any()
tags.isnull().any()

#Dado que nuestro dataset de tags tiene valores nulos en la columna 'tag', vamos a eliminarlos.
count = tags.shape[0]
print('La cantidad de filas antes de borrar es: ', count)
#borramos las fias que contengas algun valor nulo.
tags = tags.dropna()
print('Se eliminaron -> ', count - tags.shape[0], ' filas')

tags.isnull().any()