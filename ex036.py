# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.

precoCasa = float(input('Qual seria o valor da casa?\n'))
salario = float(input('Qual o salário do comprador?\n'))
tempo = int(input('Em quantos anos você irá pagar?\n'))

valorMensal = precoCasa / (tempo * 12)

print('O valor da mensalidade das prestações é de R$ {}{:.2f}{}.' .format('\033[4;33m', valorMensal, '\033[m'))
if valorMensal > salario * 0.3:
    print('Infelizmente {}não{} será possível realizar o empréstimo.' .format('\033[1;31m', '\033[m'))
else:
    print('Empréstimo {}aprovado{}! Parabéns!!!' .format('\033[1;32m', '\033[m'))
print('Tenha um ótimo dia!')
