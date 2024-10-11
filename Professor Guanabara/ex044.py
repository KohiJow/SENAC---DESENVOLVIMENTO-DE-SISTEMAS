'''
Elabore um programa que calcule o valor a ser pago por um
produto, considerando o seu preço normal e condição de pagamento:
-À vista dinheiro/cheque: 10% de desconto
-À vista no cartão: 5% de desconto
-Em até 2x no cartão: preço normal
-3x ou mais no cartão: 20% de juros
'''
#minha solução
print('Olá seja bem vindo ao caixa!')
valor = float(input('Qual o valor da compra?\n'))
fp = str(input('Qual a forma de pagamento? ')).strip().upper() 

if fp == 'DINHEIRO' or fp == 'CHEQUE':
    desconto = (valor/100) * 10
    print(f'O valor a ser pago é {valor - desconto}')
elif fp == 'CARTAO' or fp == 'CARTÃO':
    desconto = (valor/100) * 5
    juros = (valor/100) * 20
    vezes = int(input('Em quantas vezes?\n'))
    if vezes ==1:
        print(f'valor total: {valor - desconto}')
    elif vezes ==2:
        print(f'valor total: {valor} em {vezes} vezes de {valor/vezes}')
    elif vezes >=3:
        print(f'valor total: {valor+juros}')
    else:
        print('Número de parcelas inválido. Deve ser no mínimo 1.')    
else:
    print('Digite uma entrada válida')

''' Recomendação de melhora do chat gpt
print('Olá, seja bem-vindo ao caixa!')
valor = float(input('Qual o valor da compra?\n'))
fp = str(input('Qual a forma de pagamento? ')).strip().upper() 

if fp in ['DINHEIRO', 'CHEQUE']:
    desconto = valor * 0.10  # 10% de desconto
    print(f'O valor a ser pago é R${valor - desconto:.2f}')
elif fp in ['CARTAO', 'CARTÃO']:
    desconto = valor * 0.05  # 5% de desconto
    juros = valor * 0.20  # 20% de juros para parcelamento acima de 2 vezes
    vezes = int(input('Em quantas vezes?\n'))
    
    if vezes == 1:
        print(f'Valor total com desconto: R${valor - desconto:.2f}')
    elif vezes == 2:
        print(f'Valor total sem desconto ou juros: R${valor:.2f}')
    elif vezes >= 3:
        print(f'Valor total com juros: R${valor + juros:.2f}')
    else:
        print('Número de parcelas inválido. Deve ser no mínimo 1.')
else:
    print('Forma de pagamento inválida. Tente novamente.')

'''