
#Alan Francisco Emmanuel Aguilar Fuentes
#Programacion de Redes 
# 02/10/2023
#Modulo 3

user_word = input("Ingresa una palabra: ")

user_word = user_word.upper()

word_without_vowels = ""

for letter in user_word:
    if letter not in "AEIOU":
        word_without_vowels += letter

print(word_without_vowels)
