#Podemos recibir parametros en las funciones
def calculoValor(mensaje):
    calculo = 43 * 2
    division = calculo / 6
    coeficiente = 45 * 3.1416
    resultado = division * coeficiente
    print(mensaje, division)

calculoValor("El calculo da: ")

#Podemos recibir y devolver parametros en las funciones
def sumar_restar(numero1, numero2):
    suma = numero1 + numero2
    resta = numero1 - numero2
    return suma,resta

resp1, resp2 = sumar_restar(6,9)
print("\nsuma: ", resp1," resta: ", resp2)

#Tambien podemos enviar los argumentos por nombre
resp1, resp2 = sumar_restar(numero2=9, numero1=6)
print("suma: ", resp1," resta: ", resp2)

#A su vez, podemos definir valores nulos(None) o no Nulos por defecto
def multiplicar_dividir(numero1=2 , numero2=None):
    msg = ''  
    multiplicacion = 0
    division = 0
    if(numero2==None):  
        msg = 'Debe ingresar un segundo valor para la operatoria '
    else:
        multiplicacion = numero1 * numero2
        if(numero2 != 0):
            division = numero1 // numero2
        else:
            msg = 'El segundo valor no debe ser cero '
             
    return msg, multiplicacion, division

msg, resp1, resp2 = multiplicar_dividir(4,2)
print("\n",msg, "multiplicacion: ", resp1, "division: ", resp2)

msg, resp1, resp2 = multiplicar_dividir(numero2=2)
print(msg, "multiplicacion: ", resp1, "division: ", resp2)

msg, resp1, resp2 = multiplicar_dividir(2)
print(msg, "multiplicacion: ", resp1, "division: ", resp2)

#Cabe aclarar que lo que pasa en la funcion, queda en la funcion.
variable = 5 
print("\nDefinimos una nueva variable que vale ", variable)

def elevarNumeroAlCubo(numero1):
    numero1**=3
    print("\tDentro de la funcion nuestra variable vale ->",numero1)

print("Le pasamos por parametro dicha variable a la funcion elevarNumeroAlCubo y vemos que se modifica dentro de la funcion")
elevarNumeroAlCubo(variable)
print("Sin embargo, en nuestro esquema global, nuestra variable sigue valiendo ", variable)

#Pero no sucede lo mismo en las listas.
listaDeNumeros = [5,7,9]
print("\nEsto no afecta a las listas. Ej. Tenemos la siguiente lista: ", listaDeNumeros)
def elevarNumerosAlCuadrado(lista):
    for x in range(0,len(lista)):
        lista[x] **=2
elevarNumerosAlCuadrado(listaDeNumeros)
print("Luego de elevar la lista al cuadrado, queda de la siguiente manera: ", listaDeNumeros)
print("Pero si queremos que la lista no se modifique al utilizarla dentro de una funcion debemos ejecutar \n\televarNumerosAlCuadrado(listaDeNumeros[:])\n Con el ':' nosotros estaremos creando una referencia a otra nueva lista")