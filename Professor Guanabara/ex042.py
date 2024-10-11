'''
Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
-Equilátero: todos os lados iguais
-Isósceles: dois lados iguais
-Escaleno: todos os lados diferentes
'''
print('Insira o tamanho dos lados e eu direi se eles conseguem\nformar um triângulo ou não e qual tipo de triângulo será formado:\n')

A = float(input('Insira o lado A: '))
B = float(input('Insira o lado B: '))
C = float(input('Insira o lado C: '))

if A + B > C and A + C > B and B + C > A:
    print('Os lados formam um triângulo!')

    if A == B == C:
        print('Triângulo Equilátero: todos os lados são iguais.')
    elif A == B or A == C or B == C:
        print('Triângulo Isósceles: dois lados são iguais.')
    else:
        print('Triângulo Escaleno: todos os lados são diferentes.')
else:
    print('Os lados NÃO formam um triângulo.')
