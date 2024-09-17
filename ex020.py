#O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos.
#Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
from random import shuffle #Da biblioteca random importa o shuffle
#from random import choice
 
n1 = str(input('Primeiro Grupo: '))
n2 = str(input('Segundo Grupo: '))
n3 = str(input('Terceiro Grupo: '))
n4 = str(input('Quarto Grupo: '))
n5 = str(input('Quinto Grupo: '))
n6 = str(input('Sexto Grupo: '))
 
grupos = [n1, n2, n3, n4, n5, n6] #Lista dos grupos onde o usuário coloca os grupos
shuffle(grupos) # Embaralha a lista in-place 
 
# Exibe a ordem dos grupos individualmente
for grupo in grupos:
    print(grupo)
