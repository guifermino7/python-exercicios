#Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

n1 = int(input('Digite um número, por favor: '))

db = n1 * 2
tp = n1 * 3
rq = pow(n1, (1/2))

print('Sobre o número {}{}{}, o seu dobro é {}{}{}, o triplo é {}{}{} e a raiz quadrada é {}{:.2f}{}.' .format('\033[4;36m', n1, '\033[m', '\033[7;40m', db, '\033[m', '\033[7;40m', tp, '\033[m', '\033[7;40m', rq, '\033[m'))
