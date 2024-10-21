vendas = [1300, 200, 300, 400, 500, 1500] # Otd. de itens na lista
meta = 1000

contador = 0 
for maior_venda in vendas: 
    if maior_venda >= meta: # A variável maior venda serve de armazenamento do FOR
     #Isto é um contador que também funciona assim: contador = contador 1 (Incremento) 
     contador += 1

# Verificando a porcentagem de vendedores que bateram a meta de vendas 
qtd_funcionarios = len(vendas)

print('\n' + 'A porcentagem de funcionários que bateram a meta foi de: ')
print('{:.0%}'.format(qtd_funcionarios / contador))

#Fim do código
