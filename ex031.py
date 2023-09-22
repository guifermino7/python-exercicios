#Desenvolva um programa que pergunte a distância de uma viagem em Km.
#Calcule o preço da passagem, cobrando R$ 0,50 por Km para viagens de até 200 Km e R$ 0,45 para viagens mais longas.

km = float(input('Qual é a distância da viagem que você vai fazer?\nKm: '))

if km > 200:
    print('Sua viagem de {} Km irá custar R$ {:.2f}.' .format(km, km * 0.45))
else:
    print('Sua viagem de {} Km irá custar R$ {:.2f}.' .format(km, km * 0.50))
