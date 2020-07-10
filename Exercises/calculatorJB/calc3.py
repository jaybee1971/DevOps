import math

ops = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    'x': lambda x, y: x * y,
    '/': lambda x, y: x / y,
    '^': lambda x, y: x ^ y,
}


def processGoto(lineFeed) -> int:
    z = lineFeed.split()
    if z[1] == 'calc':
        return math.floor(ops[z[2]](int(z[3]), int(z[4])))
    else:
        return int(z[1])


def main():
    with open("step3", mode='r') as f:
        file_by_lines = f.read().splitlines()
        lines_hit = set()
        line_number = 1
        while True:
            current_line = file_by_lines[line_number - 1]
            if current_line in lines_hit:
                break
            new_line_number = processGoto(current_line)
            print(current_line)
            print(new_line_number)
            lines_hit.add(current_line)
            line_number = new_line_number
        print(f"Answer: Line {line_number} {current_line}")


if __name__ == "__main__":
    main()
