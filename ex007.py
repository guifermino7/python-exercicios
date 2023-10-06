#Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

media = (nota1 + nota2)/2

print('A média entre as notas {}{:.1f}{} e {}{:.1f}{} é {}{:.1f}{}!' .format('\033[1;33m', nota1, '\033[m', '\033[1;36m', nota2, '\033[m', '\033[1;32m', media, '\033[m'))
