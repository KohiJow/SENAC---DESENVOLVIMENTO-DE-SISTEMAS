'''
Escreva um programa que leia dois numeros inteiros e compare-os, mostrando na tela
uma mensagem:
-O primeiro valor é maior
-O segundo valor é maior
-Não existe valor maior, os dois são iguais
'''
print('Digite dois números e irei compará-los')
num = int(input('Primeiro número: '))
num2 = int(input('Segundo número'))

if num > num2:
    print(f'O primeiro valor que é {num} é maior que {num2}')
elif num < num2:
    print(f'O segundo valor que é {num2} é maior que {num}')
elif num == num2:
    print('Os dois valores são iguais!')
else:
    print('Digite um valor válido')
