#estoque 1 - Dicionários no Python

estoque = {}

def adicionar_produtos(nome, quantidade, preco):
    if nome in estoque:
       estoque[nome]['quantidade'] += quantidade
    else:
        estoque[nome] = {'quantidade': quantidade, 'preco': preco}

def remover_produto(nome):
    if nome in estoque:
        del estoque[nome]

def exibir_estoque():
    for produto, dados in estoque.items():
        preco_formatado = f"R$ {dados['preco']:.2f}".replace(',', 'X').replace(',',',').replace('X', '.')
        print(f"Produto: {produto}, Quantidade: {dados['quantidade']}, Preço: {preco_formatado}")

#Teste

adicionar_produtos('Cadeira', 10, 120.00)
adicionar_produtos('Mesa', 5, 300.00)
adicionar_produtos('Cadeira', 2, 120.00) #Atualiza a quantidade
remover_produto('Mesa')
exibir_estoque()