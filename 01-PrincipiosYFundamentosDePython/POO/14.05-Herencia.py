#La idea de la herencia es identificar una clase base (la superclase) 
#con los atriutos comunes y luego crear las demás clases 
#heredando de ella (las subclases) extendiendo sus campos específicos.

class Producto:
    def __init__(self,nombre,descripcion):
        self.nombre = nombre        
        self.descripcion = descripcion

    def __str__(self):
        return "\nNombre: {}\tDescripcion: {}".format(self.nombre,self.descripcion)

#Creamos un tipo de Producto
lapices = Producto("Lapices","Caja de lapices x12")
print(str(lapices))

#Para heredar los atributos y métodos de una clase en otra 
#sólo tenemos que pasarla entre paréntesis durante la definición

class Lapiz(Producto):
    precio = None
    marca = ""
    
    #Heredamos atributos Nombre y Descripcion, junto a los métodos __init__ y __str__
    #Podemos sobreescribir alguno de ellos, como el __str___
    def __str__(self):
        return "\nNombre: {}\tDescripcion: {}\nPrecio: {}\tMarca: {}".format(self.nombre,self.descripcion,self.precio, self.marca)

#Creamos un Lapiz Faber Castell
lapizFC = Lapiz("Lapiz negro","HB, punta redonda")
lapizFC.marca = "Faber Castell"
lapizFC.precio = 15

print(str(lapizFC))