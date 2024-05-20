# Faça o programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:

# Se ele ainda vai se alistar ao serviço militar;
# Se é a hora de se alistar;
# Se já passou do tempo do alistamento.

# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

import datetime

ano = int(input('Qual é ano do seu nascimento?\n'))
today = datetime.date.today()
hoje = today.strftime("%Y")
idade = int(hoje) - ano

if(idade < 18):
    print('Como você tem {}{}{} anos, ainda {}não precisa{} se alistar.' .format('\033[4;36m', idade, '\033[m', '\033[1;33m', '\033[m'))
elif(idade == 18):
    print('Como você já tem {}{}{} anos, {}está na hora{} de se alistar.' .format('\033[4;36m', idade, '\033[m', '\033[1;32m', '\033[m'))
else:
    print('Já passou da idade de se alistar, caso não tenha se alistado, {}vá se alistar{}!' .format('\033[1;31m', '\033[m'))
print('Tenha um ótimo dia!')