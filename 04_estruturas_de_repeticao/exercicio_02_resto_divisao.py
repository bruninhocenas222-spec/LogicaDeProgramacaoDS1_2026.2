"""
EXERCÍCIO 02: Resto da Divisão por 5
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Leia dois valores inteiros X e Y.
Utilize o laço for para imprimir todos os inteiros entre X e Y (em ordem crescente)
cujo resto da divisão por 5 seja igual a 2 ou igual a 3.
"""

# TODO: Desenvolva o algoritmo abaixo:
x = int(input("Digite o valor de X: "))
y = int(input("Digite o valor de Y: "))

inicio = min(x, y)
fim = max(x, y)

for numero in range(inicio, fim + 1):
    resto = numero % 5

    if resto == 2 or resto == 3:
        print(numero)