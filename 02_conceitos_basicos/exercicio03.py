consumo = float(input("digite o valor total consumido no restaurante (R$): "))
taxa_servico = consumo * 0.10
valor_final = consumo + taxa_servico

print(f"\nvalor consumido: R${consumo:.2f}")
print(f"taxa de serviço  (10%): R$ {taxa_servico:.2f}")
print(f"valor final da conta: R$ {valor_final:.2f}")