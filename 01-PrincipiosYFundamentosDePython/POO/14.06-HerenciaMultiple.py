#La capacidad de una subclase de heredar de múltiples superclases. 

#Esto conlleva un problema, y es que si varias superclases tienen los mismos atributos o métodos, 
#la subclase sólo podrá heredar de una de ellas.
#En estos casos Python dará prioridad a las clases más a la izquierda en el momento de la declaración de la subclase

class Primera:
    def __init__(self):
        print("\nSoy la Primer Clase\n")
    
    def metodoA(self):
        print("Soy un metodo de la Primer Clase")

class Segunda:
    def __init__(self):
        print("\nSoy la Segunda Clase\n")
    
    def metodoB(self):
        print("Soy un metodo de la Segunda Clase")
###################################################################
# Tanto la primer como la segunda superclase tienen mismos metodos#
# Es por ese motivo que si se heredan ambas superclases, Python   #
# prioriraza los metodos de la clase que se encuentre en la Izq.  #
###################################################################

class Tercera(Primera,Segunda):  
    def metodoC(self):
        print("Soy un metodo de la Tercer Clase")

tercera = Tercera()
tercera.metodoA()
tercera.metodoB()
tercera.metodoC()

class Cuarta(Segunda,Primera):  
    def metodoD(self):
        print("Soy un metodo de la Cuarta Clase")

cuarta = Cuarta()
cuarta.metodoA()
cuarta.metodoB()
cuarta.metodoD()