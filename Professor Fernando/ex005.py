#Calculadora

a = int(input('Digite um valor: '))

b = int(input('Digite outro valor: '))

soma = a + b

divisão = a / b

subtração = a - b

multiplicação = a * b

escolha = str(input('Escolha qual operação deseja \n A)Subtração \n B)Divisão \n C)Multiplicação \n D)Soma')).split().upper()

if escolha == 'A':
    print(subtração)

elif escolha == 'B':
    print(divisão)

elif escolha == 'C':
    print(multiplicação)

elif escolha == 'D':
    print(soma)

#incompleto