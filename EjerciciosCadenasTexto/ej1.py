#hacer que acepte este formato:
# OPERADOR N1 N2
operador = "vacio"
operacion = "vacio"
n1 = 0
n2 = 0
ANS = 0.0

while True:
    print("ACTUALIZACIÓN: puedes poner operador n1 n2, ejemplo:")
    print("ADD 29 420")
    operador = input("pon ADD, SUB, MUL, DIV o EXIT\n")
    
    #hago un poco de refactorización ya que evito repeticiones
    operacion = operador.split() #separamos por espacio
    if len(operacion) == 1: #si no tiene más aparte del operador, misma rutina
        n1 = input("Introduce el primer numero\n")
        n2 = input("Introduce el segundo numero\n")
    else:
        #si tiene más, entonces asignar las variables con los datos de operacion
        operador = operacion[0]
        n1 = operacion[1]
        n2 = operacion[2] #puede crashear si el usuario no pone segundo numero\n
        #se podria hacer un check y tal pero si funciona, funciona™
    
    #arreglito para ANS
    if n1 == "ANS":
        n1 = ANS
    else: n1 = float(n1)
    if n2 == "ANS":
        n2 = ANS
    else: n2 = float(n2)
    
    #la magia
    match operador:
        case "ADD":
            ANS = float(n1 + n2)
            print("El resultado es: " + str(ANS))

        case "SUB":
            ANS = n1 - n2
            print("El resultado es: " + str(ANS))

        case "MUL":
            ANS = n1 * n2
            print("El resultado es: " + str(ANS))

        case "DIV":
            ANS = n1 / n2
            print("El resultado es: " + str(ANS))

        case "EXIT":
            print("adiooooooooooooos")
            break
        case _:
            print("Emm lo pusiste mal 🤓☝️")
print("\n")