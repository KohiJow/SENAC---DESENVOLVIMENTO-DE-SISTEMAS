#Faça um programa que leia um ano qualquer e diga se é bissexto ou não
try:
    ano = int(input('Diga-me um ano e eu direi se ele é bissexto ou não\nR: '))

    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        print('O ano é bissexto')
    else:
        print('O ano não é bissexto')
except ValueError:
    print('Por favor, digite um ano válido (apenas números).')
