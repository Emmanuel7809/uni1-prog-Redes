#Alan Francisco Emmanuel Aguilar Fuentes
#Programacion de Redes 
# 02/10/2023
#Modulo 3
blocks = int(input("Ingresa el número de bloques: "))

height = 0
blocks_used = 0

while blocks_used + height + 1 <= blocks:
    height += 1
    blocks_used += height

print("La altura de la pirámide:", height)
