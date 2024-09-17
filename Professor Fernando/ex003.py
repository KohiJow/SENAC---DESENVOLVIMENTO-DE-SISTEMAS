#Fazer um programa de contagem regressiva

#contagem = 10

#while contagem > 0:
<<<<<<< HEAD
    #print(f'Contagem regressiva: {contagem}') 
    #contagem -= 1

# correção 
=======
#    print(f'Contagem regressiva: {contagem}') 
#    contagem -= 1

#Correção
>>>>>>> 6eb3820ef0cdb8ad4c768cd220f942108e6b8344

import time  # Importa o módulo time para usar a função sleep

contagem = 10

while contagem > 0:
    print(f'Contagem regressiva: {contagem}')
    time.sleep(1)  # Espera 1 segundo
    contagem -= 1

print('Contagem regressiva concluída!')
