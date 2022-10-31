# Las tuplas son como las listas pero sus valores son inmutables.
# Las tuplas pueden contener valores de distinto tipo
tupla1 = ()
tupla2 = ("a", 1, True)
print(tupla1, tupla2)

# Estas se pueden recorrer con for, usar operadores de pertenencia, se pueden concatenar, indexar, obtener parte de la tupla...
print(tupla2[0:2])
# Se puede obtener el tamaño, máximo, mínimo...

# Pero las tuplas no se pueden modificar, por tanto tampoco tiene elementos de adición o de emliminación.

# Hay funciones como divmod() que te devuelve los valores como tupla. Para guardar dichos valores hay que usar variables de la siguiente forma
cociente, resto = divmod(7, 2)
print(divmod(7, 2))
print(cociente, resto)
