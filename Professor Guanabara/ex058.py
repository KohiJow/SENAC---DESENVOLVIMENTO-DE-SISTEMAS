'''
Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número
entre o 0 e 10. só que agora o jogador vai tentar adivinhar até acertar, 
mostrando no final quantos palpites foram necessários para vencer.
'''

import random 
computador = random.randint(0,10)
user_choice = int(input('Que número estou pensando?\n'))
while computador != user_choice:
    user_choice = int(input('Errou, tente novamente:\n'))

print(f'Parabéns você acertou o número era {computador}')
