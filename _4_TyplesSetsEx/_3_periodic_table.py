def get_elements():
    return input().split(" ")


def add_elements_to_set(elements, tokens):
    for token in tokens:
        elements.append(token)


def read_data():
    count = int(input())
    elements = []

    while count > 0:
        tokens = get_elements()
        add_elements_to_set(elements, tokens)
        count -= 1

    return elements


def find_unique_elements(all_elements):
    unique_elements = set()

    for element in all_elements:
        unique_elements.add(element)

    return unique_elements


def print_result(result):
    for el in result:
        print(el)


def start():
    # read all elements
    all_elements = read_data()

    # collect unique elements in set
    result = find_unique_elements(all_elements)

    print_result(result)


start()
