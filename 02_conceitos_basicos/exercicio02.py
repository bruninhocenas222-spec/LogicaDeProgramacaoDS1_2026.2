distancia = float(input("Digite a distancia total percorrida (KM): "))

combustivel = float(input("Digite o valor total gasto (litros): "))

if combustivel > 0:
    consumo = distancia / combustivel

    print(f"\nO consumo medio da motocicleta foi de {consumo:.2f} KM/L.")

else:
    print("\nNao e possivel calcular o consumo sem combustivel.")
