#Faça um programa que leia uma frase pelo teclado e mostre:
#Quantas vezes aparece a letra "A".
#Em que posição ela aparece a primeira vez.
#Em que posição ela aparece a última vez.

Frase = str(input('Digite uma frase e eu acharei todos os "a" nela: ')).strip().upper()
print('A letra "A" aparece um total de: ', Frase.count('A'), )
print('A primeira letra A aparece no caractére: ',Frase.find('A')+1)
print('A última letra A aparece no caractére: ',Frase.rfind('A')+1)

