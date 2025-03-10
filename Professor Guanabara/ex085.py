'''
Exercício Python 085: Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que 
mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.
'''
num = [ [], [] ] #duas listas em 1 lista
valor = 0
for c in range(1,8):
    #recebe o valor
    valor = int(input(f'Digite o {c}o. valor: '))
    #verifica se e par
    if valor % 2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)
        
print('-='*30)

#organiza a primeira e segunda lista (0 e 1)
num[0].sort()
num[1].sort()

#Printa a primeira e segunda lista em ordem
print(f'Os valores pares digitados foram: {num[0]}')
print(f'Os valores impares digitados foram {num[1]}: ')