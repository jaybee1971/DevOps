listOfOperators = ['+', '-', 'x', '/']

ops = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    'x': lambda x, y: x * y,
    '/': lambda x, y: x / y,
}

while True:
    opsIn = input('Enter an Operator: ')
    if opsIn in listOfOperators:
        break
    else:
        print('Enter a valid Operator')
while True:
    num1 = input('Enter Your First Number: ')
    if num1.isnumeric():
        break
    else:
        print('Enter a valid Number')
while True:
    num2 = input('Enter Your Second Number: ')
    if num2.isnumeric():
        break
    else:
        print('Enter a valid Number')

print(ops[opsIn](int(num1), int(num2)))
