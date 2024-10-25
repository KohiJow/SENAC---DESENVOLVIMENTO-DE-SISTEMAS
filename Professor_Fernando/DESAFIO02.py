'''
Escreva um programa que receba três notas de um aluno, calcule 
a média e exiba o resultado.
'''
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

media = (nota1 + nota2 + nota3) / 3

print(f"A média das notas é {media:.2f}.")
