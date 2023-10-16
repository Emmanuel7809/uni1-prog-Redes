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

def day_of_year(year, month, day):
    if year < 1 or month < 1 or month > 12 or day < 1 or day > days_in_month(year, month):
        return None

    day_of_year = day
    for m in range(1, month):
        day_of_year += days_in_month(year, m)

    return day_of_year

print(day_of_year(2000, 12, 31))  
print(day_of_year(2022, 2, 29))  

