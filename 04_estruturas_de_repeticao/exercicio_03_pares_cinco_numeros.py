"""
EXERCÍCIO 03: Pares entre Cinco Números
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Solicite 5 números inteiros ao usuário.
Utilize uma estrutura de repetição e um contador para verificar quantos números pares
foram digitados. Ao final, imprima a quantidade total.
"""

# TODO: Desenvolva o algoritmo abaixo
from unicodedata import numeric


contador = 0 
for i in range(5):
    numero = int(input('digite o numero'))
    if numero % 2 == 0:
        contador = contador + 1 

print(f"o numero de numeros pares e {contador}")
