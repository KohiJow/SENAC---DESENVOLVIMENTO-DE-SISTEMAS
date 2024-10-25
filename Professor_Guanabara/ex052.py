'''Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.'''
#incorreto
num = int(input('Digite um número: '))
count = 0


for i in range(1,11): #o range não é suficiente para determinar se era numero primo mesmo
    if num % i == 0:
        print(f'\033[1;32;40m{i}\033[m', end=' ')
        count += 1
    else:
        print(f'\033[1;31;40m{i}\033[m', end=' ')
        
if count == 2:
    print(f'O número {num} foi dividido {count} vezes e por isso ele é primo')

else:
    print(f'O número {num} foi dividido {count} vezes e por isso ele não é primo') 

#correção
'''
num = int(input('Digite um número: '))
count = 0

# Vamos verificar até o próprio número, já que estamos contando divisores
for i in range(1, num + 1):
    if num % i == 0:
        print(f'\033[1;32;40m{i}\033[m', end=' ')  # Verde para divisores
        count += 1
    else:
        print(f'\033[1;31;40m{i}\033[m', end=' ')  # Vermelho para não divisores
        
print()  # Para quebrar a linha após a lista de divisores

# Verificando se o número é primo com base na quantidade de divisores
if count == 2:
    print(f'O número {num} foi dividido {count} vezes e por isso ele é primo.')
else:
    print(f'O número {num} foi dividido {count} vezes e por isso ele não é primo.')
'''
