diccionario = {'one': 1, 'two': 2, 'three': 3}
print(type(diccionario))

# Los diccionarios se recorren y se acceden a ellos como las listas PERO los diccionarios en vez de usar un índice, usan la clave que tienen para cada elemento. (arrays asociativos de php)
print(diccionario["two"])
for clave in diccionario:
    print(diccionario[clave], end=" ")

print()

# Puedo añadir valores al diccionario
diccionario1 = {}
diccionario1["nombre"] = "Lucas"
diccionario1["edad"] = 20
print(diccionario1)
# Al introducir valores en un diccionario, estos no tienen un orden preestablecido.
print(diccionario1["nombre"])

print()

# Las funciones básicas de los diccionarios son practicamente las mismas que las de las listas o las tuplas
print(len(diccionario1))
diccionario1["nombre2"] = "Paco"
diccionario1["numRandom"] = 345
print(diccionario1)

del diccionario1["nombre2"]
print(diccionario1)

print()

# También podemos comprobar si existen datos dentro del diccionario
print("nombre" in diccionario1)
print("Paco" in diccionario1)
# Solo podremos comprobar el índice de los datos, no si contenido

print()
# Para poder copiar un diccionario se puede usar el método .copy()
diccionario2 = diccionario1.copy()
print(diccionario1)
print(diccionario2)
diccionario1["nombre"] = "José María Aznar"
print(diccionario1)
print(diccionario2)

print()

# clear() => Este método nos permite limpiar un diccionario
diccionario2.clear()
print(diccionario2)

print()

# copy() => copiar un diccionario

diccionario2 = diccionario1.copy()
print(diccionario2)

print()

# update() => Actualiza el diccionario a partir de los elementos de otro
dict1 = {'one': 1, 'two': 2, 'three': 3}
dict2 = {'four': 4, 'five': 5}
dict1.update(dict2)
print(dict1)

print()

# get() => Obtenemos la clave donde está el elemento
print(dict1.get("one"))
# El segundo parámetro es para indicar cuando el valor no existe
print(dict1.get("patata", "no existe"))

print()

# pop() => devuelve el elemento que indicamos y lo borra de la lista.
# También le podemos pasar el error que nos sale cuando el elemento no existe

# keys() => nos devuelve las claves del elemento
for clave in dict1.keys():
    print(clave, end=" ")
print()

print()

# items() => Podemos recorrer tanto las claves como los elementos en el mismo for ya que devuelve una lista de tuplas devolviendo la clave y el valor
for clave, valor in dict1.items():
    print(clave, "=>", valor)
