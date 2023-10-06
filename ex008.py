#Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

m = float(input('Digite um valor em metros, por favor: '))

cm = m * 100
mm = m * 1000
km = m / 1000

print('O valor {}{}{} está em metros e fica {}{:.1f}{} em centímetros e {}{:.1f}{} em milímetros!' .format('\033[1;31m', m, '\033[m', '\033[1;31m', cm, '\033[m', '\033[1;31m', mm, '\033[m'))
print('Por curiosidade, o valor {}{}{}, que está em metros, fica {}{:.2f}{} em quilômetros!' .format('\033[1;36m', m, '\033[m', '\033[1;36m', km, '\033[m'))
