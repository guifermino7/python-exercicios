#Escreva um programa que leia a velocidade de um carro.
#Se ele ultrapassar 80 Km/h, mostre uma mensagem dizendo que ele foi multado.
#A multa vai custa R$ 7,00 por cada Km acima do limite.

vel = float(input('Qual é a velocidade do seu carro?\nKm/h: '))

if vel > 80:
    print('Você tomou multa e terá que pagar R$ {}.' .format((vel - 80) * 7))
else:
    print('Você está na abaixo do limite, tenha um ótimo dia! :)')
