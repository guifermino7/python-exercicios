# Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:

# O primeiro valor é maior;
# O segundo valor é maior;
# Não existe valor maior, os dois são iguais.

num1 = float(input('Digite um número, por favor: '))
num2 = float(input('Digite mais um número, por favor: '))

if(num1 > num2):
    print('O primeiro número, {}{:.2f}{}, é {}maior{} que o segundo, {}{:.2f}{}.' .format('\033[1;36m', num1, '\033[m', '\033[1;32m', '\033[m', '\033[1;36m', num2, '\033[m'))
elif(num2 > num1):
    print('O segundo número, {}{:.2f}{}, é {}maior{} que o primeiro, {}{:.2f}{}.' .format('\033[1;36m', num2, '\033[m', '\033[1;32m', '\033[m', '\033[1;36m', num1, '\033[m'))
else:
    print('Os números {}{:.2f}{} e {}{:.2f}{} são {}iguais{}.' .format('\033[1;36m', num1, '\033[m', '\033[1;36m', num2, '\033[m', '\033[1;33m', '\033[m'))
