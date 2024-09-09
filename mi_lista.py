
print("Ejemplo de liistas")
arcoirirs=["verde","azul", "morado"]
print(arcoirirs)
longitud=len(arcoirirs)
print("Elementos que contiene la lista arcoiris:", longitud)
print(f"Elementos que contiene la lista arcoiris v2: {longitud}")
print("accediendo a un elemento de la lista")
print(arcoirirs[1])
print(f"Elemento en la posicion 0 es {arcoirirs[0]}")
print("El primer color del arcoiris es:",arcoirirs[0])
print("agregar un elemento de la lista")
print(arcoirirs)
arcoirirs.append("naranja")
print(arcoirirs)
print("mostrar los elementos de la lista ciclo for")
for pereyra in arcoirirs:
    print(pereyra)