# Create a program that reads the price of a product and shows the new price with a 5% discount

price = float(input('What is the price? '))
discount = price * 0.05
new_price = price - discount

print(f'You will pay ${new_price:.2f} for this.')
