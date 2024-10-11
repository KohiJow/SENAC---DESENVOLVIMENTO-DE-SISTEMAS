# Create a program to read how much money a person has in their wallet and show how many dollars they can buy
# US$1.00 = R$3.27
wallet = float(input('Enter how much money you have: '))
dollar = 1.00
exchange = wallet / 3.27 * dollar

print(f'You can buy: ${exchange:.2f}')
