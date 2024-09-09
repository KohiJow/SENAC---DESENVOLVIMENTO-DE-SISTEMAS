#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

import math
 
an = float(input('Digite o angulo que vc deseja '))
 
seno = math.sin(math.radians(an))
print(f'O ângulo tem o seno {seno:.2f}')
 
cosseno = math.cos(math.radians(an))
print(f'O ângulo de {an} tem o cosseno de {cosseno:.2f}')
 
tangente = math.tan(math.radians(an))
print(f'O ângulo de {an} tem a tangente de {tangente:.2f}')