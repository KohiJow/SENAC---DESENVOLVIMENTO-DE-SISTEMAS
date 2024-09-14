#Calculadora
while True:
    
    try: 
        
        a = int(input('Digite um valor: '))

        b = int(input('Digite outro valor: '))

        soma = a + b

        divisão = a / b if b or a != 0 else 'Divisão por zero não permitida'

        subtração = a - b

        multiplicação = a * b
        
        escolha = str(input('Escolha qual operação deseja \n A)Subtração \n B)Divisão \n C)Multiplicação \n D)Soma\n E)Sair do programa \n R: ')).strip().upper()

        if escolha == 'A':
            print(f'O Resultado da subtração de {a} por {b} é: {subtração}')
        
        elif escolha == 'B':
            print(f'O Resultado da divisão de {a} por {b} é: {divisão}')

        elif escolha == 'C':
            print(f'O Resultado da multiplicação de {a} por {b} é: {multiplicação}')

        elif escolha == 'D':
            print(f'O Resultado da soma de {a} por {b} é: {soma}')

        elif escolha == 'E':
            break
        
        else:
            print('Opção inválida, tente novamente: ')
            
        continuar = input('Deseja Continuar? s/n').strip().upper()
        while continuar != 'S' or 'N':
            print('Poderia repetir?')
           
            if continuar == 'S':
                print('Continuando')
        
            else:
                continuar == 'N'
                print('Parando')
                break
        
        
    except: 'Insira um valor numérico por favor'
#incompleto