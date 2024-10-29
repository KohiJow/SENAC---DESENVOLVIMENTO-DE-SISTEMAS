msg0 = 'O indice do produto é:'
msg1 = 'O item da lista é o:'
msg3 = 'e quantidade do produto é:'

produtos = ['Celular', 'Computador', 'Monitor', 'Placa de Vídeo', 'Processador']
estoque = [100, 200, 300, 400, 1000]

i = produtos.index('Processador')
print('\n' + msg0,i,msg1,produtos[i],msg3,estoque[i])
