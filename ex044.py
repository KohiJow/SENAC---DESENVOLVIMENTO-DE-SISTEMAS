'''
Elabore um programa que calcule o valor a ser pago por um
produto, considerando o seu preço normal e condição de pagamento:
-À vista dinheiro/cheque: 10% de desconto
-À vista no cartão: 5% de desconto
-Em até 2x no cartão: preço normal
-3x ou mais no cartão: 20% de juros
'''

print('Olá seja bem vindo ao caixa!')
valor = float(input('Qual o valor da compra?\n'))
fp = str(input('Qual a forma de pagamento? ')).strip().upper() 
if fp == 'PARCELADO':
    vezes = int(input('Em quantas vezes?\n'))
    if vezes <=2:
        print(f'valor total: {valor}')
    else:
        juros = (valor/100) * 20
        print(f'valor total: {valor+juros}')
    
if fp == 'DINHEIRO' or fp == 'CHEQUE':
    desconto = (valor/100) * 10
    print(f'O valor a ser pago é {valor - desconto}')

elif fp == 'CARTAO' or 'CARTÃO':
    desconto = (valor/100) * 5
    print(f'O valor a ser pago é {valor - desconto}')
else:
    print('Digite uma entrada válida')
    