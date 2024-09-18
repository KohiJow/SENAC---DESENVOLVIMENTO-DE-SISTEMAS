#Escreva um programa que pergunte o salário de um funcionário e calcule o valor de seu aumento.
#Para salários superiores a R$1250, calcule um aumento de 10%
#Para os inferiores ou iguais, o aumento é de 15%.

salário = float(input('Insira seu salário. \nR: '))

if salário <= 1250:
    aumento = salário / 100 * 15 + salário
    print(f'Seu novo salário é: ${aumento:.2f}') 
else:
    aumento = salário / 100 * 10 + salário
    print(f'Seu novo salário é: ${aumento:.2f}')
