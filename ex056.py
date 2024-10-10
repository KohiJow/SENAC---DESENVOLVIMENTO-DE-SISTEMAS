'''Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
*A média de idade do grupo
*Qual é o nome do homem mais velho.
*Quantas mulheres têm menos de 20 anos.'''
media_idade=0
maior_idade = 0
for p in range(1,5):
    print(f'--- {p}ª Pessoa ---')
    nome = str(input(f'Qual o nome da {p} pessoa?\n'))
    idade = int(input(f'Qual a idade da {p} pessoa?\n'))
    sexo = str(input(f'Qual o sexo da {p} pessoa? M/F\n')).strip().upper()
    
    
    media_idade += idade
    
    if p == 1:
        maior_idade= p
        nome = p
        
    else:
        if idade > maior_idade:
            maior_idade = idade
            
            
print(f'A média de idade do grupo é de {media_idade//2}')
print(f'O nome do homem mais velho de {maior_idade} é {nome}')
