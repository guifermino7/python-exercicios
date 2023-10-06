#Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.

from random import choice

aluno1 = input('Qual o nome do primeiro aluno?\n')
aluno2 = input('Qual o nome do segundo aluno?\n')
aluno3 = input('Qual o nome do terceiro aluno?\n')
aluno4 = input('Qual o nome do quarto aluno?\n')

lista = [aluno1, aluno2, aluno3, aluno4]
escolhido = choice(lista)

print('O aluno sorteado foi {}{}{}!' .format('\033[4;35m', escolhido, '\033[m'))
