def read_data():
    arr_str = input().split("|")
    arr_container = []

    for el in arr_str:
        nums_as_str = el.split()
        arr_container.append(nums_as_str)

    return arr_container


def flatten(arr_container):
    result = []

    for arr in reversed(arr_container):
        result.extend(arr)
    return result


def print_result(result):
    print(" ".join(result))


def start():
    arr_container = read_data()

    result = flatten(arr_container)

    print_result(result)


start()
