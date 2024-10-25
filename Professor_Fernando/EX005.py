#Exibe a tabuada de um número inserido pelo usúario
numero = int(input("Digite um número para ver a tabuada: "))

#laço para iterar de 1 até 10
for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")
    