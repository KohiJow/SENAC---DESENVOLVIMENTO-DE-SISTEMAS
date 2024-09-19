'''
A confederação nacional de natação precisa de um programa que leia o ano de nascimento 
de um atleta e mostre sua categoria de acordo com sua idade:
-Até 9 anos: MIRIM
-Até 14 anos: INFANTIL
-Até 19 anos: JÚNIOR
-Até 20 anos: SÊNIOR
Acima: MASTER
'''
nome= str(input('\033[1;34mOlá! Qual seu nome?\033[m\n'))
print(f'\033[1;34mOlá {nome}, por favor me diga sua idade:\033[m')
idade = int(input())

if idade == 9:
    print('-*-' * 12)
    print(f'Atleta:{nome}\nClasse: MIRIM')
    print('-*-' * 12)
elif idade > 9 and idade < 14:
    print('-*-' * 12)
    print(f'Atleta:{nome}\nClasse: INFANTIL')
    print('-*-' * 12)
elif idade > 14 and idade < 20:
    print('-*-' * 12)
    print(f'Atleta:{nome}\nClasse: JÚNIOR')
    print('-*-' * 12)
elif idade == 20:
    print('-*-' * 12)
    print(f'Atleta:{nome}\nClasse: SÊNIOR')
    print('-*-' * 12)
elif idade > 20:
    print('-*-' * 12)
    print(f'Atleta:{nome}\nClasse: MASTER')
    print('-*-' * 12)
else:
    print('-*-' * 12)
    print('Você ainda é muito novo pra competir')
    print('-*-' * 12)
