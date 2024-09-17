#Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
print('Insira 3 números e eu te mostrarei o menor e o maior:')
try:
    num1 = int(input('Primero: '))
    num2 = int(input('Segundo: '))
    num3 = int(input('Terceiro: '))
    maior = max(num1,num2,num3)
    menor = min(num1,num2,num3)

    print(f'O maior {maior}')
    print(f'O menor {menor}')
except ValueError: 
    print('Insira um valor numérico!')