"""
Crie um programa que leia o nome e o preco de varios produtos. O programa devera perguntar se o usuario vai continuar.#No final, mostre:
#A)Qual e o total gasto na compra
#B)Quantos produtos custam mais de R$1000
#C)Qual e o nome do produto mais barato.
"""

total_gasto = 0
mais_1000 = 0
barato = float('inf')  # Define o preço mais baixo como infinito inicialmente.
nome_barato = ''

while True:
    produto = str(input('Insira o nome do produto: '))
    preco = float(input('Insira o preço do produto: R$ '))
    total_gasto += preco

    if preco >= 1000:
        mais_1000 += 1
    
    # Verifica se é o produto mais barato
    if preco < barato:
        barato = preco
        nome_barato = produto

    continuar = str(input('Deseja continuar? (sim/não): ')).strip().lower()
    if continuar != 'sim':
        break

# Exibe os resultados
print(f'Total gasto na compra: R$ {total_gasto:.2f}')
print(f'Produtos que custam mais de R$1000: {mais_1000}')
print(f'O produto mais barato foi: {nome_barato}, que custa R$ {barato:.2f}')
