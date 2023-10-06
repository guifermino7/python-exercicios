#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
#Considere US$ 1,00 = R$ 3,27.

din = float(input('Quanto você tem de dinheiro na carteira?\nR$ '))

dol = din / 3.27

print('Você possui {}{:.2f}{} reais e pode comprar {}{:.2f}{} doláres!' .format('\033[4;31m', din, '\033[m', '\033[4;32m', dol, '\033[m'))
