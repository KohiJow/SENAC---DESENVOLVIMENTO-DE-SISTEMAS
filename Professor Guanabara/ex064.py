'''
Crie um programa que leia varios numeros inteiros pelo teclado.
O programa só vai parar quando o usuário digitar o valor 999, que é a condição
da parada. No final, mostre quantos números foram digitados e qual foi a 
soma entre eles (desconsiderando o flag).
'''
num_add = 0
num = None
print('Digite um número e eu lerei a soma deles até você digitar 999 para parar: ')
while num != 999:
    num = int(input(('')))
    num_add += num
    
print('A soma é : ',num_add - 999)
