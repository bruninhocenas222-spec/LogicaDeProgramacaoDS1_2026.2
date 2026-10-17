"""
EXERCÍCIO 04: Função Lambda de Desconto Casas Paulino
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Escreva uma função anônima (lambda) que receba o valor de um produto
e retorne o valor com 15% de desconto à vista aplicado.
"""

# TODO: Desenvolva a expressão lambda e teste-a abaixo:
#funçao lambda aplicar 15% de desconto
desconto = lambda valor: valor * 0.85
#recena o valor
valor = float(input("digite o valor do produto R$:"))
#calcular e mostrar o desconto
valor_final = desconto(valor)
print(f"o valor do produto com 15% de desconto é R${valor_final:.2f}")
