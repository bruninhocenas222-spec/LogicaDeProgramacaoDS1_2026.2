"""
EXERCÍCIO 02: Modularizando Relatório de Viagem
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Crie duas funções:
1. `calcular_custo_transporte(distancia_km, consumo_kml, preco_combustivel)`
2. `calcular_custo_alimentacao(qtd_pessoas, dias, diaria_alimentacao)`

No programa principal, leia os dados, execute as funções e mostre o custo total da viagem.
"""

# TODO: Desenvolva as funções e o programa principal abaixo:
def calcular_custo_transporte(distancia_km, consumo_kml, preco_combustivel):
    return (distancia_km / consumo_kml) * preco_combustivel

def calcular_custo_alimentacao(qtd_pessoas, dias, diaria_alimentacao):
    return qtd_pessoas * dias * diaria_alimentacao

distancia = float(input("digite a distância em KM:"))
consumo = float(input("digite o consumo do veiculo KM/L:"))
preco = float(input("digite o preço do combustivel:"))

pessoas = int(input("digite a quantidade de pessoas:"))
dias_viagem = int(input("digite a quantidades de dias:"))
diaria = float(input("digite o valor da diaria da alimentação:"))

custo_transporte = calcular_custo_transporte(distancia, consumo, preco)
custo_alimentacao = calcular_custo_alimentacao(pessoas, dias_viagem, diaria)

custo_total = custo_transporte + custo_alimentacao
print(f"Custo total da viagem: R$ {custo_total:.2f}")