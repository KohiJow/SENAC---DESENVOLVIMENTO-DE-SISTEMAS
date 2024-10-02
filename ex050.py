'''Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o'''
soma = 0

for n in range(1,7):
    n = int(input('Insira um número: '))
    if n % 2 == 0:
        soma += n
    
print(f'A soma dos valores pares são {soma}')

'''
Correção
soma = 0

for _ in range(6):  # O "_" é usado quando o índice do loop não é necessário
    n = int(input('Insira um número: '))
    if n % 2 == 0:
        soma += n
    
print(f'A soma dos valores pares é {soma}')

'''
