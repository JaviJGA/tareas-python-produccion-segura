import random

n = 0
n_input = 0

#tope entre 1 a n, pone el usuario

max_input = int(input("NUMERO MAX PARA RANGO\n"))
n = random.randint(1, max_input)

#bucle principal

while True:
    #pregunta number
    n_input = int(input("DAME UN NUMERO \n"))
    if n_input == n:
        break
    print("te equivocaste XD")
    if n_input < n:
        print("sube un poco más")
    elif n_input > n:
        print("baja un poco más")
print("saliste del bucle de la vida")