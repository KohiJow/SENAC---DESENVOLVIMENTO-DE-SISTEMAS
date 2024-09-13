#Calculadora
while True:
    a = int(input('Digite um valor: '))

    b = int(input('Digite outro valor: '))

    soma = a + b

    divisão = a / b

    subtração = a - b

    multiplicação = a * b
    
    escolha = str(input('Escolha qual operação deseja \n A)Subtração \n B)Divisão \n C)Multiplicação \n D)Soma\n E)Sair do programa \n R: ')).strip().upper()

    if escolha == 'A':
        print(f'O Resultado da subtração de {a} por {b} é: {subtração}')

        continuar = str(input('Deseja continuar? Sim ou Não?\n')).upper().strip()

        if  continuar == 'SIM':
            print('continuando')
        
        elif continuar =='NAO' or 'NÃO':
            break

        else:
            print('Opção inválida, tente novamente: ')
    
    elif escolha == 'B':
        print(f'O Resultado da divisão de {a} por {b} é: {divisão}')

        continuar = str(input('Deseja continuar? Sim ou Não?\n')).upper().strip()

        if  continuar == 'SIM':
            print('continuando')
        
        elif continuar =='NAO' or 'NÃO':
            break

        else:
            print('Opção inválida, tente novamente: ')

    elif escolha == 'C':
        print(f'O Resultado da multiplicação de {a} por {b} é: {multiplicação}')

        continuar = str(input('Deseja continuar? Sim ou Não?\n')).upper().strip()

        if  continuar == 'SIM':
            print('continuando')
        
        elif continuar =='NAO' or 'NÃO':
            break

        else:
            print('Opção inválida, tente novamente: ')

    elif escolha == 'D':
        print(f'O Resultado da soma de {a} por {b} é: {soma}')

        continuar = str(input('Deseja continuar? Sim ou Não?\n')).upper().strip()

        if  continuar == 'SIM':
            print('continuando')
        
        elif continuar =='NAO' or 'NÃO':
            break

        else:
            print('Opção inválida, tente novamente: ')

    elif escolha == 'E':
        break
    
    else:
        print('Opção inválida, tente novamente: ')
