# Escribe un programa que pida un nombre de usuario y una contraseña y si se ha introducido “pepe” y “asdasd” se indica “Has entrado al sistema”, sino se da un error.

usuario = input("Dime el nombre de usuario :")
password = input("Dime la contraseña :")

if usuario == "pepe" and password == "asdasd":
    print("Has entrado en el sistema")
else:
    print("Te has equivocado")
