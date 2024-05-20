# A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:

# Até 9 anos: MIRIM;
# Até 14 anos: INFANTIL;
# Até 19 anos: JUNIOR;
# Até 20 anos: SÊNIOR;
# Acima: MASTER.

import datetime

ano = int(input('Qual é o ano do seu nascimento?\n'))
today = datetime.date.today()
hoje = today.strftime('%Y')
idade = int(hoje) - ano

if(idade <= 9):
    print('Com a idade de {}{}{} anos, sua categoria é MIRIM.' .format('\033[1;36m', idade, '\033[m'))
elif(9 < idade <= 14):
    print('Com a idade de {}{}{} anos, sua categoria é INFANTIL.' .format('\033[1;36m', idade, '\033[m'))
elif(14 < idade <= 19):
    print('Com a idade de {}{}{} anos, sua categoria é JUNIOR.' .format('\033[1;36m', idade, '\033[m'))
elif(20 < idade <= 25):
    print('Com a idade de {}{}{} anos, sua categoria é SÊNIOR.' .format('\033[1;36m', idade, '\033[m'))
else:
    print('Com a idade de {}{}{} anos, sua categoria é MASTER.' .format('\033[1;36m', idade, '\033[m'))
