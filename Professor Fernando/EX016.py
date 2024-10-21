'''
 Exemplo 3 Impressão de indices de uma lista durante 5 vezes em um print
'''

produtos = ['Coca-cola', 'Pepsi', 'Itubaina', 'Fanta']

#Otd. de itens na lista

producao = [ 15000, 12000, 13000, 5000 ]

#Otd. de produtos da lista

'''
Dica! Verifica o tamanho da lista, caso os produtos aumenten ou diminuam, utilizando
 o método ja utilizando em exercicios anteriores => len
'''

qtd = len(produtos)

for indices in range(qtd):
    print('O produto: {} -> foi fabricado: {} unidades em 06/2023'.format(produtos[indices],producao[indices]))

#Fim do código