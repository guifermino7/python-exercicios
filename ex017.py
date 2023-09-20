#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.
import math

print('Sobre um triângulo retângulo...')
catop = float(input('Qual é o comprimento do cateto oposto?\n'))
catad = float(input('Qual é o comprimento do cateto adjacente?\n'))

hip = math.hypot(catop, catad)

print('O calculo da hipotenusa dos catetos  {} e {}, adjacente e oposto, respectivamente, é {:.2f}' .format(catop, catad, hip))
