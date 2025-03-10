'''\\
    Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
    A) Quantas pessoas foram cadastradas. 
    B) Uma listagem com as pessoas mais pesadas.
    C) Uma listagem com as pessoas mais leves.
'''
#Cria uma lista temp ~temporaria~
temp= []
#Cria a lista principal 
princ = []

#Maior e menor comecam com 0
mai = men= 0

#Loop infinito
while True:
    temp.append(str(input("Nome: ")))
    
    temp.append(float(input('Peso: ')))
    #Verifica se eu coloquei alguma pessoa cadastrada
    if len(princ) == 0:
        #O temp[0] seria o nome (posicao) e o temp[1] seria o peso
        #Maior e menor seriam igual a temp[1] caso nao tivesse nada
        mai = men = temp[1]
    else: #se nao for igual verifica se o temp 1 e maior que mai e recebe o valor, se for menor, recebe o valor tbm no men.
        if temp[1] > mai:
            mai = temp[1]
        if temp[1] < men:
            men = temp[1]
    
    princ.append(temp[:]) #Para criar uma copia e nao uma conexao, deve-se colocar "[:]", assim adicionamos na lista principal.
    
    #Isso limpa a lista temporaria depois de adiciona-la a principal para que nao printe coisas repetidas
    temp.clear()
    
    resp = str(input('Quer continuar? [S/N] '))
    
    
    if resp in "Nn":
        break
print('-='*30)
print(f"Ao todo, voce cadastrou {len(princ)} pessoas")
print(f'O maior peso foi de {mai}kg. Peso de ', end='')

#verificador se o maior peso for igual ao p[1]
for p in princ:
    if p[1] == mai:
        print(f'[{p[0]}]', end='')
print()

print(f'O menor peso foi de {men} kg. Peso de ', end='')
for p in princ:
    if p[1] == men:
        print(f'[{p[0]}]', end='')