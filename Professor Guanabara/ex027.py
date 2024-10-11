#Faça um programa que leia o nome completo de uma pessoa.
#mostrando em seguida o primeiro e o último nome separadamente.
#Ex: Ana Maria de Souza
# Primeiro= Ana
# Último= Souza

#nome = str(input('Digite seu nome: ')).strip().split()
#print('Seu primeiro nome é:',nome[0])
#print('Seu último nome é:',nome[-1])

###correção do guanabara (ele usava a formatação antiga pois esse video é umpouco antigo)

n = str(input('Digite seu nome completo: ')).strip()
nome = n.split()
print('Muito prazer em te conhecer')
print('Seu primeiro nome é {}'.format(nome[0]))
print('Seu último nome é {}'.format(nome[len(nome)-1]))
