print('\n') #--> Função utilizada para "pular" linha no Python
print('O resultado da soma dos valores é de: ', 1 + 1)#--> Exemplo 1º
'''
O interpretador do python "entende" que são números inteiros, por isso 
o python é conhecido por ser uma linguagem do tipo "Dinâmica e Forte",
por conhecer o tipo de dado a ser interpretado.
'''

print('A cidade de campinas fica no estado de:', 'S'+'P') #--> Exemplo 2º

'''
O interpretador do Python NÃO vai somar os dois valores, devido ser duas "Strings", neste
caso o python vai concatenar (juntar), as palavras S e P, retornando: SP
'''
#--Exemplos da classe type, retornando os valores dos tipos de dados:
print('O tipo dado informado é:','1', type(1))
print('O tipo dado informado é:','A', type('A'))
print('O tipo dado informado é:',1.0, type(1.0))
print('O tipo dado informado é:',10 == 9, type(10 == 9))
# Fim do programa
