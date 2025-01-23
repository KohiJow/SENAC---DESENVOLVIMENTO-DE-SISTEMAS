"""
Faca um programa que jogue par ou impar com o computador. O jogo só sera interrompido quando o jogador PERDER, mostrando o total vitorias consecutivas 
que ele conquistou no final do jogo.
"""
import random
count = 0
print("-" * 20)
print("VAMOS JOGAR JO-KEN-PO!")
print("-" * 20)
while True:
    Escolha = str(input("vc quer PAR(P) ou IMPAR(I)? ")).strip().upper()[0]
    
    while Escolha not in "PPIi":
        Escolha = str(input("vc quer PAR(P) ou IMPAR(I)? ")).strip().upper()[0]
    
    player = int(input("Escolha seu número: "))
    computador = random.randint(1,10)
    resultado = player+computador
    print(f"Eu coloquei: {computador} entao deu {resultado}")  
    
    if resultado % 2 == 0 and Escolha in ("pP"):
        print("Voce venceu, vamos denovo!")
        count+= 1
    elif resultado % 2 != 0 and Escolha in ("Ii"):
        print("Voce venceu, vamos denovo!")
        count += 1
    else:
        print(f"PERDEU! vc ganhou {count} vezes")
        break
