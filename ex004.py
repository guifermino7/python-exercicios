#Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

elm = input('Digite algo: ')
print('O tipo primitivo desse valor é', type(elm))
print('Só tem espaços?', elm.isspace())
print('É um número?', elm.isnumeric())
print('É alfabético?', elm.isalpha())
print('É alfanumérico?', elm.isalnum())
print('Está em maíusculas?', elm.isupper())
print('Está em minúsculas?', elm.islower())
print('Está capitalizada?', elm.istitle())
