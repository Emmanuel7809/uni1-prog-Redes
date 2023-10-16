#Alan Francisco Emmanuel Aguilar Fuentes
#Programacion de Redes 
# 02/10/2023
#Modulo 3
my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]

lista_unica = []

for num in my_list:
    if num not in lista_unica:
        lista_unica.append(num)

print("La lista con elementos únicos:")
print(lista_unica)