#Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO.

from datetime import date

ano = int(input('Qual é o ano que você deseja verificar se é ou não bissexto? Caso deseje ver sobre o ano atual, digite 0.\n'))

if ano == 0:
    ano = date.today().year

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é BISSEXTO.' .format(ano))
else:
    print('O ano {} não é BISSEXTO.' .format(ano))
