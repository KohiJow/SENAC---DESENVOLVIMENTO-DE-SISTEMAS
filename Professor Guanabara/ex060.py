'''
Faça um programa que leia um número qualquer e mostre seu fatorial.

Ex:
5! = 5x4x3x2x1= 120

'''
""" 
#Solucao simples
from math import factorial
n = int(input("Digite um número para calcular seu Fatorial: "))
f= factorial(n)
print(f"O fatorial de {n} é {f}.")
"""
n = int(input("Digite um número para calcular seu Fatorial: "))
c = n
f = 1
print(f"Calculando {n}!", end="")
while c> 0:
    print(f"{c} ",end="")
    print(" x " if c> 1 else " = ", end="")
    f *= c
    c -= 1
print(f"{f}")
