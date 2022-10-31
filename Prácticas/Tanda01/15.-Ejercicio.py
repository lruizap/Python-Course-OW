# Dadas dos variables numéricas A y B, que el usuario debe teclear, se pide realizar un algoritmo que intercambie los valores de ambas variables y muestre cuanto valen al final las dos variables.

a = int(input("Introduce el valor de a : "))
b = int(input("Introduce el valor de b : "))

temporal = a
a = b
b = temporal

print(f"a = {a} y b = {b}")
