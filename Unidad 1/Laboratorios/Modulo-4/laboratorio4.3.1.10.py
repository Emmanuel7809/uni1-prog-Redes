#Alan Francisco Emmanuel Aguilar Fuentes
#Programacion de Redes 
# 11/10/2023
#Modulo 4
def liters_100km_to_miles_gallon(liters):
    miles_gallon = 100 / (liters * 0.264172)
    return miles_gallon

def miles_gallon_to_liters_100km(miles):
    liters_100km = 100 / (miles * 1609.344 / 3.785411784)
    return liters_100km

print(liters_100km_to_miles_gallon(3.9))
print(liters_100km_to_miles_gallon(7.5))
print(liters_100km_to_miles_gallon(10.0))
print(miles_gallon_to_liters_100km(60.3))
print(miles_gallon_to_liters_100km(31.4))
print(miles_gallon_to_liters_100km(23.5))
