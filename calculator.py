"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )


while True:
    input_string = input('Enter your equation > ')
    tokens = input_string.split(' ')
    if tokens[0] == 'q':
        break
    else:
        if tokens[0] == '+':
            num1 = int(tokens[1])
            num2 = int(tokens[2])
            print(add(num1, num2))
        if tokens[0] == '-':
            num1 = int(tokens[1])
            num2 = int(tokens[2])
