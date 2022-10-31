cadena = "informática"
contador = 0

print("Cadena: informática")
for caracter in cadena:
    print(f"caracter {contador} = {caracter}")
    contador += 1

print()

print("Comprobar si hay datos en la cadena :")
# Esto nos devolverá un valor bool
print("a" in cadena)
print("b" in cadena)
print("#" not in cadena)

print()

# Obtención de parte de la cadena
print(cadena[0])
# Esto nos devolverá la sub cadena desde el valor 0 al 4
print(cadena[0:4])
# También podemos hacer que nos devuelva valores según un valor, es decir, que nos devuelva un calor cada 2 caracteres o cosas así
print(cadena[0::2])
# Si no le pasamos ningún valor lo toma como el final de la cadena. Pasará lo mismo si no le introducimos un valor inicial
print(cadena[::2])
# Podemos hacer que nos devuelva la cadena invera
print(cadena[::-1])

print()

# Las cadenas tienen una serie de funciones por defecto que nos ayudan con a trabajar con ellas
# Si queremos cambiar un valor => replace()
print(cadena.replace("i", "I"))
# Cambiar la cadena a mayúsculas => upper
print(cadena.upper())

print()

# Esto no nos cambia el valor de la cadena, para cambiarlo tendríamos que indicarlo
print(cadena)
cadena = cadena.upper()
print(cadena)

print()

# Los métodos más importantes de las cadenas de caracteres

cad = "Hola, ¿cómo estás?"

# capitalize() => nos devuelve el primer carácter en mayúsculas
print(cad.capitalize())

# lower => minúsculas
# upper => mayúscuas
print(cad.lower())
print(cad.upper())

# swapcase() => devuelve cadena invirtiendo las mayúsculas y minúsculas
print(cad.swapcase())

# title()
print(cad.title())

# count() => nos devuelve cuántas veces aparece un carácter
print(cad.count("a"))
# También podemos buscar desde una posición concreta
# "Hol" empieza desde el inicio y finaliza en el carácter 3
print(cad.count("a", 0, 3))

# find() => nos devuelve la posición concreta donde está situada una cadena
print(cad.find("cómo"))

# startswitch() => nos devuelve un valor booleano indicando si la cadena comienza por la cadena indicada
print(cad.startswith("Hola"), cad.startswith("A"))
# También le podemos indicar la posición desde donde comienza a buscar

# endswitch() => nos devuelve un valor booleano indicando si la cadena termina por la cadena indicada
print(cad.endswith("tás?"), cad.endswith("papaya"))

# replace() reemplazar valores de la cadena
print(cad.replace("o", "0"))

# strip() => nos devuelve la cadena quitandoles los espacios de delante y de atrás
print(f" {cad} ".strip())
# También la podemos usar para eliminar algún caracter que esté al principio o al final de la cadena
print(cad.strip("H"))

# split() => Nos permite convertir una cadena en una lista
print(cad.split(" "))

# splitlines() => nos permite separar las líneas que hay en una cadena. Estas líneas son las indicadas con el carácter \n
texto = "Linea 1\nLinea 2\nLinea 3"
print(texto)
print(texto.splitlines())
