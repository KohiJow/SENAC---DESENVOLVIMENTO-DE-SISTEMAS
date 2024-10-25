'''
Escreva um programa que receba três números e exiba o maior deles, utilizando o "método" max, escreva e execute p código a seguir.
'''

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))

maior = max(num1, num2, num3)

linha= '--------------------------------'

print(linha)
print(f"O maior número é {maior}")
print(linha)
