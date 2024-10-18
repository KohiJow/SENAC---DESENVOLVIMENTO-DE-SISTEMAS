#Função que soma dois números
def somar(a, b):
    return a + b

#Recebe dois números reais (float)
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o psegundo número: "))

#chama a função de soma
resultado = somar(num1, num2)

#Exibe o resultado da soma
print(f"O resultado da soma é: {resultado}")
