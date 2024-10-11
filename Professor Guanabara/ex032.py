#Faça um programa que leia um ano qualquer e diga se é bissexto ou não
from datetime import date
try: 
    ano = int(input('Diga-me um ano e eu direi se ele é bissexto ou não, Digite "0" se quiser saber o atual\nR: '))
    if ano == 0:
        ano = date.today().year
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        print(f'O ano {ano} é bissexto')
    else:
        print(f'O ano {ano} não é bissexto')
except ValueError:
    print('Por favor, digite um ano válido (apenas números).')
