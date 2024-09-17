#Desenvolva um programa que pergunte a distancia de uma viagem
#em km. calcule o preço da passagem, cobrando R$ 0.50 por km para viagens
#de até 200km e 0,45 para viagens mais longas

distancia = float(input('Qual a distãncia da sua viagem?\n'))

if distancia > 200:
    print(f'Vai custar: ${distancia * 0.45:.2f}')
else:
    print(f'Sua viagem vai custar: ${distancia <= 200:.2f}')