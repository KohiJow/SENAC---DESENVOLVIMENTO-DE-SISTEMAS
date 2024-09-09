#Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um
#dos dígitos separados.
#Ex: Digite um número: 1834
#Unidade: 4
#Dezena: 3
#Centena: 8
#Milhar: 1

#Make a program that reads a number from 0 to 9999 and shows
#each one of its digits separately.
#Ex: Insert a number: 1834
#Unit: 4
#Tens: 3
#Thousands: 1

num = int(input('Enter a Number: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

print(f'The unit is: {u}')
print(f'The tens are: {d}')
print(f'The hundreds are: {c}')
print(f'The thousands are: {m}')

#n = str(num)

#print('seu número é: ', num)
#print('Sua únidade é: ', num[3])
#print('Sua dezena é: ', num[2])
#print('Sua centena é: ', num[1])
#print('Seu milhar é: ', num[0])

