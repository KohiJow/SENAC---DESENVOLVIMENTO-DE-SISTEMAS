'''
Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
-Equilátero: todos os lados iguais
-Isósceles: dois lados iguais
-Escaleno: todos os lados diferentes
'''
print('Insira o tamanho das linhas e eu direi se elas conseguem\nformar um triângulo ou não:\n')

A = float(input('Insira a linha A: '))
B = float(input('Insira a linha B: '))
C = float(input('Insira a linha C: '))

if A + B > C and A + C > B and B + C > A:
    print('Formam um Triângulo')
if (A == B and A == C) or (B == A and B == C) or (C==A or C==B):
    print('Triângulo Equilátero')
elif (A == B and A == C and A!= C or B) or (B == A and B == C and B != A or C) or (C==A or C==B and C != A or B):
    print('Triângulo Isósceles')
elif (A != B and A != C):
    print('Triângulo Escaleno')
else:
    print('Não formam um triângulo')
    