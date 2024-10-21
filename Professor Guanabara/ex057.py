'''
Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores M ou F
Caso esteja errado, peça a digitação novamente até ter um valor correto.
'''

nome = str(input('Digite seu sexo: (M/F)')).upper().strip()

while nome != "M" or "F":
    print('Digite um gênero válido')
    nome = str(input('Digite seu sexo: (M/F)')).upper().strip()
print('Programa encerrado')  
