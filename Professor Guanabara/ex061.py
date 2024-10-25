'''
Refaça o DESAFIO051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos
da progressão usando a estrutura while.
'''
i = 1
razao = int(input('Qual sua razão: '))
termo = int(input('Digite o primeiro termo: '))

print('Os 10 primeiros termos são:')

while i < 11:
    i += 1
    print(termo, end=' ')
    termo += razao
    