vendas = [1300, 200, 300, 400, 500, 600, 700, 800, 900, 1500] # Qtd. de itens na lista 
meta = 1000

contador = 0

for maior_venda in vendas: # A variável maior venda serve de armazenamento do FOR 
    if maior_venda >= meta: # Verifica se é MAIOR ou IGUAL ao valor da variável meta
    #Isto é um contador que também funciona assim: contador contador + 1 (Incremento)
     contador += 1

print('\n' + 'Quantidade de vendedores que bateram a meta de vendas, foi de:','\n')
print('Apenas', contador, 'vendedores bateram a meta de vendas de Julho de 2023.')

# Fim do código