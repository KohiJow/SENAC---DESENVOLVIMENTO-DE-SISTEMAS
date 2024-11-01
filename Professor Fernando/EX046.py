#Verificando tamanho da lista
#Máximo: max = max(var_produtos)

produtos = ['MOTO G6', 'MOTO G7', 'MOTO G8']
vendas =   [100,        200,       300]
prod_ma_v= max(vendas)

p = vendas.index(prod_ma_v)
prod_ma_v = produtos[p]

v = produtos.index(prod_ma_v)
verif_ma_v = vendas[v]

print(f'Quantidade do produto mais vendido foi: {verif_ma_v} unidades da Motorola e o modelo mais vendido foi: {prod_ma_v}')
