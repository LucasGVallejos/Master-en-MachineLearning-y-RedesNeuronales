#Creamos nuestra Clase 'Auto' vacia
class Auto:
    pass
    # a class with no methods (yet)
    #pass is a null operation -- when it is executed, nothing happens.

#Podemos ir agregandole atributos de la siguiente manera
auto.color = 'Rojo'
auto.puertas = 2
auto.dueño = input("\nIngrese Dueño del auto: ")

print("\nEl auto de ", auto.dueño, " posee ",auto.puertas, "puertas y es de color ",auto.color)

#O podemos agregarle atributos cuando se define la propia Clase
class Consecionaria:    
    #La funcion __init__ refleja un constructor
    def __init__(self, cantidadDeAutos):
        self.cantidadDeAutos = cantidadDeAutos
        print("Se creo una Consecionaria con una cantidad de ",self.cantidadDeAutos," autos!\n")
    def AgregarNuevoAuto(self):
        self.cantidadDeAutos +=1
        print("La nueva cantidad de autos es -> ", self.cantidadDeAutos)
        
consecionaria = Consecionaria(10)  