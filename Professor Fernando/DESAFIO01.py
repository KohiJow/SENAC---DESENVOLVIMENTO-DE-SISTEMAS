'''
Crie um programa que peça ao usúario seyu nome, idade e altura. 
Em seguida, exiba uma mensagem formatada com essas informações
e informe se ele pode dirigir (idade mínima de 18 anos)
'''

nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
altura = float(input("Digite sua altura: "))

print(f"Nome: {nome}, Idade: {idade}, Altura: {altura:.2f}")

if idade>=18:
    print("Você pode dirigir.")
else:
    print("Você não pode dirigir")
    