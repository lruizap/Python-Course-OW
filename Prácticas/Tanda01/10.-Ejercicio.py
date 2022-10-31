# Un alumno desea saber cual será su calificación final en la materia de Algoritmos. Dicha calificación se compone de los siguientes porcentajes:
# 55% del promedio de sus tres calificaciones parciales.
# 30% de la calificación del examen final.
# 15% de la calificación de un trabajo final.

nota1 = float(input("Dime la nota del parcial 1: "))
nota2 = float(input("Dime la nota del parcial 2: "))
nota3 = float(input("Dime la nota del parcial 3: "))
examen = float(input("Dime la nota del exámen 3"))
trabajo = float(input("Dime la nota del trabajo "))

media = (nota1+nota2+nota3) / 3

notaFinal = round((media*0.55) + (0.3 * examen) + (0.15 * trabajo))

print(f"La nota del alumno es de: {notaFinal}")
