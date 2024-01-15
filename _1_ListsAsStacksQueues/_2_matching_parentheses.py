def read_data():
    return input()


def extract_parenthesis(data):
    stack = []
    results = []

    for i, element in enumerate(data):
        if element == '(':
            stack.append(i)
        elif element == ')':
            start = stack.pop()
            results.append(data[start:i + 1])

    return results


def print_result(results):
    for result in results:
        print(result)


def get_matching_parenthesis():
    data = read_data()
    results = extract_parenthesis(data)
    print_result(results)


get_matching_parenthesis()
