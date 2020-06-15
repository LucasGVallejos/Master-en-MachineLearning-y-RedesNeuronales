#Prueba de Velocidad
#Descubriremos que los arrays son mas rapidos que las listas
import numpy as np
from timeit import Timer
from numpy import arange

size = 1000000
timeits = 1000
#Vamos a realizar operaciones de tamaño 1000000, 1000 veces

nd_array = arange(size)
a_list = list(range(size))
print("Dado el siguiente array -> Dato: ", type(nd_array)," Forma: ", nd_array.shape)
print("Dada la siguiente lista -> Dato: ", type(a_list)," Forma: ", len(a_list))

#La funcion Timer nos mide el tiempo que lleva en realizar una operacion o funcion.
timer_numpy = Timer("nd_array.sum()","from __main__ import nd_array")
print("\nTime taken by numpy ndarrays: %f seconds" %(timer_numpy.timeit(timeits)))

timer_list = Timer("sum(a_list)","from __main__ import a_list")
print("Time taken by list: %f seconds" % (timer_list.timeit(timeits)))