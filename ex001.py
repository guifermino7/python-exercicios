#Crie um programa que escrava "Olá, Mundo!" na tela.

cores = {'limpa': '\033[m',
         'branco': '\033[1;30;43m',
         'vermelho': '\033[31m',
         'verde': '\033[32m',
         'amarelo': '\033[33m',
         'azul': '\033[34m',
         'roxo': '\033[35m',
         'ciano': '\033[36m',
         'cinza': '\033[37m',
         'preto': '\033[7;30m'}

print('{}O{}l{}á{}, {}m{}u{}n{}d{}o{}!{}' .format(cores['branco'], cores['limpa'], cores['vermelho'], cores['limpa'], cores['verde'], cores['limpa'], cores['amarelo'], cores['azul'], cores['roxo'], cores['ciano'], cores['cinza'], cores['preto'], cores['vermelho'], cores['verde'], cores['limpa']))
