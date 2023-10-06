#Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

elm = input('Digite algo: ')

print('O tipo primitivo desse valor é', '\033[1;33m', type(elm), '\033[m')
print('Só tem espaços?', '\033[1;33m', elm.isspace(), '\033[m')
print('É um número?', '\033[1;33m', elm.isnumeric(), '\033[m')
print('É alfabético?', '\033[1;33m', elm.isalpha(), '\033[m')
print('É alfanumérico?', '\033[1;33m', elm.isalnum(), '\033[m')
print('Está em maíusculas?', '\033[1;33m', elm.isupper(), '\033[m')
print('Está em minúsculas?', '\033[1;33m', elm.islower(), '\033[m')
print('Está capitalizada?', '\033[1;33m', elm.istitle(), '\033[m')
