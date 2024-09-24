'''
Faça um programa que leia o ano de nascimento de um jovem e informe,
de acordo com sua idade:
-Se ele ainda vai se alistar ao serviço militar.
-Se é a hora de se alistar.
-se já passou do tempo do alistamento.
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
'''

ano = int(input('Em que ano você nasceu? '))

idade = 2024 - ano

if idade < 18:
    print(f'Faltam {18 - idade} anos para poder se alistar') 

elif idade > 18:
    print(f'Você está atrasado {idade - 18} anos para poder se alistar') 

else:
    print('Você deve se alistar ainda esse ano ') #by maranhao

    #correção
'''
    from datetime import datetime

# Pega o ano atual
ano_atual = datetime.now().year

# Entrada do ano de nascimento
ano_nascimento = int(input('Em que ano você nasceu? '))

# Calcula a idade
idade = ano_atual - ano_nascimento

# Verifica a situação do alistamento
if idade < 18:
    print(f'Faltam {18 - idade} anos para o seu alistamento.')
elif idade > 18:
    print(f'Você está atrasado {idade - 18} anos para o alistamento.')
else:
    print('Você deve se alistar este ano.')
'''