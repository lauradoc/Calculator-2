"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )


while True:
    input_string = input('Enter your equation > ')
    tokens = input_string.split(' ')
    if tokens[0] == 'q':
        break
    else:
        num1 = int(tokens[1])
        num2 = int(tokens[2])
        if tokens[0] == '+':
            print(add(num1, num2))
        if tokens[0] == '-':
            print(subtract(num1, num2))
        if tokens[0] == '*':
            print(multiply(num1, num2))
        if tokens[0] == '/':
            print(divide(num1, num2))
        if tokens[0] == 'square':
            print(square(num1))
        if tokens[0] == 'cube':
            print(cube(num1))
        if tokens[0] == 'pow':
            print(power(num1, num2))
        if tokens[0] == 'mod':
            print(mod(num1, num2))
