#Alan Francisco Emmanuel Aguilar Fuentes
#Programacion de Redes 
# 02/10/2023
#Modulo 2


hour = int(input("Hora de inicio (horas): "))
mins = int(input("Minuto de inicio (minutos): "))
dura = int(input("Duración del evento (minutos): "))

total_minutos = hour * 60 + mins + dura
hora_final = total_minutos // 60  # Obtén la hora final
minutos_final = total_minutos % 60  # Obtén los minutos finales

hora_final = hora_final % 24

print(f"{hora_final:02}:{minutos_final:02}")
