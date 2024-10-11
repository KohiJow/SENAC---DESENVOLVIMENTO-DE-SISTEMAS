# Write a program that asks for the number of kilometers traveled by a rented car and the number of days it was rented.
# Calculate the price to pay, knowing that the car costs $60 per day and $0.15 per kilometer driven.
# Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado
# e a quantidade de dias pelos quais ele foi alugado. 
# Calcule o preço a pagar, sabendo que o carro custa 60$ por dia e 0,15$ por km rodado.

KM = float(input('How many kilometers were traveled? | Quantos quilômetros foram percorridos? '))
Days = int(input('How many days was it rented for? | Por quantos dias ele foi alugado?'))

Final_Price = (Days * 60) + (KM * 0.15)

print(f'Your total amount to pay is: | Seu valor total a pagar pelo aluguel é: {Final_Price}')
