'''
Melhore o DESAFIO061, perguntando para o usuário se ele quer mostrar mais 
alguns termos. O programa encerra quando ele disser que quer mostrar 0 termos.
'''

# Solicita ao usuário a razão da progressão aritmética (PA)
razao = int(input('Qual sua razão: '))

# Solicita o primeiro termo da PA
termo = int(input('Digite o primeiro termo: '))

# Inicializa a quantidade de termos a ser exibida com 10, para mostrar os 10 primeiros termos inicialmente
total_termos = 10  

# O loop continua enquanto o usuário não escolher 0 (indicação de que deseja parar)
while total_termos != 0:
    print('Os próximos termos são:')  # Exibe uma mensagem para indicar a sequência
    
    # Loop para mostrar a quantidade atual de termos desejada
    for _ in range(total_termos):
        print(termo, end=' ')  # Exibe o termo atual da PA, mantendo na mesma linha
        termo += razao  # Calcula o próximo termo somando a razão

    print()  # Adiciona uma quebra de linha para separar o próximo grupo de termos
    
    # Pergunta ao usuário quantos termos a mais ele quer ver. Se ele digitar 0, o programa para
    total_termos = int(input('\nQuantos termos você deseja ver a mais? (Digite 0 para encerrar): '))

# Mensagem final indicando que o programa foi encerrado
print("Encerrando o programa.")
