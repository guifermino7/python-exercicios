#Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e antecessor.

n1 = int(input('Digite um número, por favor: '))
suc = n1 + 1
ant = n1 - 1
print('Sobre o número {}, o antecessor é {} e sucessor é {}!' .format(n1, ant, suc))
