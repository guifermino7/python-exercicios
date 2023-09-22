#Crie um programa que leia um número inteiro e mostre se ele é PAR ou ÍMPAR.

num = int(input('Digite um número: '))

if num % 2 == 1:
    print('O número {} é ÍMPAR.' .format(num))
else:
    print('O número {} é PAR.' .format(num))
