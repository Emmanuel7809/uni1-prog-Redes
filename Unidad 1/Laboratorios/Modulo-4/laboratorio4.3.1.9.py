#Alan Francisco Emmanuel Aguilar Fuentes
#Programacion de Redes 
# 11/10/2023
#Modulo 4
def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True

    if num % 2 == 0 or num % 3 == 0:
        return False

    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6

    return True

for i in range(1, 20):
    if is_prime(i + 1):
        print(i + 1, end=" ")
print()
