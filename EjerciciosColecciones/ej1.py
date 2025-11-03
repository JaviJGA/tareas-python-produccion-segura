import math

operador = "vacio"
operacion = "vacio"
ANS = 0.0

while True:
    print("ACTUALIZACIÓN: puedes poner operador seguido de los números, ejemplo:")
    print("ADD 2 3 5 8   o   SQRT 16")
    operador = input("pon ADD, SUB, MUL, DIV, SQRT o EXIT\n")

    operacion = operador.split()

    # si solo hay el operador, pedir los números
    if len(operacion) == 1:
        operador = operacion[0]
        numeros = input("Introduce los números separados por espacio:\n").split()
    else:
        operador = operacion[0]
        numeros = operacion[1:]

    # convertir los números o usar ANS
    for i in range(len(numeros)):
        if numeros[i] == "ANS":
            numeros[i] = ANS
        else:
            numeros[i] = float(numeros[i])

    match operador:
        case "ADD":
            resultado = 0
            for n in numeros:
                resultado += n
            ANS = resultado
            print("El resultado es:", ANS)

        case "SUB":
            resultado = numeros[0]
            for n in numeros[1:]:
                resultado -= n
            ANS = resultado
            print("El resultado es:", ANS)

        case "MUL":
            resultado = 1
            for n in numeros:
                resultado *= n
            ANS = resultado
            print("El resultado es:", ANS)

        case "DIV":
            resultado = numeros[0]
            for n in numeros[1:]:
                resultado /= n
            ANS = resultado
            print("El resultado es:", ANS)

        case "SQRT":
            if len(numeros) != 1:
                print("SQRT solo necesita un número")
                continue
            ANS = math.sqrt(numeros[0])
            print("El resultado es:", ANS)

        case "EXIT":
            print("adiooooooooooooos")
            break

        case _:
            print("Emm lo pusiste mal 🤓☝️")

print("\n")
