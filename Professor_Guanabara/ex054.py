'''
Crie um programa que leia o ano de nascimento de sete 
pessoas. No final, mostre quantas pessoas ainda não atingiram a 
maioridade e quantas já são maiores.
'''
from datetime import date

anoatual = date.today().year

for i in range(1,8):
    ano = int((input(f'Em que ano a {i} pessoa nasceu? ')))
    if anoatual - ano < 18:
        print('Você ainda não é maior de idade!')
    else:
        print('Você já é de maior!')
        
'''
Correção do Guanabara
from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0

for pess in range(1,8):
    nasc = int(input(f'Em que ano a {pess} pessoa nasceu? '))
    idade = atual - nasc
    if idade >= 21:
        print('Essa pessoa é maior')
        totmaior += 1
    else:
        print('Essa pessoa é menor')
        totmenor += 1
print(f'Ao todo tivemos {totmaior} pessoas maiores de idade')
print(f'Ao todo tivemos {totmenor} pessoas menores de idade')
'''