investimento = float(input("Digite o valor total investido na campanha (R$): "))

cliques = int(input("Digite o numero total de cliques obtidos: "))

if cliques > 0:
    cpc = investimento / cliques

    print(f"\nO custo por clique (CPC) medio foi de R$ {cpc:.2f}.")

else:
    print("\nNao e possivel calcular o CPC sem cliques.")
