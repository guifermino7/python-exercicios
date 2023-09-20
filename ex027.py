#Faça um programa que leia o nome completo de uma pessoa e mostre em seguida o primeiro e o último nome separadamente.
#Ex: Ana Maria de Souza
#Primeiro = Ana
#Último = Souza

nome = input('Qual seu nome completo, por favor?\n')

dividido = nome.split()

print('O nome completo é: {}.' .format(nome))
print('O primeiro nome é: {}.' .format(dividido[0]))
print('O último nome é: {}.' .format(dividido[-1]))
