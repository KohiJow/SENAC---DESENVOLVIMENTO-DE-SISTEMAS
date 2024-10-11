'''
Escreva um programa que leia um número inteiro qualquer e peça para o usuário
escolher qual será a base de conversão:
-1 para binário
-2 para octal
-3 para hexadecimal
'''
num = int(input('Digite um número inteiro:'))
 
escolha = input('Escolha uma das bases para conversão\nA) Binário\nB) Octal\nC) Hexadecimal\n R:').strip().upper()
 
if escolha == 'A':
   print(f'{num} em binário é {bin(num)[2:]}')
elif escolha == 'B':
   print(f'{num} em octal é {oct(num)[2:]}')
elif escolha == 'C':
    print(f'{num} em hexadecimal é {hex(num)[2:]}')
else:
    print('Digite uma opção válida')