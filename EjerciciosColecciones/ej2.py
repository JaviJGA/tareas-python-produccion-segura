origen = input("Introduce la divisa de origen (USD, EUR, GBP, CAD, JPY): ").upper()
destino = input("Introduce la divisa de destino (USD, EUR, GBP, CAD, JPY): ").upper()
cantidad = float(input("Introduce la cantidad a convertir: "))

# tasas con respecto al USD
tasas = {
    "USD": 1.0,
    "EUR": 0.94,
    "GBP": 0.79,
    "CAD": 1.38,
    "JPY": 149.00
}

# convertir a USD
if origen in tasas:
    dolares = cantidad / tasas[origen]
else:
    print("Divisa de origen no válida.")
    dolares = 0

# convertir de USD a la divisa destino
if destino in tasas:
    resultado = dolares * tasas[destino]
else:
    print("Divisa de destino no válida.")
    resultado = 0

# mostrar resultado
print("Resultado:", round(resultado, 2), destino)
