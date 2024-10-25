# Write a program to read a value in meters and show it converted to centimeters and millimeters.

meters = int(input('Enter the number of meters you want to convert: '))
centimeters = meters * 100
millimeters = meters * 1000

print(f'The meters converted to cm is {centimeters} and to mm is {millimeters}')
print('The meters converted to cm is {} and to mm is {}'.format(centimeters, millimeters))
print('The meters converted to cm is', centimeters, 'and to mm is', millimeters)
