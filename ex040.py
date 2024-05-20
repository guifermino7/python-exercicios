# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:

# Média abaixo de 5.0: REPROVADO;
# Média entre 5.0 e 6.9: RECUPERAÇÃO;
# Média 7.0 ou superior: APROVADO.

nota1 = float(input('Qual é a sua primeira nota, por favor?\n'))
nota2 = float(input('Qual é a sua segunda nota, por favor?\n'))

media = (nota1 + nota2) / 2

if(media < 5):
    print('Como sua média foi {}{:.2f}{}, você está {}REPROVADO{}!' .format('\033[4;36m', media, '\033[m', '\033[1;31m', '\033[m'))
elif( 5 <= media < 7):
    print('Como a sua média foi {}{:.2f}{}, você está de {}RECUPERAÇÃO{}!' .format('\033[4;36m', media, '\033[m', '\033[1;33m', '\033[m'))
else:
    print('Parabéns!!! Você está {}APROVADO{} com a média {}{:.2f}{}!' .format('\033[1;32m', '\033[m', '\033[4;36m', media, '\033[m'))