#Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO".

cidade = input('Qual é o nome da cidade?\n').strip()

print('Começa "SANTO" no nome? {}' .format('SANTO' in cidade[:5].upper()))
