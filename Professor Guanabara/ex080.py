'''
Crie um programa onde o usuario possa digitar cinco valores
numericos e cadastre-os em uma lista, ja na posicao correta de insercao (sem
usar o sort()).

No final mostre a lista ordenada na tela.
'''

lista=[]

for c in range(0,5):
    n= int(input('Insira um numero: '))
    if c == 0 or n > lista[-1]:
        lista.append(n)
        print('Adicionado ao final da lista')
    else:
        pos = 0 
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos,n)
                print(f'Adicionado na {pos} pos da lista')
                break
            pos+=1
print(f'Os valores digitados foram {lista}')