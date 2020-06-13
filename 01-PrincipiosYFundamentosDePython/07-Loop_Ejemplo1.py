cantidadParticipante =  int(input("Por favor, ingrese la cantidad de participantes de la maraton: "))
for x in range(1, cantidadParticipante):
    confirmacion = ""
    while confirmacion != "s":

        nombre = input("\nIngrese nombre participante: ")
        mail = input("Ingrese el e-mail del participante: ")
        print("\nHola ", nombre," el e-mail es: ", mail," ¿Desea confirmar estos datos?")
        confirmacion = input("Para confirmar escriba \"S\" o \"N\" para rechazar: ")
        confirmacion = confirmacion.lower()
        if confirmacion == "s":
            print("\nGracias, confirmamos la inscripcion, lo esperamos!")
            print("El numero del participante es -> ", x)
        else:
            print("\nOperacion cancelada, intente nuevamente.\n")