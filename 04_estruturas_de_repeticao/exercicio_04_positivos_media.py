"""
EXERCÍCIO 04: Positivos e Média
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Leia 6 valores numéricos.
Conte quantos foram estritamente positivos (> 0) e calcule a média aritmética deles.
Imprima a quantidade de positivos e a média formatada com 1 casa decimal.
"""

# TODO: Desenvolva o algoritmo abaixo:
quantidade = int(input("Quantos números você vai digitar? "))

contador = 0
soma = 0

for i in range(quantidade):
    numero = float(input("Digite um número: "))

    if numero > 0:
        contador += 1
        soma += numero

if contador > 0:
    media = soma / contador
else:
    media = 0

print(f"Quantidade de positivos: {contador}")
print(f"Média dos positivos: {media:.1f}")