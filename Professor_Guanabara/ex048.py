'''Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três e que se
encontram no intervalo de 1 até 500.'''

soma = 0
for i in range(1,501):
    if i % 2 != 0 and i % 3 == 0:
        soma += i
        print(i)
print(f'A soma de todos eles é: {soma}')

'''
Correção guanabara:
soma = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        cont = cont + 1
        soma = soma + c
print(f'A soma de todos os {cont} valores solicitados é {soma}')
'''