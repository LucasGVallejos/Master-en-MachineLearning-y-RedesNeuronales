sabores = ["chocolate","crema americana","vainilla", True, 20]
sabores2 = ["chocolate amargo","CREMA del CIELO", False, -20]

print("\nla lista contiene: ",sabores)

print("\nen la posicion 4 esta: ", sabores[4])

elementoEliminado = sabores.pop(4)
print("\nel elemento que se elimino es: ",elementoEliminado)
print("la lista contiene: ",sabores)

sabores.append("DDL")
print("\nagregamos el dulce de leche")
print("la lista contiene: ",sabores)

sabores.insert(0,"Heladeria EL VALLE")
print("\nAgregamos el nombre de la heladeria al comienzo de la lista")
print("la lista contiene: ",sabores)

print("\nAgregamos nuevos valores de otra lista")
sabores.extend(sabores2)
print("la lista contiene: ",sabores)
