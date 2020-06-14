class Fabrica:
    autos = []

    def __init__(self, nombre):
        self.nombre = nombre
        self.cantidadArticulos = 0
        print("Se creo la Fabrica: ", self.nombre)
    
    def __del__(self):
        print("Se elimino la Fabrica: ", self.nombre)

    def __str__(self):
        return "La fabrica {} generó con exito {} autos ".format(self.nombre,self.cantidadArticulos)
    
    def agregarAuto(self,auto):
        self.autos.append(auto)
        self.cantidadArticulos +=1
        print("Se agrego el siguiente auto --> ",str(auto))

class Auto:
    dueño = ''
    def __init__(self, color, puertas, ruedas):
        self.color = color
        self.puertas = puertas
        self.ruedas = ruedas
        print("Se creo un auto con {} puertas, {} ruedas y de color {}".format(self.puertas,self.ruedas,self.color))
    def __del__(self):
        print("Se elimino el auto")
    def __str__(self):
        return "El auto posee {} puertas, {} ruedas y de color {}".format(self.puertas,self.ruedas,self.color)


auto1 = Auto("Rojo", 2, 4)

fabrica = Fabrica("Ford")

fabrica.agregarAuto(auto1)