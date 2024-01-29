def get_unique_numbers():
    nums_str = input().split(" ")
    container = list()

    for el in nums_str:
        if not container.__contains__(el):
            container.append(int(el))

    return container


def read_data():
    s1 = get_unique_numbers()
    s2 = get_unique_numbers()

    commands_count = int(input())

    return s1, s2, commands_count


def get_command():
    tokens = input().split(" ")
    commands = []
    nums = []

    for i, el in enumerate(tokens):
        if i < 2:
            commands.append(el)
        else:
            nums.append(int(tokens[i]))

    return commands, nums


def do_add(my_list, values):
    for value in values:
        if not my_list.__contains__(value):
            my_list.append(value)

    return my_list


def do_remove(my_list, values):
    for value in values:
        if my_list.__contains__(value):
            my_list.remove(value)

    return my_list


def check_subset(bigger, smaller):
    if bigger.__contains__(smaller):
        return True

    return False


def process_commands(s1, s2, commands_count):
    while commands_count > 0:
        commands, values = get_command()

        if commands[0] == "Add":
            if commands[1] == "First":
                do_add(s1, values)
            elif commands[1] == "Second":
                do_add(s2, values)

        elif commands[0] == "Remove":
            if commands[1] == "First":
                do_remove(s1, values)
            elif commands[1] == "Second":
                do_remove(s2, values)
        elif commands[0] == "Check":
            if len(s1) > len(s2):
                print(check_subset(s1, s2))
            else:
                print(check_subset(s2, s2))
        commands_count -= 1

    return s1, s2


def print_list(sorted_l):
    result = ", ".join(map(str, sorted_l))
    print(result)


def print_sorted_lists(l1, l2):
    sorter_l1 = sorted(l1)
    print_list(sorter_l1)

    sorter_l2 = sorted(l2)
    print_list(sorter_l2)


def start():
    l1, l2, commands_count = read_data()

    l1, l2 = process_commands(l1, l2, commands_count)

    print_sorted_lists(l1, l2)


start()
