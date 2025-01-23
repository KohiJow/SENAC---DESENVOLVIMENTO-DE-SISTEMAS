"""
Crie um programa que leia varios numeros inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condicao de parada. 
No final, mostre quantos numeros foram digitados e qual foi a soma entre eles (desconsiderando o flag).
"""
print("-"*30)
num=int(input("insira um número: "))
new_num = 0
cont = 0
while num != 999:
    num=int(input("insira um número: "))
    if num != 999:
        new_num += num
        cont +=1
    else:
        break
print(f"Os numeros digitados foram {cont} e a soma deles é {new_num}")
print("-"*30)

