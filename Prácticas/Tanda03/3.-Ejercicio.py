# Algoritmo que pida números hasta que se introduzca un cero. Debe imprimir la suma y la media de todos los números introducidos.

suma = 0
cont = 0

num = int(input("Número (0 para salir) : "))
while num != 0:
    suma = suma + num
    cont = cont + 1
    num = int(input("Número (0 para salir): "))

if cont > 0:
    media = round((suma / cont), 2)
else:
    media = 0

print(f"Suma: {suma}")
print(f"Media: {media}")
