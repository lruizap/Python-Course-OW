# Dados los catetos de un triángulo rectángulo, calcula su hipotenusa.

# Bibliotecas importadas
import math

# Lectura de datos de entrada
cat1 = float(input("Dime el primer cateto: "))
cat2 = float(input("Dime el segundo cateto: "))

# Raíz cuadrada
hipotenusa = round(math.sqrt(cat1**2 + cat2**2), 2)
# La fución round nos permite redondear a los caracteres que le indiquemos

print(f"La hipotenusa es : {hipotenusa}")
