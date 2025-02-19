'''
Faca um programa que leia 5 valores e guarde-os em uma lista.

No final, mostre qual foi o maior e o menor valor digitado e as
suas respectivas posicoes na lista.
'''

inventario = []

for i in range(5):
    inventario.append(int(input(f'Guarde na posicao {i} o seu numero: ')))


maior_valor = max(inventario)
menor_valor = min(inventario)

posicoes_maior = [i for i, v in enumerate(inventario) if v == maior_valor]
posicoes_menor = [i for i, v in enumerate(inventario) if v == menor_valor]

print(f'\nO maior valor é {maior_valor} e aparece nas posições: {posicoes_maior}')
print(f'O menor valor é {menor_valor} e aparece nas posições: {posicoes_menor}')
