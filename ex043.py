'''
Desenvolva uma lógica que leia o peso e a altura de uma pessoa,
calcule seu IMC e mostre seu status de acordo com a tabela abaixo:
-Abaixo de 18.5: Abaixo do peso
-Entre 18.5 e 25: Peso ideal
-25 até 30: Sobrepeso
-30 até 40? Obesidade
-Acima de 40: Obesidade mórbida
'''
print('Por favor insira sua altura e peso: ')
altura = float(input('Altura: '))
peso = float(input('Peso: '))
imc = peso / (altura * altura)

if imc < 18.5:
    print('Você está abaixo do peso')
elif imc > 18.5 and  imc < 25:
    print('Peso Ideal')
elif imc > 20 and  imc < 30:
    print('Sobrepeso')
elif imc > 25 and  imc < 40:
    print('Obesidade')
else:
    print('Obesidade Mórbida.')

#correção
'''
print('Por favor insira sua altura e peso:')
altura = float(input('Altura (em metros): '))
peso = float(input('Peso (em kg): '))

# Cálculo do IMC
imc = peso / (altura ** 2)

# Exibindo o IMC formatado com duas casas decimais
print(f'Seu IMC é {imc:.2f}')

# Classificação do IMC
if imc < 18.5:
    print('Você está abaixo do peso.')
elif 18.5 <= imc < 25:
    print('Você está no peso ideal.')
elif 25 <= imc < 30:
    print('Você está com sobrepeso.')
elif 30 <= imc < 40:
    print('Você está com obesidade.')
else:
    print('Você está com obesidade mórbida.')

'''