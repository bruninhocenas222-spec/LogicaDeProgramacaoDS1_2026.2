#def novoSalario (salario):
#    return salario + (salario * 0.15)
#salario = float (input("Qual salario?"))
#resultado = novoSalario(salario)
#print (f"{resultado}")

#def totalSalario (porHora, numeroHora):
    #total = (porHora * numeroHora)
    #return total
#porHora = float (input ("Quanto você ganha por hora?"))
#numeroHora = float (input ("Quantas horas você trabalha?"))

#print (f"Resultado {totalSalario(porHora,numeroHora)}")

#def precoDesconto (preco):
    if preco>200:
       return preco - (preco*0.10)
    if preco>50.00:
        return preco - (preco*0.05)
    else:
        return preco 
preco = float (input("Qual o preço do produto?"))

print (precoDesconto(preco))
