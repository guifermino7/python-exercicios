# Refaça o desafio 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:

# Equilátero: todos os lados iguais;
# Isósceles: dois lados iguais;
# Escaleno: todos os lados diferentes.

lado1 = float(input('Qual seria o tamanho do primeiro lado?\n'))
lado2 = float(input('Qual seria o tamanho do segundo lado?\n'))
lado3 = float(input('Qual seria o tamanho do terceiro lado?\n'))

if lado1 < lado2 + lado3 and lado2 < lado1 + lado3 and lado3 < lado1 + lado2:
    print('As retas acima {}PODEM{} formar um triângulo.' .format('\033[1;32m', '\033[m'))

    if(lado1 == lado2 == lado3):
        print('O tipo do triângulo é {}EQUILÁTERO{}.' .format('\033[1;33m', '\033[m'))
    elif(lado1 == lado2 or lado2 == lado3 or lado1 == lado3):
        print('O tipo do triângulo é {}ISÓCELES{}.' .format('\033[1;33m', '\033[m'))
    else:
        print('O tipo do triângulo é {}ESCALENO{}.' .format('\033[1;33m', '\033[m'))
else:
    print('As retas acima {}NÃO PODEM{} formar um triângulo.' .format('\033[1;31m', '\033[m'))
