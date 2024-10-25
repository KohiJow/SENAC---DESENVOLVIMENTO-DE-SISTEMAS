#''Calculadora utilizando While, Funcao (def), IF, Try, Except e Continue'''

# Função para efetuar a soma de dois valores.
def adicao(x, y):
    return x + y

# Função para efetuar a subtração de dois valores.
def subtracao(x, y):
    return x - y

# Função para efetuar a multiplicação de dois valores.
def multiplicacao(x, y):
    return x * y

# Função para efetuar a divisão de dois valores.
def divisao(x, y):
    return x // y

lo = '------------------------------------------'
print(lo + '\n' + 'Selecione UMA das operações:' + '\n')
print('1 - Adição' )
print('2 - Subtração' )
print('3 - Multiplicação' )
print('4 - Divisão')
print(lo + '\n')

while True:
# Verifica se o INPUT é verdadeiro ou falso
    calculo = input("Insira uma das opções: 1 2 3 ou 4: ")

    # Opções pald escolha do usuário:
    if calculo in ('1', '2', '3', '4'):
        try:
            num1 = int(input('Insira o primeiro número: ') )
            num2 = int(input('insira o segundo número: ') )
        except ValueError:
            print('\n' + ' -- 0 valor inserido é INVÁLIDO -- ' + '\n')
            continue

        if calculo == '1':
            print (num1, '+', num2,' => O resultado do cálculo é:',adicao(num1, num2) )

        elif calculo == '2':
            print(num1, '-', num2,' => O resultado do cálculo é:', subtracao(num1, num2))

        elif calculo == '3':
            print(num1, '*', num2,' => O resultado do cálculo é:', multiplicacao(num1, num2))

        elif calculo == '4':
            print (num1, '//', num2,' => O resultado do cálculo é: ', divisao(num1, num2) )

    # Interrompe o loop do while se a resposta for não
        novo_calculo = input('Deseja efetuar mais algum cálculo? (sim/não): ')
        if novo_calculo == 'não':
         break
    else:
        print('\n' + '| -- ERRO -- | -- Opção INVÁLIDA -- ' + '\n')
        