# Exercicio nº 17

produtos = ['PC Desktop', 'Notebook', 'Monitor', 'Placa de video', '55D 480GB', 'HD SATA 1TB' ]
vendas_2019 = [1000,        2000,       3000,       4000,           6000,       3000]
vendas_2020 = [1300,        2150,       3500,       4600,           6700,       3900]

for i, lista_produtos in enumerate(produtos):
    if vendas_2020[i] > vendas_2019[i]: # Verifica crescinento em 2020
        crescimento = (vendas_2020[i] / vendas_2019[i]) - 1
        print('{} vendeu {} unidades em 2019, e em 2020, vendeu {} unidades. Crescimento: {:.0%}'.format(
            lista_produtos, vendas_2019[i], vendas_2020[i], crescimento))
        