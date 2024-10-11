# Create a program to read the width and height of a wall in meters, calculate its area, and determine how much paint is needed to cover the wall, considering that 1 liter of paint covers 2 m²

width = float(input('What is the width of the wall? '))
height = float(input('What is the height of the wall? '))

area = width * height
paint = area / 2

print(f'Your wall width is {width} m and height is {height} m, so the area is {area} m².')
print(f'You need {paint} liters of paint.')
