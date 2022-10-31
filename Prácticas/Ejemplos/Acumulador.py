import random

print("Comienzo")
cuenta_cincos = 0
for i in range(3):
    dado = random.randrange(1, 7)
    print(f"Tirada {i + 1}: {dado}")
    if dado == 5:
        cuenta_cincos += 1
print(f"En total ha(n) salido {cuenta_cincos} cinco(s).")
print("Final")
