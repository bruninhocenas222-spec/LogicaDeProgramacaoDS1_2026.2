# Função lambda
calcular_acrescimo = lambda valor: valor * 1.10

# Teste
valor = float(input("Digite um valor: "))

resultado = calcular_acrescimo(valor)

print(f"Valor com 10% de acréscimo: {resultado:.2f}")