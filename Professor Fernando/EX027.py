#Exemplo 19 - FOR com a função break que para o LOOP

vendas = [100,      150,        1500,           2000,           120]
loja = ['Barão Geraldo', 'Iguatemi', 'Centro', 'Cambuí', 'Santa Genebra']
meta = 2100

for lista_vendas in vendas:
    if lista_vendas < meta: # Verifica se a lista vendas é MAIOR que a variável meta
        print('A loja do bairro: ', loja[3] + ', BATEU a meta : -)' )
        break
