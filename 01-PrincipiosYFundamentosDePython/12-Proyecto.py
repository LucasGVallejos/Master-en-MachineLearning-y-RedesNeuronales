import os

print("\tBienvenido al sistema de gestion de pacientes.\n")

#   **************************
#   * VARIABLES GLOBALES     *
#   **************************
running = True
database = list()

#   **************************
#   *      FUNCIONES         *
#   **************************
def validateResponde(response):
    #validamos que la eleccion del usuario sea la correcta. Por defecto suponemos que no.
    validate = False
    resp = 0
    msg = "\nEleccion incorrecta. Intente nuevamente.\n"

    if response.isdigit():
        resp = int(response)
        if resp>=1 and resp <=4:
            msg = ""
            validate = True
    return validate, resp, msg

def busquedaDePacientes():
   tamañoBase = len(database)
   print("\t**************************************")
   print("\t*      BUSQUEDA DE PACIENTES         *")
   print("\t**************************************")
   if tamañoBase !=0:
       name = input("\nIngrese el nombre del paciente a encontrar: ")
       print("\nNUMERO DE USUARIO \tPACIENTE ENCONTRADO \tHISTORIA CLINICA\n")       
       for x in range(tamañoBase):
            if database[x]["nombre"].lower() == name.lower():
                print(x,"\t".ljust(20),database[x]["nombre"].ljust(20),"\t",database[x]["historiaClinica"].ljust(20),"\n")
       print("Busqueda finalizada\n")

   else:
        print("\nNo hay pacientes registrados en la base de datos.")
        print("Agrege nuevo pacientes para la busqueda. Muchas gracias.\n")
   return "Busqueda de pacientes.\n"

def listadoDePacientes():
    tamañoBase = len(database)
    print("\t**************************************")
    print("\t*       LISTADO DE PACIENTES         *")
    print("\t**************************************")
    print("\nNUMERO DE USUARIO \tNOMBRE PACIENTE \tHISTORIA CLINICA\n")
    for x in range(tamañoBase):
        print(x,"\t".ljust(20),database[x]["nombre"].ljust(20),"\t",database[x]["historiaClinica"].ljust(20),"\n")

def cargaDePacientes():
    print("\t**************************************")
    print("\t*       CARGA DE PACIENTES           *")
    print("\t**************************************")
    nombre = input("\nIngrese el nombre del paciente que desea cargar: ")
    clinica = input("\nIngrese la historia la clinica del paciente: ")
    nuevoPaciente = {"nombre":nombre,"historiaClinica":clinica}
    database.append(nuevoPaciente)
    print("¡Paciente agregado con exito!\n")

def salir():
    global running
    running = False
    print ("Esperemos que haya disfrutado el sistema, hasta la proxima!.\n")

def showMenu():
    global running
    running = True
    print("\t1. Cargar pacientes.")
    print("\t2. Buscar paciente.")
    print("\t3. Listar paciente.")
    print("\t4. Salir.")
    print("\t~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~\n")
    response = input("Seleccione el numero de opcion -> ")  
    os.system('cls')
    return response

#   **************************
#   *   LOOP PRINCIPAL       *
#   **************************
while(running):
    menuOptions = {1: cargaDePacientes, 2:busquedaDePacientes, 3:listadoDePacientes, 4:salir}    
    response = showMenu()
    validate, resp, msg = validateResponde(response)
    if(validate):
        #obtenemos la eleccion deseada
        funcion = menuOptions.get(resp)
        funcion()
    else:
        print(msg)


