# GRACIAS STACKOVERFLOW, por si el usuario no tiene unidecode
import subprocess
import sys

def import_or_install(package):
    try:
        __import__(package)
    except ImportError:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])

import_or_install("unidecode")

import unidecode  # hay que instalar

# pedir texto al usuario
texto = input("Escribe un texto con varias palabras:\n")

# convertir a minúsculas y quitar acentos
texto = unidecode.unidecode(texto.lower())

# dividir por espacios
palabras = texto.split()

# diccionario para guardar los anagramas
anagramas = {}

# recorrer palabras
for palabra in palabras:
    # ordenar letras para usarlo como clave
    clave = ''.join(sorted(palabra))
    if clave in anagramas:
        anagramas[clave].append(palabra)
    else:
        anagramas[clave] = [palabra]

# mostrar resultados
print("\nAnagramas encontrados:")
hay_anagramas = False
for clave, grupo in anagramas.items():
    if len(grupo) > 1:  # si hay más de una palabra con las mismas letras
        print(grupo)
        hay_anagramas = True

if not hay_anagramas:
    print("No se encontraron anagramas 🔥🔥")
