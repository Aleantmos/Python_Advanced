def read_elements():
    return input().split(" ")


def parse_elements(numbers_as_str):
    return [float(num) for num in numbers_as_str]


def read_input():
    # read input separated by spaces
    numbers_as_str = read_elements()

    # converts strings into floats
    numbers = parse_elements(numbers_as_str)
    return numbers


def count_occurrences(numbers):
    # use a dictionary to count occurrences
    occurrences = {}

    # count occurrences of each unique number
    for number in numbers:
        if number in occurrences:
            occurrences[number] += 1
        else:
            occurrences[number] = 1

    return occurrences


def print_result(numbers_counted):
    # iterate through the dictionary and print the occurrences
    for number, count in numbers_counted.items():
        print(f"{number:.1f} - {count} times")


def start():
    numbers = read_input()
    numbers_counted = count_occurrences(numbers)
    print_result(numbers_counted)


start()
