#Escreva um programa que leia a velocidade de um carro.
#Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.
#A multa vai custar R$ 7.00 por cada km acima do limite.
"""
velocidade = float(input('Em que velocidade o carro estava: '))
diferença = velocidade - 80

if velocidade > 80.0:
   print(f'A multa foi de: ${diferença * 7}')
elif velocidade < 80.0:
    print('esse é lerdão hein pai, tomo multa não')
else: 
    velocidade == 80.0
    print('no limiteeeeeeeeee, tomo multa não.')
"""
##Guanabara
velocidade = float(input('Qual é a velocidade atual do carro ? '))
if velocidade > 80:
    print('MULTADO! Você excedeu o limite permitido que é de 80Km/h')
    multa = (velocidade-80) * 7
    print(f'Voce deve pagar uma multa de R${multa:.2f}')
print('Tenha um bom dia! Dirija com segurança')