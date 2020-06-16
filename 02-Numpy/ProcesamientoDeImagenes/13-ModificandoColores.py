import matplotlib as plt
import numpy as np
from scipy import misc
import matplotlib.pyplot as plt
import urllib.request
from PIL import Image

#Para los fondos oscuros
plt.style.use("dark_background")

#Crearemos un array desde una imagen de internet
url = 'https://scontent.faep8-2.fna.fbcdn.net/v/t1.0-9/56447500_1992672647694256_2550888167808958464_o.jpg?_nc_cat=107&_nc_sid=730e14&_nc_ohc=K2jMLNYJQhQAX_UD3ca&_nc_ht=scontent.faep8-2.fna&oh=5d5e68693176ca598ec3e4a46342e621&oe=5F0EC8E7'

internet_image = Image.open(urllib.request.urlopen(url))

#Transformamos la imagen en un array de numpy
img1 = np.array(internet_image)

#Vemos como luce la imagen 
plt.figure(figsize=(10,20))
plt.imshow(img1)

#Veamos la forma
imageForm = img1.shape
print("\nEje X -> ",imageForm[0])
print("Eje Y -> ",imageForm[1])
print("Eje Z -> ",imageForm[2], " siendo este valor la cantidad de veces que se superponen los colores")
print("\nObteniendo en total una cantidad de {} valores".format(img1.size))
print("Si la imagen estuviera en escala de grises, no existiria dicho Eje Z, y solo tendria {} valores".format(imageForm[0]*imageForm[1]))

#Para saber el valor minimo y maximo de todo ese conjunto de valores, utilizamos:
print("\nValor Min: {}\tValor Max: {}".format(np.amin(img1),np.amax(img1)))

############################
# ACCEDIENDO A LOS VALORES#
############################
#Como puedo acceder a una seccion de la imagen?
print("\nFila Completa")
print(img1[100])
print("----------------")
print("\nColumna Completa")
print(img1[:150])
print("----------------")
print("\nCantidad de colores de un Pixel")
print(img1[100,150])
print("----------------")
print("\nEl valor de un Pixel")
print(img1[100,150,3])

############################
#   MODIFICANDO IMAGENES   #
############################

img2 = np.array(internet_image)
img2[0:100,:,0] = np.amax(img2)
img2[100:200,:,1] = np.amax(img2)
img2[400:600,0:500,2] = np.amax(img2)

#X1:X2 -> elejimos desde la fila X1 a la X2
#: -> en cuanto a la columna, no hacemos especificaciones. Agarramos todas
#     ->Al poner 0, decimos rojo
#   Z ->Al poner 1, decimos verde
#     ->Al poner 2, decimos azul

#ACLARACION: Cabe aclarar que si queremos modificar nuevamente la imagen en alguno de los rangos utilizados,
#Deberemos cargar nuevamente la imagen, dado que nuestro cambio estara arriba del cambio anterior.
plt.figure(figsize=(10,20))
plt.imshow(img2)

img3 = np.array(internet_image)
filtro = img3 < 100
#Esto creara una matriz booleana del mismo tamaño de la foto en donde
#cada pixel que sea menor a 100, tendra un valor True
print("\nTamaño del filtro -> ",filtro.shape)
print("Tamaño de la imagen -> ",img3.shape)

#Aplicamos el filtro, y en cada valor que cumpla,
#lo disminuiremos en el menor valor que presente 
img3[filtro] = np.amin(img3)
plt.figure(figsize=(10,20))
plt.imshow(img3)

#Crearemos un filtro seleccionando todos los pixeles mayores a 100
#lo aumentaremos al mayor valor que presente 
filtro2 = img3 >100
img3[filtro] = np.amax(img3)
plt.figure(figsize=(10,20))
plt.imshow(img3)

#Conclusion. 
#Cuando disminuimos el valor de los pixeles, ganamos opacidad
#Cuando aumentamos el valor de los pixeles, ganamos luminocidad

array_a = np.array(range(200))
array_b = np.array(range(200))
img3[array_a,array_b] = np.amax(img3)
#especifico para ese conjunto de rangos
plt.figure(figsize=(10,20))
plt.imshow(img3)