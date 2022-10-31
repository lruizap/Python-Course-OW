# Crea un programa que pida dos número enteros al usuario y diga si alguno de ellos es múltiplo del otro. Crea una función EsMultiplo que reciba los dos números, y devuelve si el primero es múltiplo del segundo.

def esMultiplo(num1, num2):
    if num1 % num2 == 0:
        return True
    else:
        return False


numero1 = int(input("Número 1 : "))
numero2 = int(input("Número 2 : "))

print(esMultiplo(numero1, numero2))
