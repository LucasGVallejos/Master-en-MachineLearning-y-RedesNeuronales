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

#Vemos como luce la imagen antes de nuestros cambios 
plt.figure(figsize=(10,20))
print("Imagen sin retocar\n")
plt.imshow(img1)

#Crearemos una mascara que tomara valor true, donde existan valores mayores a 115 en Azul.
blue_mask = img1[:,:,2] > 115

img1[blue_mask,0] = 0
img1[blue_mask,1] = 0
img1[blue_mask,2] = 0

print("\nImagen retocada \n")
plt.imshow(img1)