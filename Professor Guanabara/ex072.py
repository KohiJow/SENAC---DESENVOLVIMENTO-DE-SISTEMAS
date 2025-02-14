'''
Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero ate vinte
Seu programa devera ler um numero pelo teclado(entre 0 e 20) e mostra-lo por extenso.
'''
contagem = ('zero','um', 'dois', 'tres', 'quatro', 'cinco',
            'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze',
            'treze','quatorze', 'quinze', 'dezesseis', 'dezessete',
            'dezoito', 'dezenove','vinte')

Escolha = int(input('Escolha um numero e eu lhe mostrarei sua escrita por extenso: '))

while Escolha > 20:
    print('Por favor escolha um numero entre 0 e 20.')
    Escolha = int(input('Escolha um numero e eu lhe mostrarei sua escrita por extenso: '))

print("O num escolhido foi:", contagem[Escolha])
