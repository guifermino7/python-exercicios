#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

preco = float(input('Qual é o preço do produto?\nR$'))
desc = preco - (preco * 0.05)
print('O preço de R${} com 5% de desconto ficará R${}.' .format(preco, desc))
