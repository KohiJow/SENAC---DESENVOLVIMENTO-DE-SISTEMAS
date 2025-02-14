'''
Desenvolva um programa que leia quatro valores pelo teclado e guarde-os 
em uma tupla. No final, mostre:
A)Quantas vezes apareceu o valor 9.
B) Em que posicao foi digitado o primeiro valor 3.
C) Quais foram os numeros pares.
'''
numeros_pares= 0

num= tuple(int(input('Insira um numero: ')) for _ in range(4))

print(f'Vc digitou os valores{num}')
print(f'O valor 9 apareceu: {num.count(9)} vezes')

if 3 in num:
    print(f'O valor 3 apareceu na posicao: {num.index(3)+1}')
else:
    print('O valor 3 nao foi digitado')

print('os numeros pares foram:')
for n in num:
    if n % 2 == 0:
        print(f"{n}", end= " ")
        