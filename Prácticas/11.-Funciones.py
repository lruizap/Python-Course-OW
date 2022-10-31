# Para definir una función usamos la palabra clave "def" + nombreFuncion + parámetros

# Los parámetros que les pasamos a la función se denominan parámetros formales
from unittest import result


def Factorial(n):
    resultado = 1
    for i in range(1, n+1):
        resultado *= i
    return resultado

# Las variables que se creen fuera de la función son variables globales
# Las variables que esten dentro de la función son variables locales


# Los parámetros que introducimos al llamar a la función son denominados parámetros reales.
num = int(input("Dame un número : "))
print(Factorial(num))
# El tipo de una función es el valor que devuelve, por tanto lo podemos tratar como tal.
# Es decir, si una función devuelve una cadena, podemos tratar a deicha función como cadena

# Las funciones recursivas suelen tener 2 soluciones, las itirativas (un bucle) y la recursiva (llamando a la misma función)


def factorialRecursiva(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * factorialRecursiva(num-1)


numero = int(input("Dime un número : "))
print(factorialRecursiva(numero))
