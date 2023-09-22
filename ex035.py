#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

lado1 = float(input('Qual seria o tamanho do primeiro lado?\n'))
lado2 = float(input('Qual seria o tamanho do segundo lado?\n'))
lado3 = float(input('Qual seria o tamanho do terceiro lado?\n'))

if lado1 < lado2 + lado3 and lado2 < lado1 + lado3 and lado3 < lado1 + lado2:
    print('As retas acima PODEM formar um triângulo.')
else:
    print('As retas acima NÃO PODEM formar um triângulo.')
