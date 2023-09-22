#Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
#O programa deverá escrever na tela se o usuário venceu ou perde.

import random
import time

resposta = input('Olá, tudo bem? Vamos jogar um jogo? s/n\n')

if resposta == 's':
    print('Perfeito! Estou pensando em um número de 1 a 5...')
    time.sleep(3)

    numran = random.randint(1, 5)
    num = int(input('Qual número estou pensando?\n'))

    if num == numran:
        print('Parabéns! Era o número {} que eu pensando!' .format(num))
    else:
        print('Você perdeu! O número que eu estava pensando era {}!' .format(numran))

else:
    print('Tudo bem... até breve! :D')
