import math

numeroDado = 0
factorialCalculado = 0
cerosContados = 0

numeroDado = int(input("dame u número sin comas\n"))
factorialCalculado = str(math.factorial(numeroDado))
print("El factorial de", numeroDado, "es", factorialCalculado)

for ceros in reversed(factorialCalculado): #reversed es para iterar al reves lol
    # print(ceros)
    if ceros != "0":
        break
    else:
        cerosContados += 1
        continue
print("Se han encontrado", cerosContados, "ceros.")