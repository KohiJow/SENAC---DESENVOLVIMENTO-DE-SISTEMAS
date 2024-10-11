'''Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo. 
desconsiderando os espaços.'''

frase = str(input('Insira uma frase e eu direi se ela é um palíndromo ou não:\n')).replace(' ', '').upper()
frase_invertida = frase[::-1]
if frase == frase_invertida:
    print('É um palíndromo')
else:
    print('Não é um palíndromo')
