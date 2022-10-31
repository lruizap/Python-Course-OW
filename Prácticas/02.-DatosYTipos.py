# Datos y tipos de datos

# Las librerías importadas siempre deben ir al principio del fichero
import math

# Función type() nos devuelve de que tipo es la variable
edad = int(19)
print(type(edad))
print(type(4.5))
vBoolean = True
print(type(vBoolean))


# Datos numéricos

numNeg = -5
print(abs(numNeg))

print(7/2)
print(7 // 2)
print(divmod(7, 2))  # Devuelve una tupla(como un array)

# Potencias
print(7**2)
print(pow(3, 2))

# Convertir datos
a = int("234")
print(a, type(a))

# Funciones dependientes de librerias
# Para estas funciones debemos importar la librería y luego llamar a la función como si fuesen características del objeto librería (nombreLeria.función)
print(math.sqrt(9))


# Datos Booleanos

num = 7
print(num == 7)

if (num > 7):
    print(f"{num} es mayor a 7")
else:
    if (num == 7):
        print(f"{num} es igual a {num}")
    else:
        print(f"{num} es menor a 7")


# Trabjando con variables

# del num  # Con esto podemos eliminar la variable
# print(num)


# Cadenas de caracteres

# %s usa la string
# %d usa el número entero
# %f usa el número decimal. Podemos indicarle los decimales que queremos que coja
# (%.(cantidad decimales)f)
print("El producto %s cantidad=%d precio=%.2f" % ("cesta", 23, 13.456))

# Definición de cadenas

cad1 = "Hola"
cad2 = '¿Qué tal?'
cad3 = '''Hola,
    que tal?'''

print(cad1 + "\n" + cad2 + "\n" + cad3)
print(cad1+" "+cad2)
print(cad1, cad2)
print(cad1*3)
print(cad1[0], cad1[2])

# Para obtener la longitud de la cadena podemos usar la función len()
print(len(cad2))

# También se puede comparar cadenas.
# Se comparan utilizando los códigos unicode
# a => U+0061
# b => U+0041
print("a" > "A")  # = true
print("hola" == "Hola")  # = false

# upper para poner todo en mayúsculas
print("hola".upper())

# lower para poner todo en minúsculas
print("ADIOS".lower())
