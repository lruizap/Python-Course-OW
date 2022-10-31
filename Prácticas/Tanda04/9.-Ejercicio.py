# Realizar un programa que compruebe si una cadena contiene una subcadena. Las dos cadenas se introducen por teclado.

cad1 = input("Introduce la primera cadena ").strip()
cad2 = input("Introduce la segunda cadena ").strip()

if cad1.count(cad2) == True:
    print(f"{cad1} contiene {cad2}")
else:
    print(f"{cad1} no contiene {cad2}")

if cad1.find(cad2) > -1:
    print(f"{cad1} contiene {cad2}")
else:
    print(f"{cad1} no contiene {cad2}")

if cad2 in cad1:
    print(f"{cad1} contiene {cad2}")
else:
    print(f"{cad1} no contiene {cad2}")
