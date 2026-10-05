"""
MVP 03: QUIZ EDUCACIONAL INTERATIVO COM RANKING
Disciplina: Lógica de Programação com Python
EEEP Professor Sebastião Vasconcelos Sobrinho

REQUISITOS DO SOFTWARE:
1. Banco de 5 perguntas de Lógica/Python em listas de dicionários.
2. Mecânica de perguntas, validação de alternativas e pontuação.
3. Persistência do ranking em ranking_jogadores.txt.
4. Exibição do Top 5 jogadores.
"""

# TODO: Desenvolva o sistema completo abaixo:
# QUIZ EDUCACIONAL

# Banco de perguntas
perguntas = [
    {
        "pergunta": "Qual é a linguagem de programação usada neste projeto?",
        "alternativas": ["A) Java", "B) Python", "C) C++", "D) JavaScript"],
        "resposta": "B"
    },
    {
        "pergunta": "Qual comando mostra uma mensagem na tela em Python?",
        "alternativas": ["A) print()", "B) input()", "C) mostrar()", "D) write()"],
        "resposta": "A"
    },
    {
        "pergunta": "Qual símbolo é usado para fazer um comentário em Python?",
        "alternativas": ["A) //", "B) /*", "C) #", "D) --"],
        "resposta": "C"
    },
    {
        "pergunta": "Qual função recebe uma informação digitada pelo usuário?",
        "alternativas": ["A) print()", "B) input()", "C) int()", "D) str()"],
        "resposta": "B"
    },
    {
        "pergunta": "Qual estrutura é usada para tomar decisões em Python?",
        "alternativas": ["A) if", "B) for", "C) import", "D) def"],
        "resposta": "A"
    }
]


# Pedir nome do jogador
nome = input("Digite seu nome: ")

pontuacao = 0

print("\n===== QUIZ EDUCACIONAL =====")

# Fazer as perguntas
for numero, pergunta in enumerate(perguntas, 1):

    print(f"\nPergunta {numero}:")
    print(pergunta["pergunta"])

    for alternativa in pergunta["alternativas"]:
        print(alternativa)

    # Validação da resposta
    while True:
        resposta = input("Digite a alternativa (A, B, C ou D): ").upper()

        if resposta in ["A", "B", "C", "D"]:
            break
        else:
            print("Resposta inválida! Digite apenas A, B, C ou D.")

    # Verificar resposta
    if resposta == pergunta["resposta"]:
        print("✓ Resposta correta!")
        pontuacao += 1
    else:
        print("✗ Resposta incorreta.")


# Resultado
print("\n===== RESULTADO =====")
print(f"Jogador: {nome}")
print(f"Pontuação: {pontuacao}/5")


# Salvar no arquivo
with open("ranking_jogadores.txt", "a", encoding="utf-8") as arquivo:
    arquivo.write(f"{nome};{pontuacao}\n")


# Ler ranking
jogadores = []

try:
    with open("ranking_jogadores.txt", "r", encoding="utf-8") as arquivo:

        for linha in arquivo:
            linha = linha.strip()

            if linha:
                nome_jogador, pontos = linha.split(";")
                jogadores.append((nome_jogador, int(pontos)))

except FileNotFoundError:
    pass


# Ordenar do maior para o menor
jogadores.sort(key=lambda jogador: jogador[1], reverse=True)


# Mostrar Top 5
print("\n===== TOP 5 JOGADORES =====")

for posicao, jogador in enumerate(jogadores[:5], 1):
    print(f"{posicao}º - {jogador[0]}: {jogador[1]} pontos")