"""
Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada o programa deverá perguntar se o usuário quer ou nao continuar,
no final, mostre: #A) quantas pessoas tem mais de 18 anos.
#B) Quantos homens foram cadastrados.
#C) Quantas mulheres com menos de 20 anos:
"""

total_maior_18 = 0
homens_cadastrados = 0
mulheres_menos_20 = 0

while True:
    print("-" * 30)
    print("CADASTRE UMA PESSOA")
    print("-" * 30)

    idade = int(input("Insira a idade: "))
    
    sexo = input("Insira o gênero [M/F]: ").strip().upper()
    while sexo not in ['M', 'F']:
        print("Por favor, insira um gênero válido!")
        sexo = input("Insira o gênero [M/F]: ").strip().upper()

    if idade > 18:
        total_maior_18 += 1
    
    if sexo == "M":
        homens_cadastrados += 1
        
    if idade < 20 and sexo == "F":
        mulheres_menos_20 += 1
        
    decisao = input("Deseja continuar? [S/N]: ").strip().upper()
    while decisao not in ["S", "N"]:
        print("Por favor, escolha uma opção válida!")
        decisao = input("Deseja continuar? [S/N]: ").strip().upper()
    
    if decisao == "N":
        print("-" * 30)
        print(f"Homens cadastrados: {homens_cadastrados}")
        print(f"Pessoas com mais de 18 anos: {total_maior_18}")
        print(f"Mulheres com menos de 20 anos: {mulheres_menos_20}")
        print("-" * 30)
        break
