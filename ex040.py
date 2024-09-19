'''
Crie um programa que leia duas notas de um aluno e calcule sua média,
mostrando uma mensagem no final, de acordo com a média atingida:
-Média abaixo de 5.0:
Reprovado
-Média entre 5.0 e 6.9:
Recuperação
-Média 7.0 ou superior
Aprovado
'''

math = float(input('\033[1;34mDigite a nota:\nN:\033[m'))
port = float(input('\033[1;34mDigite a nota:\nN:\033[m'))
média_final = port + math / 2

if média_final < 5.0:
    print('\033[1;31mREPROVADO\033[m')
elif média_final > 5.0 and média_final <6.9:
    print('\033[1;33mRECUPERAÇÃO\033[m')
elif média_final > 7.0:
    print('\033[1;32mAPROVADO\033[m')
