'''Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e menor peso lidos.'''
maior = 0
menor = 0

for p in range(1,6):
    peso = float(input(f'Peso da pessoa {p}: '))
if p == 1:
    maior = p
    menor = p
else:
    if peso > maior:
        maior = peso 
    if peso < menor:
        menor = peso
print(f'O maior peso lido foi de {maior}Kg')
print(f'O menor peso foi de {menor}')
    