#Escreva um programa que leia a velocidade de um carro.
#Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.
#A multa vai custar R$ 7.00 por cada km acima do limite.

velocidade = float(input('Em que velocidade o carro estava: '))
multa = 7.00
diferença = velocidade - 80

if velocidade > 80.0:
   print('Sua multa foi de: ', diferença * 7 + velocidade)
elif velocidade < 80.0:
    print('esse é lerdão hein pai, tomo multa não')
else: 
    velocidade == 80.0
    print('no limiteeeeeeeeee, tomo multa não.')
