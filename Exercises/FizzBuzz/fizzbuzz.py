number_list = []
index = 0
number = 1


def print_text(argument):
    text = {
        0: "Fizz",
        1: "Buzz",
        2: "FizzBuzz",
        3: "Bang",
        4: "FizzBang",
        5: "Bong",
        6: "Fezz",
        7: "FezzBuzz",
        8: "FizzFezzBuzz",
        9: "FezzBong",
        10: "BuzzFizz"
    }
    return text.get(argument, number)


# def divide_func(n, d):
#     return lambda a: n / d
#
#
# def check_float(check_number):
#     float_number = check_number / divide_number
#     return argument


def check_float(check_number, divide_number):
    float_number = check_number / divide_number
    return float(float_number).is_integer()


user_input = input('Enter a FizzBuzz number ')
user_number = int(user_input)

while number != user_number + 1:
    number_list.append(number)
    number = number + 1

try:
 while index != user_number:
    number = number_list[index]
    if check_float(number, 3) and check_float(number, 5) and not check_float(number, 7) and not check_float(number, 11):
        argument = 2
    elif not check_float(number, 3) and not check_float(number, 7) and check_float(number, 5) and not check_float(number, 11):
        argument = 1
    elif check_float(number, 3) and not check_float(number, 5) and not check_float(number, 7) and not check_float(number, 11):
        argument = 0
    elif check_float(number, 3) and check_float(number, 5) and check_float(number, 7) and not check_float(number, 11):
        argument = 4
    elif not check_float(number, 3) and check_float(number, 7) and not check_float(number, 5) and not check_float(number, 11):
        argument = 3
    elif check_float(number, 11):
        argument = 5
    else:
        argument = "x"
    print(print_text(argument))
    index = index + 1
except TypeError:
    print('Something went wrong!')
finally:
    print('Exiting FizzBuzz Pt1')
