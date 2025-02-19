'''
Crie um programa onde o usuario possa digitar varios valores numericos e 
cadastre-os em uma lista, caso o numero ja exista la dentro, ele
nao sera adicionado.

No final serao exibidos todos os valores unicos 
digitados em ordem crescente.
'''

lista_de_numeros = []

while True:
    
    n = int(input('Adicione um numero na lista: '))
        
    if n not in lista_de_numeros:
        lista_de_numeros.append(n)
        print('Valor adicionado com sucesso')
    
    else:
        print('Valor duplicado nao vou adicionar')
    
    decide = str(input('Deseja continuar?[S/N]\n').strip())
    
    if decide in "Ss":
        print('Continuando...')

    if decide in "Nn":
        break

lista_de_numeros.sort()

print(f'Os numeros registrados foram {lista_de_numeros}')