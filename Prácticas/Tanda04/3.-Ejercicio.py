# Pide una cadena y un carácter por teclado (valida que sea un carácter) y muestra cuantas veces aparece el carácter en la cadena.

cad1 = input("Introduce la primera cadena ")

while True:
    cad2 = input("Introduce el caracter a comprobar ")
    if len(cad2) > 1:
        print("La segunda cadena debe ser un carácter")
    else:
        break

print(cad1.count(cad2))
