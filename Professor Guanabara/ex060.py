'''
Faça um programa que leia um número qualquer e mostre seu fatorial.

Ex:
5! = 5x4x3x2x1= 120

'''
num = int(input('Insira um número e eu direi seu fatorial:\n!'))
cont = num
fatorial = 1
while cont > 0:
    fatorial *= cont
    cont -= 1
print(f'Seu fatorial de {num}! é {fatorial}')
