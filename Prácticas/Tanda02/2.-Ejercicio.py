# Algoritmo que pida un número y diga si es positivo, negativo o 0.

num = float(input("Dime el número: "))
if num == 0:
    print("El número es 0")
elif num > 0:
    print("El número es positivo")
else:
    print("El número es negativo")
