'''
Crie um programa que leia dois valores e mostre um menu na tela:
[1] somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair do programa

Seu programa deverá realizar a operação solicitada em cada caso.
'''
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
somar = n1 + n2
multiplicar = n1 * n2
opcoes = '1234'
escolha = ''

while escolha in opcoes:

    print('Escolha uma das opções:\n[1] Somar\n[2] multiplicar\n[3] maior\n[4]novos números\n[5]Sair do programa')
    
    escolha = str(input(''))

    if escolha == '1':
        print(f'A soma dos números: {n1} + {n2} é igual a {n1+n2}')

    elif escolha == '2':
        print(f'A multiplicação dos números {n1} e {n2} é igual a {n1 * n2}')

    elif escolha == '3':

        if n1 > n2:
            print(f'O número {n1} é maior')

        else: 
            print(f'o número {n2} é maior')

    elif escolha == '4':
        n1 = int(input('Digite o primeiro número: '))
        n2 = int(input('Digite o segundo número: '))
        escolha = str(input('Escolha uma das opções:\n[1] Somar\n[2] multiplicar\n[3] maior\n[4] novos números\n[5]Sair do programa'))

    else:
        print('Saindo do programa...')
