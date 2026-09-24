media_aluno = float(input("Digite a média do aluno: "))
frequencia_percentual = float(input("Digite a frequência do aluno (%): "))

aprovado = media_aluno >= 6.0 and frequencia_percentual >= 75

if aprovado:
    print("Aluno aprovado!")
else:
    print("Aluno reprovado!")
