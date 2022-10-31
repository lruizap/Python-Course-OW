edad = int(input("Dime tu edad: "))

if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")

# En python también existe el else if => "elif"

if edad <= 5:
    print("Eres un infante")
elif edad <= 10:
    print("Eres un niñ@")
elif edad <= 19:
    print("Eres un adolescente")
elif edad <= 26:
    print("Eres un joven")
elif edad <= 59:
    print("Eres una persona mayor")
elif edad > 59:
    print("Eres un viejo")

print()

# Estructuras de control repetitivas

contador = 1
while contador <= 10:
    print(contador, end=" ")
    contador += 1
print()

# Para el bucle for hay que acalrar el rango con "range()"
# Dentro de "range()" puede ir tanto números como variables
# range(1,11) => del 1 al 10; el último valor no se pone
# range(VariableIgualADiez) => del 0 al 10

for i in range(1, 11):
    print(i, end=" ")
print()

for i in range(2, 11, 2):
    print(i, " ", end="")
print()

print()

print("Comienzo")
for numero in [0, 1, 2, 3]:
    print(f"{numero} * {numero} = {numero ** 2}")
print("Final")

print()

print("Comienzo")
for i in range(10):
    print("Hola ", end="")
print()
print("Final")

print()

veces = int(input("¿Cuántas veces quiere que le salude? "))
for i in range(veces):
    print("Hola ", end="")
print()
print("Adiós")
