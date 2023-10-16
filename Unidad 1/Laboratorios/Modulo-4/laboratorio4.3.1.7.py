#Alan Francisco Emmanuel Aguilar Fuentes
#Programacion de Redes 
# 10/10/2023
#Modulo 4

def is_year_leap(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

def days_in_month(year, month):
    month_lengths = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if month < 1 or month > 12:  
        return None

    if month == 2 and is_year_leap(year):
        return 29

    return month_lengths[month - 1]

test_data = [(2020, 2), (2021, 2), (2021, 6), (2022, 12)]
test_results = [29, 28, 30, 31]

for i in range(len(test_data)):
    year, month = test_data[i]
    print(f"{year}-{month} ->", end="")
    result = days_in_month(year, month)
    if result == test_results[i]:
        print("OK")
    else:
        print("Fallido")
