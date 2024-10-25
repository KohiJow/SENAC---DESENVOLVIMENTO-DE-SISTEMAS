# Create an algorithm to read an employee's salary and show their new salary with a 15% increase

salary = float(input('What is your salary? '))
increase = salary * 0.15
new_salary = salary + increase

print(f'You received a 15% increase! Here is your new salary: ${new_salary:.2f}')
