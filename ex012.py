#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

preco = float(input('Qual é o preço do produto?\nR$ '))

desc = preco - (preco * 0.05)

print('O preço de {}R${}{} com 5% de desconto ficará {}R${}{}.' .format('\033[1;32m', preco, '\033[m', '\033[4;32m', desc, '\033[m'))
