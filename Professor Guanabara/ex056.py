'''Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
*A média de idade do grupo
*Qual é o nome do homem mais velho.
*Quantas mulheres têm menos de 20 anos.'''
totmulher20 = 0
soma_idade=0
homemvelho = 0
nomevelho = 0

for p in range(1,5):
    print(f'--- {p}ª Pessoa ---')
    nome = str(input(f'Qual o nome da {p} pessoa?\n'))
    idade = int(input(f'Qual a idade da {p} pessoa?\n'))
    sexo = str(input(f'Qual o sexo da {p} pessoa? M/F\n')).strip().upper()
    
    
    soma_idade += idade
 
    if sexo == 'M' and idade > homemvelho:
        homemvelho = idade
        nomevelho = nome
    
    if sexo == 'F' and idade < 20:
        totmulher20 += 1
        
print(f'A média de idade do grupo é de {soma_idade//2}') #*A média de idade do grupo
print(f'O nome do homem mais velho de {homemvelho} anos é {nomevelho}')
print(f'O total de mulheres com menos de 20 anos é {totmulher20}')
