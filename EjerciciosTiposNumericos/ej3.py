import datetime

fecha_Actual = datetime.datetime.now()
year = int(input("Dime tu año de nacimiento\n"))
mes = int(input("Dime tu mes de nacimiento\n"))
dia = int(input("Dime tu día de nacimiento\n"))

fecha_nacimiento = datetime.datetime(year, mes, dia)

# Calcular edad
edad = fecha_Actual.year - fecha_nacimiento.year

# por si cumples años ya
if (fecha_Actual.month, fecha_Actual.day) < (fecha_nacimiento.month, fecha_nacimiento.day):
    edad -= 1

print(f"Tienes: {edad} años.")
