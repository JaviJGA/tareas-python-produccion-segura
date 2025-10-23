fraseIngresada = ""
fraseSeparada = ""
palabraClave = ""
longitudFrase = 0
ocurrencias = 0

fraseIngresada = input("pon lo que quieras\n")

#dividimos las palabras por espacios
fraseSeparada = fraseIngresada.split()
longitudFrase = len(fraseSeparada) #contar elementos hay en array
print("el texto tiene", longitudFrase, "palabras.")

#ahora, para las ocurrencias (repeticiones supongo?) seguramente usar for
#para ver cada elemento a ver si está repetido

palabraClave = input("escribe una palabra para buscar sus repeticioesn:\n")

ocurrencias = 0
for palabra in fraseSeparada:
    if palabra == palabraClave:
        ocurrencias += 1

print("la palabra", palabraClave, "aparece", ocurrencias, "veces en el texto.")
    