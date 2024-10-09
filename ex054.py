'''
Crie um programa que leia o ano de nascimento de sete 
pessoas. No final, mostre quantas pessoas ainda não atingiram a 
maioridade e quantas já são maiores.
'''

for i in range(1,8):
    
    idade = int(input(f'Insira a {i} idade: '))
    
    if idade < 18:
        print(f'Você tem {idade} anos e ainda não atingiu a maioridade!')
    else:
        print(f'Você tem {idade} anos e já é de maior!')
        