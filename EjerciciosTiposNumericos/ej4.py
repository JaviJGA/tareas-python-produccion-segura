origen = input("Introduce la divisa de origen (USD, EUR, GBP, CAD, JPY): ").upper()
destino = input("Introduce la divisa de destino (USD, EUR, GBP, CAD, JPY): ").upper()
cantidad = float(input("Introduce la cantidad a convertir: "))

# tasas
usd_eur = 0.94
usd_gbp = 0.79
usd_cad = 1.38
usd_jpy = 149.00

# vonvertir a USD
dolares = 0

match origen:
    case "USD":
        dolares = cantidad
    case "EUR":
        dolares = cantidad / usd_eur
    case "GBP":
        dolares = cantidad / usd_gbp
    case "CAD":
        dolares = cantidad / usd_cad
    case "JPY":
        dolares = cantidad / usd_jpy
    case _:
        print("Divisa de origen no válida.")
        dolares = 0

# convertir de USD a otra divisa
resultado = 0

match destino:
    case "USD":
        resultado = dolares
    case "EUR":
        resultado = dolares * usd_eur
    case "GBP":
        resultado = dolares * usd_gbp
    case "CAD":
        resultado = dolares * usd_cad
    case "JPY":
        resultado = dolares * usd_jpy
    case _:
        print("Divisa de destino no válida.")
        resultado = 0

# Mostrar resultado
print("Resultado:", round(resultado, 2), destino)
