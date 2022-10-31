# Diseñar el algoritmo correspondiente a un programa, que:

# - Crea una tabla(lista con dos dimensiones) de 5x5 enteros.
# - Carga la tabla con valores numéricos enteros.
# - Suma todos los elementos de cada fila y todos los elementos de cada columna visualizando los resultados en pantalla.

tabla = []

for indice_fila in range(1, 6):
    fila = []
    for indice_col in range(1, 6):
        fila.append(int(
            input(f"Introduce el número de la fila {indice_fila} y columna {indice_col}: ")))
    tabla.append(fila)

print(tabla)

# Suma filas

contador = 0
for fila in tabla:
    print(
        f"La suma de los elementos de la fila {contador} = {fila} es => {sum(fila)}")
    contador += 1

print()

# Suma Columnas

for indice_col in range(1, 6):
    suma = 0
    for fila in tabla:
        suma = suma + fila[indice_col-1]
    print(
        f"La suma de los elementos de la columna {indice_col} es => {suma}")
