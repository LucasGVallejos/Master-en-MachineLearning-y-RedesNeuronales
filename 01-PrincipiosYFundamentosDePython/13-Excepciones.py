#Podemos atrapar los errores que pueden ir surgiendo a lo largo de la ejecucion de nuestro programa
cantidadDeIntentos = 0
while(True):
    try:
        variable = float(input("Ingrese un valor numerico: "))       
    except:
        cantidadDeIntentos +=1
        print("\n\tERROR: Se solicitó ingresar un numero\n")
    else:
        doble = variable * 2
        print("El doble de su variable ", variable, " es -> ", doble)  
        break
    #Esto ultimo se ejecuta sin importar si surgio error o no
    finally:
        print(cantidadDeIntentos)

#No solo podemos agarrar uno solo, sino muchos

while(True):
    try:
        variable = float(input("Ingrese un valor numerico por el cual desea dividir el numero 43: "))
        division = 43//variable
    except TypeError:
        cantidadDeIntentos +=1
        print("\n\tERROR: Se solicitó ingresar un numero\n")
    except ValueError:
        cantidadDeIntentos +=1
        print("\n\tERROR: Se solicitó ingresar un numero\n")
    except ZeroDivisionError:
        cantidadDeIntentos +=1
        print("\n\tERROR: No se puede dividir por 0\n")
    except Exception as e:
        cantidadDeIntentos +=1
        print("\n\tERROR: ",type(x).__name__ ,"\n")
    else:
        print("Dividir 43 por ", variable, " es -> ", division)  
        break
    finally:
        print(cantidadDeIntentos)

##Averiguar sobre raise()