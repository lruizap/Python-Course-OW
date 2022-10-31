# Realizar un programa que inicialice una lista con 10 valores aleatorios (del 1 al 10) y posteriormente muestre en pantalla cada elemento de la lista junto con su cuadrado y su cubo.

import random

lista = []
for indice in range(0, 10):
    lista.append(random.randint(1, 10))

listaCuadrados = []
listaCubos = []

for indice in lista:
    listaCuadrados.append(indice ** 2)
    listaCubos.append(indice ** 3)

print(f"Lista = {lista}")
print(f"Lista cuadrados= {listaCuadrados}")
print(f"Lista cubos= {listaCubos}")
