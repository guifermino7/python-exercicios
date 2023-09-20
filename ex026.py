#Faça um programa que leia uma frase pelo teclado e mostre:
#Quantas vezes aparece a letra "A";
#Em que posição ela aparece a primeira vez;
#Em que posição ela aparece a última vez.

frase = input('Digite algo: ').strip()

print('Aparece {} vezes a letra "A" na frase.' .format(frase.upper().count('A')))
print('Aparece pela primeira vez a letra "A" na posição {}.' .format(frase.upper().find('A') + 1))
print('Aparece pela última vez a letra "A" na posição {}.' .format(frase.upper().rfind('A') + 1))
