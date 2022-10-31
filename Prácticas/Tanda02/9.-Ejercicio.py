# Algoritmo que pida tres números y los muestre ordenados (de mayor a menor);

array = []
array.insert(0, int(input("Dime el primer número: ")))
array.insert(1, int(input("Dime el segundo número: ")))
array.insert(2, int(input("Dime el tercer número: ")))
array.sort()
print(f"Los números son {array}")
array.reverse()
print(f"Los números son {array}")
