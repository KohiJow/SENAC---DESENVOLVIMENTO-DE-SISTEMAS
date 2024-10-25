#Exemplo 10 - FOR sendo utilizado para verificação de estoque em uma lista.

qtd_estoque = [30, 40, 50, 1200, 300, 800, 1500, 1900, 2000, 3500, 4500, 4100, 5000]
produtos = ['Coca-cola', 'Fanta', 'IT Guarana', 'Pepsi', 'Agua c/ gas', 'Agua s gas', 'Dolly', 'Velho Barreiro', 'Pinga 51' ]
estoque_minino = 50

# Variavel qtd crida na hora, para armazenar os valores da lista

for lista, qtd in enumerate(qtd_estoque):
    if qtd < estoque_minino:
        print('O produto {} esta abaixo do nivel do estoque, temos apenas {}'.format(produtos[lista],qtd),'unidades. ')
