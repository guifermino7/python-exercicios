# Crie um programa que leia dois números de mostre a soma entre eles.

n1 = int(input('Digite um número, por favor: '))
n2 = int(input('Digite outro número, por favor: '))

soma = n1 + n2

print('A soma entre o número {}{}{} e {}{}{} é {}{}{}!' .format('\033[1;33m', n1, '\033[m', '\033[1;36m', n2, '\033[m', '\033[1;32m', soma, '\033[m'))
