##Alan Francisco Emmanuel Aguilar Fuentes
##Progamacion de Redes
##Crear listas con nombres, edades y nombre de amistades 
##09/10/2023


lstnombres = []

for i in range(5):
    nombre = input("Ingresa el nombre de tu mejor amigo o amiga: ")
    lstnombres.append(nombre)

lstedades = []

for i in range(5):
    while True:
        edad_str = input("Ingresa la edad de tu mejor amigo o amiga: ")
        if edad_str.isdigit():  
            edad = int(edad_str)
            lstedades.append(edad)
            break
        else:
            print("Por favor, ingresa un número válido para la edad.")

dicDatos = dict(zip(lstnombres, lstedades))

def imprimir_diccionario(diccionario):
    for clave, valor in diccionario.items():
        print(f"{clave} -> {valor}")

imprimir_diccionario(dicDatos)

print(f"Longitud de la lista lstnombres: {len(lstnombres)}")
print(f"Longitud de la lista lstedades: {len(lstedades)}")
print(f"Longitud del diccionario dicDatos: {len(dicDatos)}")

claves_ordenadas = sorted(dicDatos.keys())
print("Claves ordenadas del diccionario:")
for clave in claves_ordenadas:
    print(clave)

def buscar_clave(diccionario, clave):
    return diccionario.get(clave, None)

clave = input("Ingresa una clave a buscar en el diccionario: ")
valor = buscar_clave(dicDatos, clave)
if valor is not None:
    print(f"El valor asociado a la clave {clave} es {valor}")
else:
    print(f"La clave {clave} no se encuentra en el diccionario.")
