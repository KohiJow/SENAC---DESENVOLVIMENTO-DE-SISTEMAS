#Crie um programa que diga se uma pessoa pode dirigir ou não, com base nos valores idade, altura e nome.

print('Olá, seja bem-vindo!')

nome = input('Qual seu nome: ')
print(f'Olá {nome}!')

idade = int(input('Qual sua idade: '))
altura = float(input('Digite sua altura em metros: '))

if idade < 18:
    print('Você ainda não tem idade suficiente para dirigir.')
elif altura < 1.60:
    print('Você não tem altura suficiente para dirigir.')
else:
    print('Você pode dirigir!')
