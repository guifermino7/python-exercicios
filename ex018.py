#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

import math

ang = float(input('Digite o ângulo que você deseja: '))

sen = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tan = math.tan(math.radians(ang))

print('O ângulo de {}{}{} tem o SENO de {}{:.2f}{}.' .format('\033[1;32m', ang, '\033[m', '\033[4;35m', sen, '\033[m'))
print('O ângulo de {}{}{} tem o COSSENO de {}{:.2f}{}.' .format('\033[1;32m', ang, '\033[m', '\033[4;34m', cos, '\033[m'))
print('O ângulo de {}{}{} tem a TANGENTE de {}{:.2f}{}.' .format('\033[1;32m', ang, '\033[m', '\033[4;33m', tan, '\033[m'))
