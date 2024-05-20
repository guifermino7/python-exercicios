# Crie um programa que faça o computador jogar Jokenpô (pedra, papel e tesoura) com você. Vale lembrar que as regras são:

# Pedra ganha da tesoura;
# Tesoura ganha do papel;
# Papel ganha da pedra;
# Objetos iguais são empate.

from random import randint
from time import sleep

escolhas = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)

print('Escolha abaixo uma das opções para jogar {}JOKENPÔ{}!' .format('\033[1;36m', '\033[m'))
print('{}[0]{} - {}PEDRA{}\n{}[1]{} - {}PAPEL{}\n{}[2]{} - {}TESOURA{}' .format('\033[7;36;40m', '\033[m', '\033[7;30;43m', '\033[m', '\033[7;36;40m', '\033[m', '\033[7;30;46m', '\033[m', '\033[7;36;40m', '\033[m', '\033[7;30;47m', '\033[m'))
jogador = int(input('Qual é a sua jogada?\n'))

if( 0 <= jogador < 3):
    print('{}JO{}...' .format('\033[1;34m', '\033[m'))
    sleep(1)
    print('{}KEN{}...' .format('\033[1;35m', '\033[m'))
    sleep(1)
    print('{}PÔ{}!!!' .format('\033[1;36m', '\033[m'))

    print('=-' * 13)
    print('O computador jogou {}!' .format(escolhas[computador]))
    print('O jogador jogou {}!' .format(escolhas[jogador]))
    print('=-' * 13)

    if(computador == 0):

        if(jogador == 0):
            print('{}EMPATE!{}' .format('\033[1;33m', '\033[m'))
        elif(jogador == 1):
            print('Jogador {}VENCEU!{}' .format('\033[1;32m', '\033[m'))
        elif(jogador == 2):
            print('Computador {}VENCEU{}!'. format('\033[1;36m', '\033[m'))
        else:
            print('Jogada {}INVÁLIDA{} do jogador! Por favor, jogue novamente.' .format('\033[1;31m', '\033[m'))
    elif(computador == 1):

        if (jogador == 0):
            print('Computador {}VENCEU{}!'.format('\033[1;36m', '\033[m'))
        elif (jogador == 1):
            print('{}EMPATE!{}'.format('\033[1;33m', '\033[m'))
        elif (jogador == 2):
            print('Jogador {}VENCEU!{}'.format('\033[1;32m', '\033[m'))
        else:
            print('Jogada {}INVÁLIDA{} do jogador! Por favor, jogue novamente.'.format('\033[1;31m', '\033[m'))

    elif(computador == 2):

        if (jogador == 0):
            print('Jogador {}VENCEU!{}'.format('\033[1;32m', '\033[m'))
        elif (jogador == 1):
            print('Computador {}VENCEU{}!'.format('\033[1;36m', '\033[m'))
        elif (jogador == 2):
            print('{}EMPATE!{}'.format('\033[1;33m', '\033[m'))
        else:
            print('Jogada {}INVÁLIDA{} do jogador! Por favor, jogue novamente.'.format('\033[1;31m', '\033[m'))

else:
    print('Opção de jogada {}INVÁLIDA{}! Por favor, escolha novamente.' .format('\033[1;31m', '\033[m'))
