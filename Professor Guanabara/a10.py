#Condições

#nome = str(input('Qual é seu nome? '))

#if nome == 'Jow':
#    print('Que nome lindo você tem!')
#    print(f'Bom dia {nome}')
#else:
#    print('Seu nome é tão normal!')
#    print(f'Bom dia {nome}')

n1= float(input('Digite a primeira nota: '))
n2= float(input('Digite a segunda nota: '))

m = (n1 + n2/2)

print(f'A sua média foi {m:.1f}')

print('Parabéns' if m >=6 else 'Estude Mais!')

#if m >= 6.0:
#    print('Parabéns!')
#else:
#    print('Estude mais!')