import pandas as pd
#Los dataframes se asemejan a las tablas de MySQL
#Podemos crear un dataframe a partir de un diccionario de python.

dicc = {'invierno': pd.Series(data = [100.,200.,300.],index =['manzana','pera','naranja']),
        'primavera': pd.Series(data = [111.,222.,333.,4444.],index=['manzana','pera','cereza','uva'])}


df = pd.DataFrame(dicc)
print("Nuestro primer DataFrame: \n",df)

print("\nTambien podemos imprimir sus indices y columnas")
print(df.index)
print(df.columns)

print("\nPodemos crear un dataframe especificando los indices que quiero usar de otro dataframe\n")
df2 = pd.DataFrame(data = dicc, index = ['manzana','pera','cereza'],columns = ['invierno','primavera','verano'])
print(df2)

print("\nTambien podemos crear un Dataframe a partir de una lista de diccionarios de python\n")
data = [{'gregorio':2,'emiliano':1},{'lucas':5,'brian':10,'patricio':20}]
dataframe = pd.DataFrame(data)
print(dataframe)
print("\n\tVemos que automaticamente se asignan los nuevos indices")
print("\nPodemos reemplazar los indices anteriores\n")
dataframe = pd.DataFrame(data, index = ['coordinador','planificador'])
print(dataframe)