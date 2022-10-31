# Si queremos usar los módulos debemos importarlos.

# randint es la función que hemos creado que hace lo mismo que random.
import funciones  # Este es un fichero creado por mi
from random import randint

# Si queremos trabajar con horas o fehcas, importamos el módulo "time"
import time

# Si queremos trabajar con fechas importamos el módulo datetime
import datetime

# Podemos importar un módulo para ejecutar funciones del sistema operativo
import os

from math import sqrt  # De esta forma no necesitaríamos importar la galería completa

import math
print(math.sqrt(9))

# Si solo queremos usar la raíz cuadrada podemos usar:

print(randint(1, 100))

print(datetime.datetime.now())  # Nos devuelve la hora actual

# Podemos importar nuestras propias funciones desde otro fichero usando el import normal pero poniendo el nombre de nuestro fichero
print(funciones.factorialRecursiva(6))

time.sleep(5)  # El programa se para durante x segundos

os.system("cls")  # Con esto vamos a ejecutar en la consola el comando clear
