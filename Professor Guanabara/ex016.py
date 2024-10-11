# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção inteira.
# EX: Digite um número: 6.127 "O número 6.127 tem a parte inteira 6."
# Create a program that reads a real number and shows its integer part
# EX: Enter a number: 6.127 "The number 6.127 has the integer part 6."

# Number = float(input('Enter a real number, and I will show you its nearest integer: '))
# nearest_integer = round(Number)
# print(f'The real number is {Number} and its nearest integer is: {nearest_integer}')

from math import trunc  # removes decimal places from a number

num = float(input('Digite um valor: '))
print(f'O valor digitado foi {num} e a sua porção inteira é {trunc(num)}')

# num = float(input('Digite um valor: '))
# print(f'O valor digitado foi {num} e sua porção inteira é {int(num)}')
