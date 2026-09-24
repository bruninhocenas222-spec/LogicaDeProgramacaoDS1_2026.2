import math

A = float(input("Digite o valor de A: "))
B = float(input("Digite o valor de B: "))
C = float(input("Digite o valor de C: "))

delta = B ** 2 - 4 * A * C

print("A =", A)
print("B =", B)
print("C =", C)
print("Delta =", delta)

if A == 0:
    print("Impossivel calcular")
elif delta < 0:
    print("Impossivel calcular")
else:
    R1 = (-B + math.sqrt(delta)) / (2 * A)
    R2 = (-B - math.sqrt(delta)) / (2 * A)

    print(f"R1 = {R1:.5f}")
    print(f"R2 = {R2:.5f}")
