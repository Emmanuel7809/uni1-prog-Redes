#Alan Francisco Emmanuel Aguilar Fuentes
#Programacion de Redes 
# 02/10/2023
#Modulo 3
secret_number = 777

print(
"""
+==================================+
| ¡Bienvenido a mi juego, muggle!  |
| Introduce un número entero       |
| y adivina qué número he          |
| elegido para ti.                 |
| Entonces,                        |
| ¿Cuál es el número secreto?      |
+==================================+
""")


while True:
    user_guess = input("Ingresa un número entero: ")
    
    if user_guess.isdigit():
        user_guess = int(user_guess)
    if user_guess == secret_number:
            print("¡Bien hecho, muggle! Eres libre ahora")
            break  # El juego termina si el usuario adivina el número secreto
    else:
            print("¡Ja, ja! ¡Estás atrapado en mi bucle!")
else:
        print("Debes ingresar un número entero válido.")