#Verificando tamanho da lista

#Máximo: max = (var_produtos)
#Mínimo: min = (var_produtos)

mobile = ['MOTO G6', 'MOTO G7', 'MOTO G8']
qtd =    [100,        200,       300]
# Indices ->0           1        2
prod_ma_v = max(mobile)
prod_me_v = min(mobile)

#print('\n' + f'O produto mais vendido foi: {prod_ma_v} e o produto que menos vendeu: {prod_me_v}')
print('\n' + f'O produto MAIS vendido foi o modelo: {prod_ma_v}, atingindo a marca de: {qtd[2]} unidades VENDIDAS.')
print('\n' + f'O produto MENOS vendido foi o modelo: {prod_me_v}, atingindo a marca de: {qtd[0]} unidades VENDIDAS.')
print('\n')
