"""
DESAFIO 04: REFATORAÇÃO INVESTIGATIVA
Disciplina: Lógica de Programação com Python

RELATÓRIO DA INVESTIGAÇÃO:
O código monolítico repete cálculos de desconto e impostos várias vezes.

SUA MISSÃO:
1. Crie uma função calcular_preco_final(preco_base, taxa_desc, taxa_imp) com return.
2. Crie um procedimento exibir_relatorio_item(numero_item, preco_final) com print.
3. Teste suas funções refatoradas.
"""

# TODO: Desenvolva as funções modulares abaixo:
# 1. Função para calcular o preço final com desconto e imposto
def calcular_preco_final(preco_base, taxa_desc, taxa_imp):
    valor_com_desconto = preco_base * (1 - taxa_desc)
    preco_final = valor_com_desconto * (1 + taxa_imp)
    return preco_final

# 2. Procedimento para exibir o relatório do item
def exibir_relatorio_item(numero_item, preco_final):
    print(f"Item {numero_item}: Preço Final = R$ {preco_final:.2f}\n")

# 3. Teste das funções refatoradas com entrada do utilizador
if __name__ == "__main__":
    print("=== TESTE DAS FUNÇÕES REFATORADAS ===")
    
    # Permite ao utilizador testar múltiplos itens interativamente
    quantidade_itens = int(input("Digite a quantidade de itens que deseja calcular: "))
    
    for i in range(1, quantidade_itens + 1):
        print(f"\n--- Dados do Item {i} ---")
        preco_base = float(input("Digite o preço base do item (R$): "))
        taxa_desc = float(input("Digite a taxa de desconto (ex: 0.10 para 10%): "))
        taxa_imp = float(input("Digite a taxa de imposto (ex: 0.05 para 5%): "))
        
        # Chamada da função e do procedimento
        preco_final = calcular_preco_final(preco_base, taxa_desc, taxa_imp)
        exibir_relatorio_item(i, preco_final)