#Crie um programa que faça o computador jogar jokenpô com você
import random
print('x1 de pedra papel tesoura?')
jogador= input('Escolha sua jogada!\n').upper().strip()
computador = random.choice(['PEDRA', 'PAPEL', 'TESOURA'])

if jogador == computador:
    print('Empate!')
elif (jogador == 'PEDRA' and computador == 'TESOURA') or (jogador == 'TESOURA' and computador == 'PAPEL') or (jogador == 'PAPEL' and computador == 'PEDRA') :
    print(f'Você ganhou! eu escolhi {computador}')
else:
    print(f'Você perdeu! eu escolhi {computador}')

'''
import random

print('Vamos jogar Pedra, Papel, Tesoura!')
print('Escolha sua jogada:\n- PEDRA\n- PAPEL\n- TESOURA')
jogador = input('Sua jogada: ').upper().strip()

# Escolha aleatória do computador
computador = random.choice(['PEDRA', 'PAPEL', 'TESOURA'])

# Verificando se o jogador fez uma escolha válida
if jogador not in ['PEDRA', 'PAPEL', 'TESOURA']:
    print('Jogada inválida! Escolha entre PEDRA, PAPEL ou TESOURA.')
else:
    print(f'Computador escolheu: {computador}')

    # Verificando o resultado do jogo
    if jogador == computador:
        print('Empate!')
    elif (jogador == 'PEDRA' and computador == 'TESOURA') or \
         (jogador == 'TESOURA' and computador == 'PAPEL') or \
         (jogador == 'PAPEL' and computador == 'PEDRA'):
        print('Você ganhou!')
    else:
        print('Você perdeu!')

'''