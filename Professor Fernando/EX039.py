#Exemplos de uma lista com índices POSITIVOS e NEGATIVOS

#Lista com elementos de 'a' a 'j'
lista = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
'''
#Alterando os caracteres para CAIXA ALTA com o método CAPITALIZE
conversor_texto = [letra.capitalize() for letra in lista]
'''

#Alterando os caracteres para CAIXA BAIXA com o método LOWER
conversor_texto = [letra.lower() for letra in lista]
    
#Exibindo os índices positivos e os valores correspondentes
    
'''
print('Indíces positivo:')
for i in range(len(lista)):
    print(f'Indice {i}: {lista[i]}')
    
#Exibindo os índices negativos e os valores correspondentes
print('\nIndices Negativos:')
for i in range(-1,-len(lista)-1,-1):
    print(f'Indice {i}: {lista[i]}')
'''    

# CAIXA ALTA desta vez
'''
print('Indíces positivo:')
for i in range(len(conversor_texto)):
    print(f'Indice {i}: {conversor_texto[i]}')
    

print('\nIndices Negativos:')
for i in range(-1,-len(conversor_texto)-1,-1):
    print(f'Indice {i}: {conversor_texto[i]}')
'''

#CAIXA BAIXA desta vez
print('Indíces positivo:')
for i in range(len(conversor_texto)):
    print(f'Indice {i}: {conversor_texto[i]}')
    

print('\nIndices Negativos:')
for i in range(-1,-len(conversor_texto)-1,-1):
    print(f'Indice {i}: {conversor_texto[i]}')