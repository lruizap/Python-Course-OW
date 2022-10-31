# Suponiendo que hemos introducido una cadena por teclado que representa una frase (palabras separadas por espacios), realiza un programa que cuente cuantas palabras tiene.

cad1 = input("Introduce la primera cadena ")
arrayCad = cad1.strip().split(" ")

print(f"el número de palabas es de : {len(arrayCad)}")
