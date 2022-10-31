# Crea una función “calcularMaxMin” que recibe una lista con valores numéricos y devuelve el valor máximo y el mínimo. Crea un programa que pida números por teclado y muestre el máximo y el mínimo, utilizando la función anterior.

import random


def CalculaMaxMin(lista):
    return (max(lista), min(lista))


numeros = []
for i in range(20):
    numeros.append(random.randint(1, 100))

vmax, vmin = CalculaMaxMin(numeros)
print(f"Max = {vmax}")
print(f"Min = {vmin}")
