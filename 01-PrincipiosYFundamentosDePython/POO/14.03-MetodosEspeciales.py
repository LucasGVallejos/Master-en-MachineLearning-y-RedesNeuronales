#Existen Metodos especiales que podemos usar en las clases

class Fabrica:
    def __init__(self, nombre, cantidadEmpleados):
        self.nombre = nombre
        self.cantidadEmpleados = cantidadEmpleados
        print("Se creo la Fabrica: ", self.nombre)
    
   #It is called when an object is garbage collected 
   #which happens at some point after all references to the object have been deleted. 
    def __del__(self):
        print("Se elimino la Fabrica: ", self.nombre)

    def __str__(self):
         return "La fabrica {} generó con exito {} articulos con la siguiente cantidad de empleados: {}".format(self.nombre,self.cantidadArticulos, self.cantidadEmpleados)

fabrica = Fabrica("Peleles", 15)

cantidadAutos = input("\nIngresa la cantidades de peleles que fabrica la Fabrica creada ")
fabrica.cantidadArticulos = cantidadAutos

print(str(fabrica))

fabrica = Fabrica("Ford", 10)
cantidadAutos = input("\nIngresa la cantidades de autos que fabrica la Fabrica creada ")
fabrica.cantidadArticulos = cantidadAutos

print(str(fabrica))