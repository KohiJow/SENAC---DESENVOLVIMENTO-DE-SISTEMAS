'''
Crie um programa que tenha uma tupla unica com nomes de produtos e seus respectivos 
precos. na sequencia.
No final, mostre uma listagem de precos, organizando os dados em forma tabular.
'''

tupla_unica = 'Pizza Portuguesa', 60.00, 
'Lanche', 120.00, 
'Suco', 15.00, 
'Agua', 2.00

lista_comida = tupla_unica[0::2]
lista_precos = tupla_unica[1::2]


print('-'*40)
print(f"{'PRODUTO':<25}{'PRECO(R$S)':>10}")
print('-'*40)

for produto, preco in zip(lista_comida,lista_precos):
    print(f'{produto:25} R${preco:>7.2f}')
