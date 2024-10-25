#Desenvolva um programa que leia o comprimento de três retas e vai dizer se ele pode ou não formar um triângulo.
print('Insira o tamanho das linhas e eu direi se elas conseguem\nformar um triângulo ou não:\n')

A = float(input('Insira a linha A: '))
B = float(input('Insira a linha B: '))
C = float(input('Insira a linha C: '))

if A + B > C and A + C > B and B + C > A:
    print('Formam um triângulo')
else:
    print('Não formam um triângulo')