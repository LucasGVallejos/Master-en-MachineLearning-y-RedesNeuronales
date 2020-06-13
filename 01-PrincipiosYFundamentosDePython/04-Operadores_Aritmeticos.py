#Ingreso de datos al sistema|
print("Operadores Aritmeticos \n")
num1 = float(input("Ingrese el primer numero para realizar la operacion: "))
num2 = float(input("Ingrese el segundo numero para realizar la operacion: "))

#suma
suma = num1 + num2
print("\n La suma de sus valores es: ", suma)

#resta
resta = num1 - num2
print("La resta de sus valores es: ", resta)

#potencia
potencia = num1 ** num2
print(num1, " potenciado a ", num2, " da como resultado: ", potencia)

#division entera
if num2 != 0 : 
    division = num1 // num2
    print("La division entera entre ", num1, "y ", num2, "es: ", division)
    resto = num1 % num2
    print("El resto entre ", num1, "y ", num2, "es: ",resto)
else:
    print("No puede realizarse la division dado que el segundo numero elegido es ", num2)
