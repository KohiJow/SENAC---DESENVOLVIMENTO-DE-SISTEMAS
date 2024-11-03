#-
'''Reduão de Listas com reduce()
A função reduce() da biblioteca functools pode ser usada para reduzir uma lista a um único valor, aplicando uma 
função de forma cumulativa.
'''
'''
O que é o lambda?
E uma expressão que cria uma função de forma concisa.
Uma função lambda pode ter qualquer número de parametros, mas apenas uma expressão.
Ela retorna automaticamente o resultado da expressão sem precisar de um return explicito.
'''

linha = '-------------------------------------------------------------------------------'

from functools import reduce

# Somando todos os numeros de uma lista
numeros = [1, 2, 3, 4, 5]
soma_total = reduce(lambda x, y: x + y, numeros)
print('\n' + linha + '\n')
print(' O valor total da soma da lista é:',soma_total) # Saida: 15
print('\n' + linha + '\n')
