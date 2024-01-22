def read_data():
    count = int(input())
    names = set()

    for i in range(count):
        name = input()
        names.add(name)

    return names


def print_names(names):
    result = ""
    for name in names:
        result += name + "\n"

    print(result)


def start():
    # read names and collect unique in a set
    names = read_data()
    # print collected names (each on a new line)
    print_names(names)


start()