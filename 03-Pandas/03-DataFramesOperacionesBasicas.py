import pandas as pd
dicc = {'invierno': pd.Series(data = [100.,200.,300.],index =['manzana','pera','naranja']),
        'primavera': pd.Series(data = [111.,222.,333.,4444.],index=['manzana','pera','cereza','uva'])}


df = pd.DataFrame(dicc)

#OPERACIONES BASICAS

print("\nGeneramos una nueva columna a partir de la operacion de otras dos\n")
df['verano'] = df['invierno'] * df['primavera']
print(df)
#En donde pudo realizar el resultado, coloco dicho valor en la columna 'verano'

print("\nGeneramos otra columna a partir de una operacion booleana\n")
df['infra'] = df['primavera']<4000
print(df)

print("\nPodemos aislar una nueva columna\n")
columnaAislada = df.pop('infra')
print(columnaAislada)
print("\n",df)
#otra manera de eliminar la columna, pero sin que nos la devuelva
#es con la palabra reservada 'del'
del df['verano']
print("\n",df)

print("\nTambien podemos insertar una nueva columna\n")
#0 -> posicion de la nueva columna
#primavera_copia -> nombre de la nueva columna
#df['primavera'] -> datos que contiene la nueva columna. Puede ser una serie, o bien una columna de la misma u otra tabla
df.insert(0,'primavera_copia',df['primavera'])
print(df)