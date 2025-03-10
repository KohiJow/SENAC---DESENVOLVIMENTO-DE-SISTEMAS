'''
Exercício Python 086: Crie um programa que declare uma matriz de dimensão 3×3 e preencha com valores lidos pelo teclado. 
No final, mostre a matriz na tela, com a formatação correta.
'''
#Lista com tres listas dentro, dentro de cada lista voce tem 3 valores vazios.
matriz = [[0, 0, 0], [0,0,0], [0,0,0]]
#laco para para linhas
for l in range(0,3):
    #laco para colunas
    for c in range(0,3):
        #matriz recebe um valor inteiro de um input na linha {l} e coluna {c} (posicoes definidas com o laco)
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
    

print('-='*30)
#laco para a linha dentro da coluna, a diferenca e que esse for mostra a estrutura na tela
for l in range(0,3):
    #o for de baixo
    for c in range(0,3):

        print(f'[{matriz[l][c]:^5}]', end='')
    #quebra a linha para formatar mais alinhado
    print()