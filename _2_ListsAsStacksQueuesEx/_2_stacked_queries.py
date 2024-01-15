def findMax(stack):
    max_v = float('-inf')
    for v in stack:
        if v > max_v:
            max_v = v

    print(max_v)


def findMin(stack):
    min_v = float('+inf')
    for v in stack:
        if v < min_v:
            min_v = v

    print(min_v)


def print_rest(stack):
    str_result = ""
    while stack:
        element = stack.pop()
        str_result += str(element) + " "

    print(str_result.rstrip())


def process_data(commands, stack):
    for line in commands:
        tokens = line.split(" ")

        command = tokens[0]
        if command == "1":
            stack.append(int(tokens[1]))
        elif command == "2":
            stack.pop()
        elif command == "3":
            findMax(stack)
        elif command == "4":
            findMin(stack)

    return stack


def read_commands_cnt():
    return int(input())


def start():
    num_commands = read_commands_cnt()
    commands = []
    for i in range(num_commands):
        line = input()
        commands.append(line)

    stack = []
    rest = process_data(commands, stack)
    print_rest(rest)


start()
