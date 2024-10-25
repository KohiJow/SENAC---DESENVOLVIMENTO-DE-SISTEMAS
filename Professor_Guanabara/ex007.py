# Develop a program to read two grades from a student, calculate the average, and display it

english = float(input('Enter the grade of your student in English: '))
science = float(input('Enter the grade of your student in Science: '))
## In this line, it is very important not to forget the "()" and to respect the order of operations
average = (english + science) / 2

print('The average of this student is: ', average)
print(f'The average of this student is: {average}')
print('The average of this student is: {}'.format(average))
