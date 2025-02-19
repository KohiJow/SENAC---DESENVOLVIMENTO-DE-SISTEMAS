'''
Crie um programa que vai ler varios numeros e colocar em uma lista

Depois disso, crie duas listas extras que vao conter apenas
os valores pares e os valores impares digitados respectivamente.

Ao final, mostre o conteudo das tres listas geradas.
'''
lista_Normal= []
lista_Impar= []
lista_Par= []

while True:
    n= int(input('Digite um numero:\n'))
    if n % 2 != 0:
        lista_Impar.append(n)
        lista_Normal.append(n)
    elif n % 2 == 0:
        lista_Par.append(n)
        lista_Normal.append(n)
    
    decide = str(input('Deseja continuar?\n'))
    if decide not in 'Ss':
        break

print(f'A lista de numeros Impar {lista_Impar}')
print(f'A lista de numeros Par {lista_Par}')
print(f'A lista de numeros Geral {lista_Normal}')

