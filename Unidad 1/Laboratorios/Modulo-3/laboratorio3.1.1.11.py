#Alan Francisco Emmanuel Aguilar Fuentes
#Programacion de Redes 
# 02/10/2023
#Modulo 3

income = float(input("Introduce el ingreso anual:"))

if income <= 85528:
    tax = (income * 0.18) - 556.02
else:
    tax = 14839.02 + (income - 85528) * 0.32

tax = round(max(tax, 0), 0)

tax = round(tax, 0)
print("El impuesto es:", tax, "pesos")
