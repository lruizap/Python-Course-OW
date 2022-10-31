lista1 = [1, 2, 3, 4, 5, 6]
listaPrueba = ["a", "b", "c", "d", "e"]
lista2 = []
print(type(lista2))
print()

# Dentro de las listas podemos introducir elementos de distinto tipo
lista2 = [1, "string", True, 2.5]
print(lista2)
for contenido in lista2:
    print(contenido, type(contenido))

print()

# Podemos usar la variable num para acceder a cada elemento de la lista
# num son los elementos de la lista
# lista es donde estan guardado los elementos
contador = 0
for num in listaPrueba:
    print(f"{num} => Elemento {contador}")
    contador += 1

print()

lista3 = ["a", "b", "c", "d", "e"]

# En python podemos usar un unico for para recorrer dos listas al mismo tiempo
# Debemos poner dos contadores y una función que una las dos listas => zip(lista1, lista2)
for num, letra in zip(lista1, lista3):
    print(f"{num} => {letra}")

print()

# Podemos buscar directamente valores en las listas con "in".
# Esto nos devolverá un valor booleano
print(1 in lista1)
print("1" in lista2)
print(1 in lista3)

print()

# Podemos añadirle contenido a las listas simplemente concatenando
print(lista1)
lista1 += [7, 8, 9, 10]
print(lista1)

print()

# Si el índice que le pasamos es negativo, comienza a contar desde el final
print(lista1[-1], lista1[-2])
# Podemos hacer lo mismo que con cadenas, pedirle un rango o invertirlas a placer.
print(lista1[2:4])
print(lista1[::-1])

# Para ver el tamaño de la lista usaremos la función => len()
print(len(lista1))
# Para ver el valor máximo usaremos => max()
# Para el mínimo => min()
print(max(lista1), min(lista1))

# Podemos obtener la suma de la lista => sum()
print(sum(lista1))
# Podemos ordenar la lista => sorted()
lista4 = [7, 6, 9, 10, 1, 4]
print(sorted(lista4))

print()

# Podemos definir tablas haciendo listas de lista (matrices)
tabla = [lista1, lista2, lista3, lista4]
print(tabla)
# Para recorrer esta matriz usaremos un for anidado
for fila in tabla:
    for elem in fila:
        print(elem)

print()

# Los elementos de la lista pueden ser modificados y borrados a placer
lista5 = [1, 9, 2222]
print(lista5)
lista5[2] = 27
print(lista5)
del (lista5[2])
print(lista5)

print()

# Con el método append() podemañadir contenido a la lista
lista5.append(69)
print(lista5)

# Copiar listas es tan sencillo como igualar listas
# Al copiar una lista y modificar esta ultima, la lista copia también se modifica
lista6 = lista5
print(lista5, lista6)
lista5.append(2700)
print(lista5, lista6)

print()

# para copiar listas deberemos hacer lo siguiente
lista7 = lista6[:]
print(lista6, lista7)
lista6.append(1)
print(lista6, lista7)

print()

# Métodos principales de listas

# append() => introducimos un elemento al final de la lista
print(lista7)
lista7.append(55)
print(lista7)

print()

# extend() une dos listas en una
lista8 = [1, 2, 3]
lista9 = [4, 5, 6]
lista8.extend(lista9)
print(lista8)

print()

# insert() => añadir elemento en posición concreta
lista9.insert(1, 2900)
print(lista9)

print()

# pop() => devuelve el último elemento y este lo borra de la lista
# También le podemos pasar una posición para borrar
lista9.pop()
print(lista9)

print()

# remove() => elimina todos los elementos que sean iguales al que le pasemos
lista9.remove(2900)
print(lista9)
lista9.append(1)
lista9.append(6)
lista9.append(3)
lista9.append(9)
print(lista9)

print()

# reverse() => le damos la vuelta a la lista
lista9.reverse()
print(lista9)

print()

# sort() => ordena la lista
lista9.sort()
print(lista9)
# También podemos ordenar la lista de forma inversa
lista9.sort(reverse=True)
print(lista9)

print()

# count() => contamos las veces que aparece un elemento
print(lista9.count(4))

print()

# index() => nos dice la primera posición en la que se encuentra un elemento
print(lista9.index(1))

print()
