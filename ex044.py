# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:

# À vista dinheiro/cheque: 10% de desconto;
# À vista no cartão: 5% de desconto;
# Em até 2x no cartão: preço normal;
# 3x ou mais no cartão: 20% de juros.

print('{:=^50}' .format(' LOJAS FERMINO '))
print('Seja muito bem vindo(a)!')

preco = float(input('Qual é o valor do produto?\nR$ '))
print('Qual vai ser o tipo de pagamento?')
print('{}[1]{} - {}À vista dinheiro/cheque{};\n{}[2]{} - {}À vista no cartão{};\n{}[3]{} - {}Em até 2x no cartão{};\n{}[4]{} - {}3x ou mais no cartão{}.'. format('\033[7;30;47m', '\033[m', '\033[1;33m', '\033[m', '\033[7;30;47m', '\033[m', '\033[1;33m', '\033[m', '\033[7;30;47m', '\033[m', '\033[1;33m', '\033[m', '\033[7;30;47m', '\033[m', '\033[1;33m', '\033[m'))
choose = int(input('Qual seria a sua escolha?\n'))

if(choose == 1):
    desconto = preco * 0.10
    precoFinal = preco - desconto

    print('O produto de valor {}R${:.2f}{} terá {}DESCONTO{} de {}R${:.2f}{} devido o tipo de pagamento.' .format('\033[4;36m', preco, '\033[m', '\033[1;32m', '\033[m', '\033[4;33m', desconto, '\033[m'))
    print('O valor final da sua compra é {}R${:.2f}{}.'.format('\033[1;35m', precoFinal, '\033[m'))
    print('Tenha um bom dia! Volte sempre!')

elif(choose == 2):
    desconto = preco * 0.05
    precoFinal = preco - desconto

    print('O produto de valor {}R${:.2f}{} terá {}DESCONTO{} de {}R${:.2f}{} devido o tipo de pagamento.' .format('\033[4;36m', preco, '\033[m', '\033[1;32m', '\033[m', '\033[4;33m', desconto, '\033[m'))
    print('O valor final da sua compra é {}R${:.2f}{}.' .format('\033[1;35m', precoFinal, '\033[m'))
    print('Tenha um bom dia! Volte sempre!')

elif(choose == 3):
    qtdParcela = int(input('Você irá parcelar em 1x ou 2x?\n'))
    parcela = preco / qtdParcela

    if(1 <= qtdParcela <= 2):
        precoFinal = preco

        print('Infelizmente, este tipo de pagamento {}NÃO TERÁ DESCONTO{}.'.format('\033[1;33m', '\033[m'))
        print('Sua compra será parcelada em {}{}x{} de {}R${:.2f}{}.' .format('\033[4;34m', qtdParcela, '\033[m', '\033[4;36m', parcela, '\033[m'), end=' ')

    else:
        juros = preco * 0.20
        precoFinalJuros = preco + juros
        parcelaJuros = precoFinalJuros / qtdParcela
        precoFinal = precoFinalJuros

        print('O produto de valor {}R${:.2f}{} terá {}JUROS{} de {}R${:.2f}{} devido o tipo de pagamento.'.format('\033[4;36m', preco, '\033[m', '\033[1;31m', '\033[m', '\033[4;33m', juros, '\033[m'))
        print('Sua compra será parcelada em {}{}x{} de {}R${:.2f}{}, {}COM JUROS{}.'.format('\033[4;34m', qtdParcela, '\033[m', '\033[4;36m', parcelaJuros, '\033[m', '\033[1;31m', '\033[m'), end=' ')

    print('O valor final da sua compra é {}R${:.2f}{}.'.format('\033[1;35m', precoFinal, '\033[m'))
    print('Tenha um bom dia! Volte sempre!')

elif(choose == 4):
    qtdParcela = int(input('Você irá parcelar em quantas vezes?\n'))
    parcela = preco / qtdParcela
    juros = preco * 0.20
    precoFinalJuros = preco + juros
    parcelaJuros = precoFinalJuros / qtdParcela

    if(1 <= qtdParcela <= 2):
        precoFinal = preco
        print('Infelizmente, este tipo de pagamento {}NÃO TERÁ DESCONTO{}.'.format('\033[1;33m', '\033[m'))
        print('Sua compra será parcelada em {}{}x{} de {}R${:.2f}{}.'.format('\033[4;34m', qtdParcela, '\033[m', '\033[4;36m', parcela, '\033[m'), end=' ')
    else:
        precoFinal = precoFinalJuros
        print('O produto de valor {}R${:.2f}{} terá {}JUROS{} de {}R${:.2f}{} devido o tipo de pagamento.' .format('\033[4;36m', preco, '\033[m', '\033[1;31m', '\033[m', '\033[4;33m', juros, '\033[m'))
        print('Sua compra será parcelada em {}{}x{} de {}R${:.2f}{}, {}COM JUROS{}.' .format('\033[4;34m', qtdParcela, '\033[m', '\033[4;36m', parcelaJuros, '\033[m', '\033[1;31m', '\033[m'), end=' ')

    print('O valor final da sua compra é {}R${:.2f}{}.'.format('\033[1;35m', precoFinal, '\033[m'))
    print('Tenha um bom dia! Volte sempre!')

else:
    print('Opção de pagamento {}INVÁLIDA{}! Por favor, tente novamente.'.format('\033[1;31m', '\033[m'))
