'''
Crie um programa que vai ler varios numeros e colocar em uma 
lista.
Depois disso, mostre:

A) Quantos numeros foram digitados.

B) A lista de valores, ordenada de forma decrescente.

C) Se o valor 5 foi digitado e esta ou nao na lista.

'''

lista = []
num_Digitado = 0

while True:
    n = int(input('Digite um numero:'))
    num_Digitado += 1
    continuar= str(input('Deseja continuar?\n'))
    
    if continuar in 'Ss':
        print('-=' * 40)
        lista.append(n)
        
    else:
        lista.append(n)
        break
    
    
if 5 in lista:
        print('O numero 5 foi digitado')
        
lista.sort(reverse= True)
print(lista)