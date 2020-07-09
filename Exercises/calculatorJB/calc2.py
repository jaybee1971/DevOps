ops = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    'x': lambda x, y: x * y,
    '/': lambda x, y: x / y,
    '^': lambda x, y: x ^ y,
}

with open("step2", mode='r') as f:
    inputText = f.read().splitlines()

runningTotal = 0

for lines in inputText:
    z = lines.split()
    lineTotal = ops[z[1]](int(z[2]), int(z[3]))
    runningTotal += lineTotal

print(runningTotal)
