#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado.
#Calcule o preço a pagar, sabendo que o carro custa R$ 60 por dia e R$ 0,15 por Km rodado.

dias = int(input('Por quantos dias você alugou o carro?\n'))
km = float(input('Quantos Km você percorreu com o carro?\n'))
precodia = 60 * dias
precokm = 0.15 * km
totalpreco = precodia + precokm
print('Você ficou com o carro por {} dias, resultando em R${:.2f}.' .format(dias, precodia))
print('Você andou {:.2f}km com o carro, resultando em R${:.2f}.' .format(km, precokm))
print('Ao todo, você terá que pagar R${:.2f}.' .format(totalpreco))
