import pandas as pd
#Pandas posee dos estructuras de datos basicos.
	#-> Series  ->Dataframes

#Crearemos una Serie, que es una estructura menor a los Dataframes.
#Estos ultimos estan conformados por Series.

#data -> [Array de elementos]
#index -> representaria nuestra 'key'
ser1 = pd.Series(data = [100,'Ninguno',300,'Texto',5.3], 
                index = ['emiliano','gregorio','patricio','brian','lucas'])
print("Serie1:\n",ser1)

ser2 = pd.Series(data = [50,'Todos',150,'',3.5])
print("\nSerie2:\n",ser2)
#(Si no lo agregamos el parametro index, se crea una llave unica e incremental)

print("\nObteniendo los indices:\n")
print(ser1.index,"\t",ser2.index)

print("\nAccediendo a los valores dado un indice\n")
print(ser1['lucas'])
print(ser1.loc['lucas'])
#La diferencia de hacerlo con .loc es que puedo acceder a multiples valores
print(ser1.loc[['emiliano','lucas','gregorio']])

#Tambien podemos acceder a traves de indices
print("\n",ser1[[0,1,2]])
#Con .loc no podremos pasar indices numeros. Lo hacemos con .iloc
print(ser1.iloc[[0,1,2]])

print("\nPodemos consultar si existe un indice en la serie\n")
print("Pablo esta en los indices -> ",'pablo' in ser1)
print("Patricio esta en los indices -> ",'patricio' in ser1)

#Podremos realizar operaciones sobre toda la serie, 
#siempre que el tipo de dato lo permita.
print(ser*3)

#Sino, podemos operar sobre ciertos elementos del mismo.
print(ser[['emiliano','patricio','lucas']]**2)