#O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos. Fçaa um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
import random

aluno1 = input('Qual seria o nome do primeiro aluno?\n')
aluno2 = input('Qual seria o nome do segundo aluno?\n')
aluno3 = input('Qual seria o nome do terceiro aluno?\n')
aluno4 = input('Qual seria o nome do quarto aluno?\n')

lista = [aluno1, aluno2, aluno3, aluno4]
random.shuffle(lista)

print('A ordem de apresentação será:\n', lista)
