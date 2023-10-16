#Alan Francisco Emmanuel Aguilar Fuentes
#Programacion de Redes 
# 02/10/2023
#Modulo 3

year = int(input("Introduce un año:"))

if year >= 1582:

    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print("Año Bisiesto")
    else:
        print("Año Común")
else:
    print("No esta dentro del período del calendario Gregoriano")
