codigo = int(input("Digite o código do item: "))
quantidade = int(input("Digite a quantidade: "))

if codigo == 1:
    preco = 4.00
elif codigo == 2:
    preco = 4.50
elif codigo == 3:
    preco = 5.00
elif codigo == 4:
    preco = 2.00
elif codigo == 5:
    preco = 1.50
else:
    print("Código inválido.")
    preco = 0

total = preco * quantidade

if preco > 0:
    print(f"Total a pagar: R$ {total:.2f}")