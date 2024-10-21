#Exemplo 14 - FOR com sistema de cadastro com range

quartos = [
['Joao', 'CPF: 111111111111'],
['Maria', 'CPF: 222222222222' ],
['Fernando', 'CPF: 333333333333'],
['Silvana', 'CPF: 4444444444444' ],
]
qtd_pessoas = int (input ('Quantas pessoas terao no quarto: ') )
quarto = []

for i in range(qtd_pessoas) :
    nome = input ('Nome do hospede: ')
