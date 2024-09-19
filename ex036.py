'''
Escreva um programa para aprovar o empréstimo bancário para a compra
de uma casa. O programa vai perguntar o valor da casa. o salário do comprador
e em quantos anos ele vai pagar.
Calcule o valor da prestação mensal, sabendo que ela não pode exceder
30% do salário ou então o empréstimo será negado.
'''
casa = float(input('Qual o valor da casa?\n'))
salário = float(input('Qual seu salário?\n'))
anos = int(input('Em quantos anos pretende pagar?\n'))
prestação = casa / (anos * 12)

if prestação > (salário / 100 * 30):
    print('Empréstimo negado')

else:
    print(f'o valor da casa é de ${casa:.2f} e a prestação ficaria em ${prestação:.2f} durante ${anos} anos')
