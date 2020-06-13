#Podemos recibir parametros en las funciones

def calculoValor(mensaje):
    calculo = 43 * 2
    division = calculo / 6
    coeficiente = 45 * 3.1416
    resultado = division * coeficiente
    print(mensaje, division)

print("Funcion calculo\n")
calculoValor("El calculo da: ")

#Podemos recibir y devolver parametros en las funciones
def sumar_restar(numero1, numero2):
    suma = numero1 + numero2
    resta = numero1 - numero2
    return suma,resta

resp1, resp2 = sumar_restar(6,9)
print("suma: ", resp1," resta: ", resp2)