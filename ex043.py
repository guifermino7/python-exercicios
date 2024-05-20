# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:

# Abaixo de 18.5: Abaixo do Peso;
# Entre 18.5 e 25: Peso ideal;
# 25 até 30: Sobrepeso;
# 30 até 40: Obesidade;
# Acima de 40: Obesidade mórbida.

import math

peso = float(input('Qual o seu peso?\n'))
altura = float(input('Qual é a sua altura?\n'))

imc = peso / (math.pow(altura, 2))

if(imc < 18.5):
    print('Com o IMC de {}{:.2f}{}, você está {}ABAIXO DO PESO{}.' .format('\033[4;34m', imc, '\033[m', '\033[1;31m', '\033[m'))
elif(18.5 <= imc < 25):
    print('Com o IMC de {}{:.2f}{}, você está {}COM PESO IDEAL{}.' .format('\033[4;34m', imc, '\033[m', '\033[1;32m', '\033[m'))
elif(25 <= imc < 30):
    print('Com o IMC de {}{:.2f}{}, você está {}SOBREBESO{}.' .format('\033[4;34m', imc, '\033[m', '\033[1;33m', '\033[m'))
elif(30 <= imc <= 40):
    print('Com o IMC de {}{:.2f}{}, você está {}OBESIDADE{}.'.format('\033[4;34m', imc, '\033[m', '\033[1;31m', '\033[m'))
else:
    print('Com o IMC de {}{:.2f}{}, você está com {}OBESIDADE MÓRBIDA{}.' .format('\033[4;34m', imc, '\033[m', '\033[1;41m', '\033[m'))
