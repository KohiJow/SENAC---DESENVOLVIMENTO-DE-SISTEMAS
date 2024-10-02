'''Refaça o ex009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for'''
num = int(input('Insira um número e eu te mostrarei sua tabua tabuada: '))
for i in range(0,11):
    if i < 11: #essa linha acabou sendo desnecessária
        print(f'{num} x {i} = {num * i}')

#correção 
''' 
num = int(input('Insira um número e eu te mostrarei sua tabuada: '))
for i in range(0, 11):
    print(f'{num} x {i} = {num * i}')
'''
