# listOfOperators = ['+', '-', 'x', '/']
runningTotal = 0
n = 0

ops = {
    '+' : lambda x, y: x + y,
    '-' : lambda x, y: x - y,
    'x' : lambda x, y: x * y,
    '/' : lambda x, y: x / y,
}

f = open("step2", mode='r')
inputText = f.read().splitlines()

z = inputText[n].split()

while n <= len(inputText):
    lineTotal = ops[z[1]](int(z[2]), int(z[3]))
    runningTotal = runningTotal + lineTotal
    n = n + 1

print(runningTotal)
