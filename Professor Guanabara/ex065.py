'''
 Crie um programa que vários números inteiros pelo teclado. No final da execução, mostre a
 média entre todos os valores e qual foi o maior e o menor valores lidos.
 O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
'''

# Inicializa a variável de resposta com "S", indicando que o programa começa em um estado onde o usuário quer continuar.
resp = "S"

# Inicializa as variáveis para somar os números, contar a quantidade de números, e armazenar os valores de maior, menor e média.
soma = quant = maior = media = menor = 0

# Inicia um loop que continua enquanto o usuário digitar "S" ou "s".
while resp in "Ss":
    # Solicita ao usuário que digite um número inteiro.
    num = int(input("Digite um numero: "))

    # Adiciona o número digitado à variável soma (soma acumulativa).
    soma += num

    # Incrementa o contador de números digitados.
    quant += 1

    # Na primeira iteração, define o número atual como o maior e o menor, já que só há um número.
    if quant == 1:
        maior = menor = num
    else:
        # Caso não seja a primeira iteração, verifica se o número atual é maior que o maior registrado.
        if num > maior:
            maior = num
        # Verifica se o número atual é menor que o menor registrado.
        if num < menor:
            menor = num

    # Pergunta ao usuário se deseja continuar. A entrada é convertida para maiúsculas, retirada de espaços e pega apenas a primeira letra.
    resp = str(input("Quer continuar? S/N")).upper().strip()[0]

# Após sair do loop, calcula a média dos números digitados.
media = soma / quant

# Exibe o total de números digitados e a média calculada.
print(f"Vc digitou {quant} numeros e a media foi {media}")

# Exibe o maior e o menor valor entre os números digitados.
print(f"O maior valor foi {maior} e o menor foi {menor}")
