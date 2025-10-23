#GRACIAS STACKOVERFLOW, por si el usuario no tiene unidecode
import subprocess
import sys

def import_or_install(package):
    try:
        __import__(package)
    except ImportError:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])
   
import_or_install("unidecode")

import unidecode #hay que instalar

#que es palindromo
#Un palíndromo es una palabra o frase que se lee igual en un sentido que en el otro
#ok gracias
#entonces quitar todo caracter especial (entra espacio?), lowercase y check reversed
#y no reversed por si son iguales, y ver los acentos con unidecode

fraseDada = ""
fraseReversa = ""

fraseDada = input("dame una frase\n")

fraseDada = fraseDada.lower() #convierte todo en lowercase
#isalnum dice true si es alfanumerico, quitando espacios y caracteres especiales (false)
fraseDada = ''.join(e for e in fraseDada if e.isalnum())
fraseDada = unidecode.unidecode(fraseDada)

fraseReversa = fraseDada[::-1] #es para revertir strings

if fraseDada == fraseReversa:
    print("Es palíndromo")
else:
    print("No es palíndromo")

# print(fraseReversa)

