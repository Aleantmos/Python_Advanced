def get_values_in_range(start, end):
    arr = []
    for i in range(start, end + 1):
        arr.append(i)

    return arr


def get_range_values(r_str):
    start, end = r_str.split(",")

    arr = get_values_in_range(int(start), int(end))
    return arr


def get_common_values(arr1, arr2):
    commons = []
    for el in arr1:
        if el in arr2:
            commons.append(el)

    return commons


def get_commons_from_line():
    values = input().split("-")

    if len(values) == 2:
        r1_str, r2_str = values

        arr1 = get_range_values(r1_str)

        arr2 = get_range_values(r2_str)

        return get_common_values(arr1, arr2)


def extract_commons():
    count = int(input())

    commons_container = []
    while count > 0:
        curr_commons = get_commons_from_line()
        commons_container.append(curr_commons)
        count -= 1

    return commons_container


def get_biggest_common(commons_container):
    biggest_common = []
    max_range = 0
    for i, curr_common in enumerate(commons_container):
        if len(curr_common) > max_range:
            biggest_common = curr_common
            max_range = len(curr_common)

    return biggest_common


def print_result(biggest_common):
    print(f"Longest intersection is {biggest_common} with length {len(biggest_common)}")


def start():
    commons_container = extract_commons()

    biggest_common = get_biggest_common(commons_container)

    print_result(biggest_common)


start()
