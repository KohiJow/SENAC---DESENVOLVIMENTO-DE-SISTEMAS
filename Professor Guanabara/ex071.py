"""
Crie um programa que simule o funcionamento de um caixa eletronico. No inicio pergunte ao usuario qual sera o valor a ser sacado (numero inteiro) e o programa vai informar
quantas celulas de cada valor serao entregues.
#OBS= Considere que o caixa possui cedulás de $50, $20, $10 $1.
"""

# Solicita o valor a ser sacado
valor = int(input('Qual o valor a ser sacado? R$ '))  # O usuário digita o valor a ser retirado, que é convertido para inteiro

# Definindo as cédulas disponíveis (valores que o caixa eletrônico tem)
cedulas = [50, 20, 10, 1]  # Lista contendo os valores das cédulas: 50, 20, 10 e 1 real

# Para armazenar a quantidade de cédulas de cada valor
quantidade = []  # Inicializa uma lista vazia que irá armazenar a quantidade de cédulas de cada valor (50, 20, 10, 1)

# Calculando a quantidade de cédulas para cada valor
for cedula in cedulas:  # Laço que percorre cada valor de cédula (50, 20, 10 e 1)
    quantidade.append(valor // cedula)  # Calcula quantas cédulas do valor atual podem ser retiradas
    valor = valor % cedula  # Atualiza o valor restante após a retirada das cédulas, usando o módulo para o restante

# Exibindo o resultado final
for i, cedula in enumerate(cedulas):  # Laço que percorre a lista de cédulas junto com seus índices
    if quantidade[i] > 0:  # Verifica se foi retirada alguma cédula desse valor (quantidade > 0)
        print(f'{quantidade[i]} cédulas de R${cedula}')  # Exibe a quantidade de cédulas daquele valor
