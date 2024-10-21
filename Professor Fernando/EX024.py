#Exemplo 16 - FOR (Sistema de verificação de meta de vendas)

meta = 10000
valor_vendas = [
['Joao Paulo', 15000],
['Pedro Silva', 14000],
['Julio Matos', 16000],
['Ronaldo Silveira', 9000],
]
print ('O valor da meta do mês de julho é de R$',meta, '\n')
for item in valor_vendas:
    if item[1] > meta:
        print('Vendedor {} BATEU a meta, com o valor de vendas de R$ {}'. format(item[0] ,item[1] ) )
    else:
        print('\n' + 'Vendedor {} "NAO" bateu a meta, com o valor de vendas de R$ {}'.format(item[0], item[1] ))
