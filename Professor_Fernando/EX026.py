#Exemplo 18 - FOR dentro de outro FOR com listas distintas

estoque = [
[1000,2000,3000,4000,5000,6000],
[1100,2100,3100,4100,5100,6100],
[1200,2200,3200,4200,5200,6200],
[1300,2300,3300,4300,5300,6300],
[1400,2400,3400,4400,5400,6400],
]

fabricas = ['LexCorp', 'Wayne Enterprise', 'Stark Solutions', 'Siberian Foundation' , 'IDRA Arms' ]
estoque_minimo = 7000

for i, lista in enumerate(estoque) :
# 0 for anterior percorre a primeira lista para verificar os valores da mesma
    for qtd in lista:
        if qtd < estoque_minimo:
            print('As empresas com estoque abaixo de:',estoque_minimo, 'unidades, sao as fabricas:', fabricas[i])
        else:
            print('As empresas com estoque acima de:',estoque_minimo, 'unidades, sao as fabricas: ', fabricas[i])
