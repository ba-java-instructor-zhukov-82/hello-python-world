a = int(input('Please, enter the number:'))  # reads input values
b = int(input('Please, enter the number:'))
operation = input('Please, enter the operation (+ - * /):')

if operation == '+':
    print(a, ' + ', b, ' = ', a + b)

if operation == '-':
    print(a, ' - ', b, ' = ', a - b)

# Home task: add multiplicity and division to this program