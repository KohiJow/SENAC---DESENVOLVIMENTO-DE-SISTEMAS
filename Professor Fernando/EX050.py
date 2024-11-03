'''
1. Gestão de Estoque
Sistema de controle de estoque de papelaria. Cada item no estoque é representado por um nome e sua quantidade disponivel.
Tarefa: Crie uma função que, dada uma lista de itens e suas respectivas quantidades,
retorne os itens que precisam ser repostos (quantidade menor ou igual a 5).
'''
def verificar_estoque(itens):
    # Lista de itens com quantidade menor ou igual a 5
    reposicao = [item for item, quantidade in itens if quantidade <= 5]
    return reposicao

linha = '------------------------------------------------------------------'

# Estudo de caso
estoque = [('Caneta', 10), ('Caderno', 4), ('Borracha', 2), ('Lapis', 8) ]
print('\n' + linha)
print('Os itens que estão em falta no estoque da papelaria são:', verificar_estoque(estoque) )
print(linha + '\n')
# Saída: ['Caderno', 'Borracha']
