#Crie um programa que leia o nome e mostre uma mensagem de boas-vindas.

nome = input('Digite seu nome: ')
print('É um prazer te conhecer, {}{}{}!' .format( '\033[1:35m', nome, '\033[m'))
