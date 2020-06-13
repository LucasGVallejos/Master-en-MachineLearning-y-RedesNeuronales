paciente = {"nombre": "juan", "edad":23, "fuma": False}
print(paciente)

print("\n¿El paciente fuma?")
print(paciente.get("fuma"))

print("\nActualizamos la edad")
#paciente.update({"edad": 18})
paciente["edad"] = 18
print(paciente)

print("pesos" in paciente) #vemos si existe la clave pesos en nuestro diccionario

#podemos simular un BD guardando estos datos en un alista 