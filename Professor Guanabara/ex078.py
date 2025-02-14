'''
Faca um programa que leia 5 valores e guarde-os em uma lista.

No final, mostre qual foi o maior e o menor valor digitado e as
suas respectivas posicoes na lista.
'''

inventario = []

for i in range(5):
    item = int(input('Guarde 5 itens no seu inventario! \n R: '))
    inventario.append(item)
    
print(f'Na posicao {i} foi encontrado o maior valor: ', max(inventario))
print(f'Na posicao {i} foi encontrado o menor valor: ', min(inventario))
