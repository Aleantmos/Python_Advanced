import math

import numpy as np


def read_data():
    tokens = input().split(" ")
    return tokens


def cumulative_division(numbers):
    if len(numbers) < 2:
        return numbers

    result = numbers[0]

    for element in numbers[1:]:
        if element == 0:
            continue

        result /= element

    return math.floor(result)


def convert_to_numbers(numbers_str):
    return [int(number) for number in numbers_str]


def cumulative_product(numbers):
    result = numbers[0]
    for el in numbers[1:]:
        result *= el
    return result


def do_calculation(numbers, token):
    # numbers = convert_to_numbers(numbers_str)

    if token == "-":
        # numbers_np = np.array(numbers[1:])
        first = numbers[0]
        other_sum = sum(numbers[1:])
        result = first - other_sum
        return result
    elif token == "+":
        return np.sum(numbers)
    elif token == "/":
        return cumulative_division(numbers)
    elif token == "*":
        return cumulative_product(numbers)


def is_integer(s):
    try:
        int(s)  # Try converting the string to an integer
        return True
    except ValueError:
        return False


def process_data(tokens):
    numbers = []
    for token in tokens:
        if is_integer(token):
            numbers.append(int(token))
        else:
            last_result = do_calculation(numbers, token)
            numbers = [last_result]

    return numbers[0]


def start():
    tokens = read_data()

    result = process_data(tokens)

    print(result)


start()
