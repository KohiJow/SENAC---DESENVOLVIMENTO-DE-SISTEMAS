'''
Crie um programa que vai gerar cinco numeros aleatorios e colocar em uma tupla.
Depois disso, mostre a listagem de numeros gerados e tambem indique o menor e o maior valor 
que estao na tupla.
'''
import random

cinco_random = ([])

for _ in range (5):
    numero_aleatorio = [random.randint(1,100)]
    cinco_random += numero_aleatorio
    

print(cinco_random)
print(min(cinco_random))
print(max(cinco_random))

##correcao 

import random

cinco_random = tuple(random.randint(1, 100) for _ in range(5))  # Gera e armazena diretamente na tupla

print(cinco_random)
print("Menor:", min(cinco_random))
print("Maior:", max(cinco_random))
