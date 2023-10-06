#Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e antecessor.

n1 = int(input('Digite um número, por favor: '))

suc = n1 + 1
ant = n1 - 1

print('Sobre o número {}{}{}, o antecessor é {}{}{} e sucessor é {}{}{}!' .format('\033[4;36m', n1, '\033[m', '\033[1;30;41m', ant, '\033[m', '\033[1;30;42m', suc, '\033[m'))
