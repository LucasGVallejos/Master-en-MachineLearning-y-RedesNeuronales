#recorriendo diccionarios
paciente1 = {"nombre": "nati", "edad":19, "alcoholico": False, "peso":53}
paciente2 = {"nombre": "lucas", "edad":23, "alcoholico": True, "peso":108}
paciente3 = {"nombre": "claudia", "edad":58, "alcoholico": False, "peso":88}

pacientes = [paciente1,paciente2,paciente3]

#for clave, valor in paciente1.items():
#    print("clave -> ", clave, " valor -> ", valor)
#    print("**************************************\n")
#    if(clave == "edad" and valor<=20):
#        print("esta persona nacio en este siglo\n")

#recorriendo listas
demo=["uno", "dos", "tres", "cuatro"]

for x in range(len(demo)):
    print(demo[x])


#recorremos una lista de diccionarios
for x in range(len(pacientes)):    
    for clave, valor in pacientes[x].items():
        print("\nclave -> ", clave, " valor -> ", valor)
        print("**************************************\n")
        if(clave == "edad" and valor<=20):
            print("esta persona nacio en este siglo\n")