#Alan Francisco Emmanuel Aguilar Fuentes
#Programacion de Redes 
# 02/10/2023
#Modulo 3

beatles = []

beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")

new_members = ["Stu Sutcliffe", "Pete Best"]
for member in new_members:
    beatles.append(member)

del beatles[3]
del beatles[3]

beatles.insert(0, "Ringo Starr")

print("Lista de los Beatles:", beatles)

print("Número de miembros de los Beatles:", len(beatles))
