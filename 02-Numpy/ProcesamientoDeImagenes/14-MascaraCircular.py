#Crearemos un circulo.
#Dentro de dicho circulo, podremos ver la imagen, pero por fuera no.
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

#1- Obtendremos el cento de la imagen

total_rows, total_cols, total_layers = img1.shape
X,Y = np.ogrid[:total_rows,:total_cols]
print("X-> ",X.shape," Y-> ",Y.shape)
print("\npodemos ver que X es un array de una sola columna con todos sus indices")
print("podemos ver que Y es un array de una sola fila con todos sus indices")

#Calcularemos las distancias de cada pixel, al punto central. 
#(Distx = X - Xcentral)**2 y (Disty = Y - Ycentral)**2
#Para librarnos de las distancias negativas, elevamos al cuadrado (¿Podemos usar funcion modulo?)
#Una vez que tengamos ambas tablas, las fuscionamos

center_row = total_rows/2
center_col = total_cols/2
print("\nFila Central -> ", center_row," Columna Central -> ",center_col)

dist_from_center = (X - center_row)**2 + (Y - center_col)**2
print("\n",dist_from_center )

print("La distancia maxima al cuadrado es -> ",np.amax(dist_from_center))

#Luego, con un filtro eligiremos el radio del circulo. 
radius = (total_rows/2)**2
print("\nEl radio de nuestro circulo será -> ", radius)
circular_mask = (dist_from_center > radius)
#Los valores de cada pixel que esten dentro del radio seran True
img1[circular_mask] = np.amin(dist_from_center)
plt.figure(figsize=(10,20))
plt.imshow(img1)