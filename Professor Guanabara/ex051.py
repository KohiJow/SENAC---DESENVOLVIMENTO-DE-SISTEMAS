'''
Desenvolva um programa que leia o primeiro termo e a razão de uma PA. 
No final, mostre os 10 primeiros termos dessa progressão.
'''
razao = int(input('Qual sua razão: '))
termo = int(input('Digite o primeiro termo: '))

print('Os 10 primeiros termos são:')

for i in range(10):
    print(termo, end=' ')
    termo += razao
    