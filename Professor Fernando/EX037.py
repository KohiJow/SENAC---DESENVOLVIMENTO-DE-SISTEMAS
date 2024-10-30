#Exemplo 2 - Verificação e indice de uma lista com condições
produto = input('\n' + 'Insira o nome de um equipamento eletrônico: ')
produtos = ['Celular', 'Computador', 'Monitor', 'Placa de Vídeo', 'Processador']
estoque = [100,         200,          300,      400,                1000]

#verificação automática de produtos na lista

if produto in produtos:
    i = produtos.index(produto)
    qtd_estoque = estoque[i]
    print('\n' + f'A quantidade do produto: {produto} em estoque é de {qtd_estoque} unidades.')
else:
    print('\n' + f'--ATENÇÃO-- o produto {produto} Não existe no estoque :-(')
    #fim
