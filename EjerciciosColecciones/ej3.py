fraseIngresada = ""
fraseSeparada = ""
palabraClave = ""
longitudFrase = 0
ocurrencias = 0

fraseIngresada = input("pon lo que quieras\n")

# dividimos las palabras por espacios
fraseSeparada = fraseIngresada.split()
longitudFrase = len(fraseSeparada)
print("el texto tiene", longitudFrase, "palabras.")

# pedimos palabra clave (puede estar vacía)
palabraClave = input("escribe una palabra para buscar sus repeticiones (o deja vacío para ver todas):\n")

# si no se pone palabra clave, mostramos todas
if palabraClave == "":
    contador = {}
    for palabra in fraseSeparada:
        if palabra in contador:
            contador[palabra] += 1
        else:
            contador[palabra] = 1

    print("Apariciones de cada palabra:")
    for palabra, veces in contador.items():
        print(palabra, ":", veces)

else:
    ocurrencias = 0
    for palabra in fraseSeparada:
        if palabra == palabraClave:
            ocurrencias += 1
    print("la palabra", palabraClave, "aparece", ocurrencias, "veces en el texto.")
