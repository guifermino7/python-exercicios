#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2 m².

lar = float(input('Qual seria a largura da parede?\n'))
alt = float(input('Qual seria a altura da parede?\n'))

area = lar * alt

tinta = area / 2

print('A área da parede é {}{:.2f}{}m² e precisa de {}{:.2f}{}l de tinta para pinta-la!' .format('\033[4;35m', area, '\033[m', '\033[4;36m', tinta, '\033[m'))
