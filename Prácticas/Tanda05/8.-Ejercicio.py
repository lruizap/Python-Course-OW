# Queremos guardar los nombres y la edades de los alumnos de un curso. Realiza un programa que introduzca el nombre y la edad de cada alumno. El proceso de lectura de datos terminará cuando se introduzca como nombre un asterisco (`*`) Al finalizar se mostrará los siguientes datos:

# - Todos lo alumnos mayores de edad.
# - Los alumnos mayores(los que tienen más edad)

V = True
alumnos = []
nombre = str("")
edad = int(0)
edadMax = -1

print("Introduzca los datos de los alumnos")

while V:
    nombre = str(input("Introduzca el nombre del alumno "))
    if (nombre.find("*") != -1):
        V = False
    else:
        edad = int(input("Introduzca la edad del alumno "))
        alumnos.append([nombre, edad])

print(f"Los alumnos son: {alumnos}")

print("Los alumnos mayores de edad son: ")

for i in range(len(alumnos)):
    if alumnos[i][1] >= 18:
        print(alumnos[i][0], end=" ")
    if alumnos[i][1] > edadMax:
        edadMax = alumnos[i][1]

print()
print(f"La edad máxima es de {edadMax} años")
