#Crie um programa que leia o nome completo de uma pessoa e mostre:
#O nome com todas as letras maiúsculas;
#O nome com todas as letras minúsculas;
#Quantas letras ao todo (sem considerar espaços);
#Quantas letras tem o primeiro nome.

nome = input('Qual seu nome?\n')

print('O nome com todas as letras maiúsculas é {}.'.format(nome.upper()))
print('O nome com todas as letras minúsculas é {}.' .format(nome.lower()))
print('Possui {} letras (sem considerar espaços).' .format(len(nome.replace(" ",""))))

dividido = nome.split()

print('O primeiro nome tem {} letras.' .format(len(dividido[0])))
