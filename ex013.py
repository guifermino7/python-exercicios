#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salario = float(input('Qual é o salário atual do funcionário?\nR$ '))

aum = salario + (salario * 0.15)

print('O salário atual do funcionário é {}R${:.2f}{} e com acréscimo fica {}R${:.2f}{}.' .format('\033[1;32m', salario, '\033[m', '\033[4;32m', aum, '\033[m'))
