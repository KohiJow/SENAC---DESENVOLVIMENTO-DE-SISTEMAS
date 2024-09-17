#Escreva um programa que faça o computador "pensar" em um número entre 0 e 5
#e peça para o usuário tentar descobrir qual foi o número
#escolhido pelo computador.
#O programa deverá escrever na tela se o usuário venceu ou perdeu.

import random
num = [1,2,3,4,5]
user = (input('Tente advinhar em que número estou pensando entre 1 a 5: '))

if user == random.choice(num):
    print('Caramba você lê mentes? era esse mesmo!')
elif type(user) != int:
    print('Insira um número de 1 a 5 burro')
else:
    print('Ha! Errou!')
