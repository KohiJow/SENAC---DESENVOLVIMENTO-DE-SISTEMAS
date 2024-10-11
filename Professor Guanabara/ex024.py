#Create a program that reads the name of a city and tells if it starts with "Santo" or not
#Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "Santo".


#cidade = 'Santo'
#cidade_usuario= str(input('Onde você Nasceu? '))
#cM = cidade_usuario.upper()
#cN = cidade_usuario.lower()
#print('Começa com santo: ', cidade in cidade_usuario)
#print('Começa com Santo: ', cM in cidade_usuario)
#print('Começa com Santo: ', cN in cidade_usuario)

#Correção

cid = str(input('Enter a city: ')).strip() #Pede uma entrada para o usuário e
#e o trata como str, strip() remove quaisquer espaços em branco no inicio e final da string.
print(cid[:5].upper() == 'SANTO') #Aqui convertemos a entrada do usuário para maiusculo e especificamos apenas os 5 primeiros caracteres
#Entao o programa retornará true or false.
