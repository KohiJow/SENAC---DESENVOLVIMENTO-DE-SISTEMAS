'''
Crie um programa que tenha uma tupla com varias palavras (nao usar acentos). Depois disso, voce
deve mostrar, para cada palavra, quais sao as suas vogais.
'''
nomes = ("joao", "ester", "maranhao", "godoy")  # Tupla com as palavras

vogais = "aeiou"  # Definição das vogais

for nome in nomes:  # Percorre cada palavra na tupla
    print(f"\nNa palavra {nome.upper()} temos as vogais: ", end="")
    
    for letra in nome:  # Percorre cada letra da palavra
        if letra in vogais:  # Se for vogal, imprime
            print(letra, end=" ")
