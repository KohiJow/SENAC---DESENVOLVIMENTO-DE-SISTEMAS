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