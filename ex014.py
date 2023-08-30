#Escreva um programa que converta uma temperatura digitada em °C e converta para °F.

c = float(input('Qual é a temperatura atual?\n°C: '))
f = ((9 * c) / 5) + 32
print('A temperatura de {}°C equivale a {}°F.' .format(c, f))
