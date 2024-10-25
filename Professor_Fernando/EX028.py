#Exemplo 22 - While cadastro de produtos

produtos = [
['Maça',5],
['Banana',15],
['Goiaba',25],
['Manga',35],
]
produtos = []

while True:
    produto = input ('Insira o produto: ')
    if not produto:
        break
    qtd = int (input('Qual é a quantidade do produto: '))
    produtos.append([produto, qtd] )
print ('Os produtos e quantidade cadastrados foram: ',produtos)
