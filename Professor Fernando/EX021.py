#Exemplo 9 - FOR com o método enumerate

funcionarios = ['João', 'Maria', 'José', 'Fernando', 'Fabio', 'Marisa' ]
for indice, lista_funcionarios in enumerate(funcionarios) :
    print('A ID do funcionario: {} é: {}'.format(funcionarios[indice], indice, lista_funcionarios))