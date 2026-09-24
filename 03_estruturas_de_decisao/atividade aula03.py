opcao = int(input("Digite a opção desejada (1, 2 ou 3): "))

match opcao:
    case 1:
        print("Você escolheu: Consultar livro.")
    case 2:
        print("Você escolheu: Realizar empréstimo.")
    case 3:
        print("Você escolheu: Devolver livro.")
    case _:
        print("Opção não encontrada.")