import numpy as np

print("Dado el siguiente array")
ex1 = np.array([[11,12],[21,22]])
print(ex1)
print("\nSumamos todos los elemntos del array -> ",np.sum(ex1))
print("Sumamos las columnas -> ",np.sum(ex1,axis=0))
print("Sumamos las filas -> ",np.sum(ex1,axis=1))

#####################################
#REFORMATEANDO UN ARRAY (IMPORTANTE)
#####################################
#1.Creamos un array
arr = np.arange(20)
print("\nDado el siguiente array")
print(arr)
print(arr.shape)

#2.Cambiamos su forma
print("Cambiamos su forma")
resharped_arr = arr.reshape(4,5)
print(resharped_arr,"\n")

#3.Transponemos un array
ex1 = np.array([[11,12],[21,22]])
print("\nDado el siguiente array")
print(ex1)
print("----")
print("Obtenemos su transpuesta")
print(ex1.T)

#####################################
#               WHERE               #
#####################################
print("\nDado el siguiente array")
mat = np.random.rand(4,4)
print(mat)

#le paso al array una condicion. En caso de que sea TRUE, le paso el segundo parametro.
#En caso de que sea FALSE, le paso el tercer parametro
np.where(mat > 0.5, 1000, -1)
print("El nuevo array aplicando la condicion es:")
print(np.where(mat > 0.5, 1000, -1))

arr_bools = np.array([0,0,0,0,1,True])
print("\nDado el siguiente array")
print(arr_bools)
print("Comprobamos si alguno de los valores del array es verdadero.")
print(arr_bools.any())
print("Comprobamos si todos los valores del array son verdaderos.")
print(arr_bools.all())

#####################################
#           UNIENDO DATASETS        #
#####################################
#Podemos crear un array random de ints, definiendo el numero min, max y el tipo de matriz
K = np.random.randint(low=2,high=50,size=(2,2))
M = np.random.randint(low=2,high=50,size=(2,2))
print("\nDado los siguientes arrays")
print(K,"\n\n",M)

print("\nVamos a unirlos verticalmente")
print(np.vstack((K,M)))
print("Vamos a unirlos horizontalmente")
print(np.hstack((K,M)))
print("\nPero tambien usando el metodo 'concatenate' y especificandole el eje, logramos el mismo resultado.")
print("Vamos a unirlos verticalmente")
print(np.concatenate([K,M], axis = 0))
print("Vamos a unirlos horizontalmente")
print(np.concatenate([K,M], axis = 1))

#####################################
#           PROPAGACION             #
#####################################
print("\nDado el siguiente array")
base = np.zeros((4,4))
print(base)

row = np.array([1,0,2,7])
print("\nCreamos un array unidimensional de forma: ",row.shape)
print(row)

print("\nY con la propagacion horizontal se lo sumamos al array de ceros")
y = base + row
print(y)
#Es importante que la cantidad de columnas de base y row sea la misma
col = np.array([[0,1,2,3]])
col = col.T
#Usamos la transpuesta para poder hacer la propagacion vertical
print("\nDado el siguiente array unidimensional de forma {}".format(col.shape))
print(col)
y = base + col
print("\nTambien podemos hacer propagar verticalmente")
print(y)

#No podemos hacer propagacion de una matriz con otra que tiene menos o mas columnas
#Pero si con un solo elemento.
arr_x = np.array([4])
print("\n", arr_x)
print("____________")
print(base + arr_x)