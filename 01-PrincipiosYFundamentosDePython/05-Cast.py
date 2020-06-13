#casteo de string a int
entero = int("777")
print(type(entero))
print(entero)
#casteo de string a float
flotante = float("777.4")
print(type(flotante))
print(flotante)


#Podemos castear un string entero a flotante y seguiria siendo un flotante
flotanteEntero = float("777")
print(type(flotanteEntero))
print(flotanteEntero)

#Pero no podremos castear un string flotante a entero dado que no reconoce el caracter '.' o ','
#El siguiente ejemplo falla

#enteroFlotante = int("777.4")
#print(type(enteroFlotante))
#print(enteroFlotante)

#casteo de string a bool
valor_booleano = bool("True")
print(type(valor_booleano))
print(valor_booleano)

#casteo de bool a int 
booleanoComoEntero= int(False)
print(type(booleanoComoEntero))
print(booleanoComoEntero)

#casteo de int a bool
valor_booleano2 = bool(1)
print(type(valor_booleano2))
print(valor_booleano2)