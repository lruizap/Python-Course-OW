# Diseñar una función que calcule el área y el perímetro de una circunferencia. Utiliza dicha función en un programa principal que lea el radio de una circunferencia y muestre su área y perímetro.

import math


def CalcularAreaPerimetro(radio):
    return (CalcularArea(radio), CalcularPerimetro(radio))


def CalcularArea(radio):
    return math.pi * radio ** 2


def CalcularPerimetro(radio):
    return 2*math.pi*radio


radio = float(input("Introduce el valor del radio: "))
area, perimetro = CalcularAreaPerimetro(radio)
print(f"Area => {area}")
print(f"Perímetro => {perimetro}")
