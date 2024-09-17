#Crie um programa que leia um número na tela e diga se é par ou impar. 

num = int(input('Insira um número e eu direi se é par ou ímpar: '))

if num % 2 != 0:
    print('Seu número é impar')
else:
    print('Seu número é par')