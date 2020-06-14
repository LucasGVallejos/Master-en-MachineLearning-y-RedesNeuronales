#Usaremos atributos/metodos privados 
#La encapsulación consiste en denegar el acceso a los atributos y métodos internos de la clase desde el exterior. 
#En Python no existe, #pero se puede simular precediendo atributos y métodos 
#con dos barras bajas __ como indicando que son "especiales".

class Gato:
    def __init__(self):
        print("Se creo un Gato\n")
    def __metodoPrivado(self):
        print("Soy un Metodo Supuestamente Privado")
    def metodoPublico(self):
        print("Soy un Metodo Publico. ¿Podre acceder al Privado?")
        self.__metodoPrivado()
try:
    gato = Gato()
    gato.__metodoPrivado()

except AttributeError:
    print("\tERROR: Trataste de acceder a un metodo privado.\n")
finally:
    gato.metodoPublico()

#Vemos que no hemos sido capaces de invocar al __metodoPrivado de nuestro Gato, pero sin embargo al invocar al  metodoPublico, sí pudimos.

print("\n",dir(gato))

print("\n Podemos observar arriba que no encontramos ninguna función '__metodoPrivado' ")

#https://dbader.org/blog/meaning-of-underscores-in-python