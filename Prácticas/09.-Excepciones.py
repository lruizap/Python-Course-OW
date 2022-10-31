# Las excepciones las usamos para que no se termine el programa y se ejecute el código que le digamos

while True:
    try:
        x = int(input("Introduce un número:"))
        break
    except ValueError:
        print("Debes introducir un número")


cad = input("Dime un número")
try:
    print(10/int(cad))
except ValueError:
    print("No se puede convertir en entero")
except ZeroDivisionError:
    print("No se puede dividir entre 0")
else:
    print("Se ha producido otro error")
finally:
    print("")
