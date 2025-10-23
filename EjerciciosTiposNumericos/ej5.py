import random as rndm

#pedir al usuario PIEDRA PAPEL O TIJERA
#una vez ponga el resultadode j1, generar uno de los 3
#podria asignar 0-2 a piedra papel tijera, listas o enum?
#check si jugador gana, empata o pierde
#hacer marcador, todo sera en un bucle
#si pone EXIT, salir

#variables que usare
jugadaJ1 = ""
jugadaJ2 = ""
jugadasDisponibles = ["PIEDRA", "PAPEL", "TIJERA", "EXIT"] #0, 1, 2, 3
marcadorJ1 = 0
marcadorJ2 = 0
marcadorPartidas = 0
marcadorEmpates = 0

#bucle
while True:
    jugadaJ1 = input("pon PIEDRA, PAPEL, TIJERAS o EXIT\n\n")
    jugadaJ1 = jugadaJ1.upper()
    jugadaJ2 = jugadasDisponibles[rndm.randint(0, 2)] #generar jugada
    match jugadaJ1:
        case "PIEDRA":
            if jugadaJ2 == "PAPEL":
                print("Oponente usó " + str(jugadaJ2) + ", PIERDES")
                marcadorJ2 += 1 #incrementa
            elif jugadaJ2 == "TIJERAS":
                print("Oponente usó " + str(jugadaJ2) + ", GANAS")
                marcadorJ1 += 1 #incrementa
            else:
                print("Oponente usó " + str(jugadaJ2) + ", EMPATE")
                marcadorEmpates += 1 #incrementa
        case "PAPEL":
            if jugadaJ2 == "TIJERAS":
                print("Oponente usó " + str(jugadaJ2) + ", PIERDES")
                marcadorJ2 += 1 #incrementa
            elif jugadaJ2 == "PIEDRA":
                print("Oponente usó " + str(jugadaJ2) + ", GANAS")
                marcadorJ1 += 1 #incrementa
            else:
                print("Oponente usó " + str(jugadaJ2) + ", EMPATE")
                marcadorEmpates += 1 #incrementa
        case "TIJERAS":
            if jugadaJ2 == "PIEDRA":
                print("Oponente usó " + str(jugadaJ2) + ", PIERDES")
                marcadorJ2 += 1 #incrementa
            elif jugadaJ2 == "PAPEL":
                print("Oponente usó " + str(jugadaJ2) + ", GANAS")
                marcadorJ1 += 1 #incrementa
            else:
                print("Oponente usó " + str(jugadaJ2) + ", EMPATE")
                marcadorEmpates += 1 #incrementa
        case "EXIT":
            print("adiooooooooooooos")
            break
        case _:
            print("Emm lo pusiste mal 🤓☝️")
    marcadorPartidas += 1
    print("\n")
    print("===================")
    print("Marcador Actual")
    print("===================")
    print("Jugador 1: " + str(marcadorJ1))
    print("IA: " + str(marcadorJ2))
    print("Empates: " + str(marcadorEmpates))
    print("Partidas Jugadas: " + str(marcadorPartidas))
    print("===================")
    print("===================")
    print("\n")