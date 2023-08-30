#Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

m = float(input('Digite um valor em metros, por favor: '))
cm = m * 100
mm = m * 1000
km = m / 1000
print('O valor {} está em metros e fica {:.0f} em centímetros e {:.0f} em milímetros!' .format(m, cm, mm))
print('Por curiosidade, o valor {}, que está em metros, fica {} em quilômetros!' .format(m, km))
