#Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

num1 = float(input('Qual seria o primeiro número, por favor?\n'))
num2 = float(input('Qual seria o segundo número, por favor?\n'))
num3 = float(input('Qual seria o terceiro número, por favor?\n'))

menor = num1

if num2 < num1 and num2 < num3:
    menor = num2
if num3 < num1 and num3 < num2:
    menor = num3

maior = num1

if num2 > num1 and num2 > num3:
    maior = num2
if num3 > num1 and num3 > num2:
    maior = num3

print('O maior valor é {} e o menor valor é {}.' .format(maior, menor))
