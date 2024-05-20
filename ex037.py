# Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:

# 1 para binário;
# 2 para octal;
# 3 para hexadecimal.

num = int(input('Digite um número inteiro, por favor: '))
print('Qual será o tipo de conversão que você irá escolher?')
choose = int(input('{}1{} - {}BINÁRIO{}\n{}2{} - {}OCTAL{}\n{}3{} - {}HEXADECIMAL{}\n'. format('\033[4;32m', '\033[m', '\033[1;33m', '\033[m', '\033[4;32m', '\033[m', '\033[1;33m', '\033[m', '\033[4;32m', '\033[m', '\033[1;33m', '\033[m')))

if(choose == 1):
    print('O número {}{}{} convertido para {}BINÁRIO{} é igual a {}{}{}.' .format('\033[1;32m', num, '\033[m', '\033[1;33m', '\033[m', '\033[4;36m', bin(num)[2:], '\033[m'))
elif(choose == 2):
    print('O número {}{}{} convertido para {}OCTAL{} é igual a {}{}{}.' .format('\033[1;32m', num, '\033[m', '\033[1;33m', '\033[m', '\033[4;36m', oct(num)[2:], '\033[m'))
elif(choose == 3):
    print('O número {}{}{} convertido para {}HEXADECIMAL{} é igual a {}{}{}.' .format('\033[1;32m', num, '\033[m', '\033[1;33m', '\033[m', '\033[4;36m', hex(num)[2:], '\033[m'))
else:
    print('{}Opção incorreta!{} Por favor, selecione novamente {}1{}, {}2{} ou {}3{}.' .format('\033[1;31m', '\033[m', '\033[4;32m', '\033[m', '\033[4;32m', '\033[m', '\033[4;32m', '\033[m'))
