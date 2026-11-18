valor1 =int(input('digite o valor 1 :'))
valor2 =int(input('digite o valor 2 :'))
valor3 =int(input('digite o valor 3 :'))
media = (valor1 + valor2 + valor3)/3
if media >= 7:
    print('aprovado')
elif media == 6:
    print('em recuperação')
else:
  print('reprovado')