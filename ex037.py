'''
Escreva um programa que leia um número inteiro qualquer e peça para o usuário
escolher qual será a base de conversão:
-1 para binário
-2 para octal
-3 para hexadecimal
'''
num = int(input('Digite um número inteiro:'))
 
input('Escolha uma das bases para conversão\nA) Binário\nB) Octal\nC) Hexadecimal\n R:').strip().upper()
 
if input == 'A':
   print(f'{num} em binário é {bin(num)}')
elif input == 'B':
   print(f'{num} em octal é {oct(num)}')
elif input == 'C':
    print(f'{num} em hexadecimal é {hex(num)}')
else:
    print('Digite uma opção válida')