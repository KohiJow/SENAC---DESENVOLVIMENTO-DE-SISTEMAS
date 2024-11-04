#Exercicio 1º - Tuplas no Python

#Lista para armazenar os produtos
produtos = []
def adicionar_produto(nome, preco, quantidade):
    produto = (nome, preco, quantidade)
    produtos.append(produto)
    
def exibir_produtos():
    for produto in produtos:
        nome, preco, quantidade = produto
        print(f'Produto: {nome}, Preço: R$ {preco:.2f}, Quantidade: {quantidade}')
        
#Adicionando produtos
adicionar_produto('Cadeira', 120.00, 50)
adicionar_produto('Mesa', 300.00, 20)

#Exibindo produtos cadastrados
exibir_produtos()