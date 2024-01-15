def print_reversed_string():
    myString = read_data()
    result = reverse_string(myString)
    print(result)


def read_data():
    data = input()
    return data


def reverse_string(input_string):
    stack = []

    for char in input_string:
        stack.append(char)

    reverse_string = ''
    while stack:
        reverse_string += stack.pop()

    return reverse_string


print_reversed_string()
