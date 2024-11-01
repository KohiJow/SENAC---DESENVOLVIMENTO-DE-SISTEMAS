#Verificando tamanho da lista
#Minimo: min = min(var_produtos)

produtos = ['MOTO G6', 'MOTO G7', 'MOTO G8']
vendas =   [100,        200,       300]
prod_me_v=  min(vendas)

p = vendas.index(prod_me_v)
prod_me_v = produtos[p]

v = produtos.index(prod_me_v)
verif_me_v = vendas[v]

print(f'Quantidade do produto menos vendido foi: {verif_me_v} unidades da Motorola e o modelo menos vendido foi: {prod_me_v}')
