#calculadora, pregunta operacion
# ad sub mul div exit
#si no usa exit, pide2 nmeros
operador = "vacio"
n1 = 0
n2 = 0
ANS = 0.0 #ver como reusar en codigo como numero
# seguramente en el input comprobar si es strign o numero?
# si input es ANS, usar variable, si no, usar numero
# se podria o separar todo en funciones
# o sacar muchas cosas fuera de los case a la func
#

while True:
    operador = input("pon ADD, SUB, MUL, DIV o EXIT\n")
    match operador:
        case "ADD":
            n1 = input("Introduce el primer numero\n")
            n2 = input("Introduce el segundo numero\n")
            if n1 == "ANS":
                n1 = ANS
            else: n1 = float(n1)
            if n2 == "ANS":
                n2 = ANS
            else: n2 = float(n2)
            ANS = float(n1 + n2)
            print("El resultado es: " + str(ANS))

        case "SUB":
            n1 = input("Introduce el primer numero\n")
            n2 = input("Introduce el segundo numero\n")
            if n1 == "ANS":
                n1 = ANS
            else: n1 = float(n1)
            if n2 == "ANS":
                n2 = ANS
            else: n2 = float(n2)
            ANS = n1 - n2
            print("El resultado es: " + str(ANS))

        case "MUL":
            n1 = input("Introduce el primer numero\n")
            n2 = input("Introduce el segundo numero\n")
            if n1 == "ANS":
                n1 = ANS
            else: n1 = float(n1)
            if n2 == "ANS":
                n2 = ANS
            else: n2 = float(n2)
            ANS = n1 * n2
            print("El resultado es: " + str(ANS))

        case "DIV":
            n1 = input("Introduce el primer numero\n")
            n2 = input("Introduce el segundo numero\n")
            if n1 == "ANS":
                n1 = ANS
            else: n1 = float(n1)
            if n2 == "ANS":
                n2 = ANS
            else: n2 = float(n2)
            ANS = n1 / n2
            print("El resultado es: " + str(ANS))

        case "EXIT":
            print("adiooooooooooooos")
            break
        case _:
            print("Emm lo pusiste mal 🤓☝️")