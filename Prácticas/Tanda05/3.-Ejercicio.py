# Se quiere realizar un programa que lea por teclado las 5 notas obtenidas por un alumno (comprendidas entre 0 y 10). A continuación debe mostrar todas las notas, la nota media, la nota más alta que ha sacado y la menor.

notas = []

for indice in range(1, 6):
    while True:
        nota = int(input(f"Introduce la nota {indice} del alumno: "))
        if nota >= 0 and nota <= 10:
            break
        else:
            print("La nota introducida no es válida")
    notas.append(nota)

print(f"Las notas del alumno son :{notas}")

print(f"La media es : {sum(notas)/len(notas)}")
print(f"La nota más alta es : {max(notas)}")
print(f"La nota más baja es : {min(notas)}")
