'''
Exercício Python 087: Aprimore o desafio anterior, mostrando no final:
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha.
'''

matriz = [[0,0,0], [0,0,0], [0,0,0]]
spar = mai = scol = 0
#laco para para linhas
for l in range(0,3):
    #laco para colunas
    for c in range(0,3):
        #matriz recebe um valor inteiro de um input na linha {l} e coluna {c} 
        # (posicoes definidas com o laco)
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))

print('-='*30)

#laco para a linha dentro da coluna, a diferenca e que esse for 
# mostra a estrutura na tela
for l in range(0,3):
    #o for de baixo
    for c in range(0,3):

        print(f'[{matriz[l][c]:^5}]', end='')
        if matriz[l][c] % 2 == 0:
            spar += matriz[l][c]
            
    #quebra a linha para formatar mais alinhado
    print()
    print(f'A soma dos valores pares {spar}')
for l in range(0,3):
    scol += matriz[l][2]
print(f'A soma dos valores da terceira coluna e {scol}')