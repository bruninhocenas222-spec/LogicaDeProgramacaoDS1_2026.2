idade = int(input("Digite a idade do visitante: "))

if idade < 12:
    tipo = "Infantil"
    valor = 50.00

elif idade >= 60:
    tipo = "Melhor Idade"
    valor = 0.00

else:
    tipo = "Integral"
    valor = 100.00

print("Tipo de bilhete:", tipo)
print(f"Valor final a pagar: R$ {valor:.2f}")