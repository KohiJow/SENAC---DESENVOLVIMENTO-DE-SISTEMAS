'''Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.'''
num = int(input('Insira um número inteiro e direi se ele é ou não um número primo: '))
numsqrt = round(num ** 0.5) #calcula a raiz quadrada

verif = 0 

for i in range(2,numsqrt+1): #loop que vai de 2 até a raiz quadrada do número inserido
    if num % i != 0:
        print(f'O número {num} não é divisivel por {i}') 

    else: #conclui que o número não é primo adicionando o valor na variavel verificavel
        print(f'O número {num} é divisivel por {i}')
        verif = 1

if verif == 0:
    print('Ele é primo')
else:
    print("Ele não é primo")

"""
Correção 
num = int(input('Insira um número inteiro e direi se ele é ou não um número primo: '))
numsqrt = int(num ** 0.5)  # Calcular a raiz quadrada e transformar em inteiro

if num < 2:  # Números menores que 2 não são primos
    print(f'O número {num} não é primo.')

else:
    verif = 0  # Indicador de divisibilidade

    for i in range(2, numsqrt + 1):
        if num % i == 0:  # Se o número for divisível por i
            print(f'O número {num} é divisível por {i}')
            verif = 1
            break  # Já podemos parar, pois ele não é primo

    if verif == 0:  # Se nenhuma divisão foi exata
        print(f'O número {num} é primo.')
    else:
        print(f'O número {num} não é primo.')

"""