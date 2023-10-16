#Calculador de interes
# Alan Francisco Emmanuel Aguilar Fuentes
# Ejercicio Par
#Unidad 1: Practico

monto_depositado = float(input("Ingrese la cantidad de dinero depositada: "))

saldo_año_1 = monto_depositado * (1 + 0.04)

saldo_año_2 = saldo_año_1 * (1 + 0.04)

saldo_año_3 = saldo_año_2 * (1 + 0.64)

print(f"Saldo después del primer año: {saldo_año_1:.2f}")
print(f"saldo despues del primer año: {saldo_año_2:.2f}")
print(f"saldo despues del tercer año: {saldo_año_3:.2f}")