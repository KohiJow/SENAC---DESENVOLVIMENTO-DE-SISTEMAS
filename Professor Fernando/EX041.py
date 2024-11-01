'''
Exemplo: Programa para fazer uma divisão, porém ao efetuar o cálculo, um erro é gerado e o
tratamento do erro é efetuado pelos métodos: Try e Except
'''
def divisao(x,y):
    try:
        #O valor do cálculo é a divisão INTEIRA de 3 por 0
        resultado = x//y
        print('O resultado da divisão é:', resultado)
    except ZeroDivisionError: #Valor PADRÃO para tratamento de erros de divisão.
        print('Desculpe! mas o  valor não pode ser dividido por ZERO :-(')
        
'''
Os valores da divisão PODEM estar em qualquer parte  da função (def)
assunto que vamos ver nas próximas aulas.
'''
divisao(3, 0)
