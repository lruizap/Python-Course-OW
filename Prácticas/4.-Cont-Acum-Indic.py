# Contador

cont = 0
for var in range(1, 6):
    num = int(input("Dime un número:"))
    if num % 2 == 0:
        cont = cont + 1
print("Has introducido ", cont, " números pares.")

# Acumulador

suma = 0
for var in range(1, 6):
    num = int(input("Dime un número:"))
    if num % 2 == 0:
        suma = suma + num
print("La suma de los números pares es ", suma)

# Indicador

indicador = False
for var in range(1, 6):
    num = int(input("Dime un número:"))
    if num % 2 == 0:
        indicador = True
if indicador:
    print("Has introducido algún número par")
else:
    print("No has introducido algún número par")
