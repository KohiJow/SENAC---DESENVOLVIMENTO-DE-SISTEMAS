#Fazer um programa de contagem regressiva

#contagem = 10

#while contagem > 0:
#    print(f'Contagem regressiva: {contagem}') 
#    contagem -= 1

#Correção

import time  # Importa o módulo time para usar a função sleep

contagem = 10

while contagem > 0:
    print(f'Contagem regressiva: {contagem}')
    time.sleep(1)  # Espera 1 segundo
    contagem -= 1

print('Contagem regressiva concluída!')
