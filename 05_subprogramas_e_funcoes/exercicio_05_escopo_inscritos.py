"""
EXERCÍCIO 05: Gestão de Escopo Global e Local
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Declare a variável global total_inscritos = 0.
Crie a função `inscrever_aluno(quantidade)` utilizando a diretiva `global`
para atualizar a variável. Demonstre o valor de total_inscritos antes e depois da chamada.
"""

# TODO: Desenvolva o algoritmo abaixo:
# 1. Declaração da variável global
total_inscritos = 0

# 2. Definição da função com a diretiva global
def inscrever_aluno(quantidade):
    global total_inscritos
    total_inscritos += quantidade
# 3. Demonstração dos valores antes da chamada
print(f"Total de inscritos antes: {total_inscritos}")
# 4. Receber o valor digitado pelo utilizador
quantidade_digitada = int(input("Digite a quantidade de alunos para inscrever: "))
# Chamada da função com o valor inserido
inscrever_aluno(quantidade_digitada)
# Demonstração do valor depois da chamada
print(f"Total de inscritos depois: {total_inscritos}")