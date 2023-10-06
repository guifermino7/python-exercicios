#Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada.

num = int(input('Digite um número, por favor: '))

print('{}============={}' .format('\033[1;33m', '\033[m'))

print('{:2} x {} = {}{}{}' .format(1, num, '\033[7;40m', num*1, '\033[m'))
print('{:2} x {} = {}{}{}' .format(2, num, '\033[7;40m', num*2, '\033[m'))
print('{:2} x {} = {}{}{}' .format(3, num, '\033[7;40m', num*3, '\033[m'))
print('{:2} x {} = {}{}{}' .format(4, num, '\033[7;40m', num*4, '\033[m'))
print('{:2} x {} = {}{}{}' .format(5, num, '\033[7;40m', num*5, '\033[m'))
print('{:2} x {} = {}{}{}' .format(6, num, '\033[7;40m', num*6, '\033[m'))
print('{:2} x {} = {}{}{}' .format(7, num, '\033[7;40m', num*7, '\033[m'))
print('{:2} x {} = {}{}{}' .format(8, num, '\033[7;40m', num*8, '\033[m'))
print('{:2} x {} = {}{}{}' .format(9, num, '\033[7;40m', num*9, '\033[m'))
print('{:2} x {} = {}{}{}' .format(10, num, '\033[7;40m', num*10, '\033[m'))

print('{}============={}' .format('\033[1;33m', '\033[1;33m'))
