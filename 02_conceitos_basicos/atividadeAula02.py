# TODO: Desenvolva seu algoritmo aqui
# 1. Leia o valor da conta (float)
# 2. Leia o número de pessoas (int)
# 3. Calcule o valor por pessoa
# 4. Imprima formatado usando f-string


valor_conta= float(input("quanto deu a conta"))
numero_de_pessoas= int(input("quantas pessoas"))
valor_por_pessoas = valor_conta / numero_de_pessoas
print(f"valor por pessoa: {valor_por_pessoas:.2f}")
