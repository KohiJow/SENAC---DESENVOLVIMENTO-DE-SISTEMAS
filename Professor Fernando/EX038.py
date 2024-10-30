'''
Adicionar = lista.append(item)
Remover = lista.pop(indice)
ou
lista.remove(item)

Exemplo 1º: Trocando um item na lista (MOTO G7 para MOTO G8)

'''
#Trocando
'''
trocar_mobile = ['MOTO G5', 'MOTO G6', 'MOTO G7']
print('\n' + 'Os modelos da lista atual, são:', trocar_mobile, '\n')
trocar_mobile[2] = 'Moto G8'
print('O celular MOTO G7 foi trocado pelo modelo', trocar_mobile[2])
print('\n' + 'Lista de produtos atualizada é:', trocar_mobile)
'''
#Adicionando
'''
adiciona_mobile = ['MOTO G6', 'MOTO G7', 'MOTO G8']
print('\n' + 'Os modelos da lista atual, são:', adiciona_mobile, '\n')
adiciona_mobile.append('MOTO G9')
print('O celular', adiciona_mobile[3], 'foi adicionado no estoque com sucesso')
print('\n' + 'A lista de produtos atualizada é:', adiciona_mobile)
'''
#Removendo com remove, pop e if else
'''
r0_mobile = ['MOTO G6', 'MOTO G7', 'MOTO G8']
print('\n' + 'Os modelos da lista atual, são:',r0_mobile,'\n')
r0_mobile.remove('MOTO G8')
print('O celular MOTO G8 foi removido no estoque com sucesso.')
print('\n' + 'A lista de produtos atualizada é:', r0_mobile)
'''
'''
r1_mobile = ['MOTO G6', 'MOTO G7', 'MOTO G8']
print('\n' + 'Os modelos da lista atual, são:',r1_mobile,'\n')
item_removido = r1_mobile.pop(2)
print(f'O celular do modelo: {item_removido} foi removido do estoque.')
print('\n' + 'A lista de produtos atualizada é:', r1_mobile)
'''

r1_mobile = ['MOTO G6', 'MOTO G7', 'MOTO G8']
item_removido = [2]

if r1_mobile in item_removido:
    r1_mobile.remove('MOTO G9')
else:
    print('\n' + 'O produto MOTO G9, não consta no estoque.')

print('\n' + 'Os modelos da lista atual, são:', r1_mobile, '\n')
