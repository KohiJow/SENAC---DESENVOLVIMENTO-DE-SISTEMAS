'''
Exercício Python 088: Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 
para cada jogo, cadastrando tudo em uma lista composta.
'''
from random import randint
games= int(input('Insert the number of games are generated: '))
jogos = []
for num in range(games):
    for games in range(1,7):
        six_Games= [randint(0,60) in range(0,6)]
        jogos.append(six_Games)
print(jogos)