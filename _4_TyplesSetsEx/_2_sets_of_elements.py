def read_arr(count):
    arr = []
    while count > 0:
        arr.append(input())
        count -= 1

    return arr


def read_data():
    counts = input().split(" ")

    if len(counts) == 2:
        try:
            c1_str, c2_str = counts

            c1_int = int(c1_str)
            arr1 = read_arr(c1_int)

            c2_int = int(c2_str)
            arr2 = read_arr(c2_int)

            return arr1, arr2

        except ValueError:
            print("Error: One of the inputs is not an integer.")
    else:
        print("Error: Please enter exactly two values separated by a space.")


def find_common_elements(arr1, arr2):
    commons = []
    for el in arr1:
        if arr2.__contains__(el):
            commons.append(el)

    return commons


def print_result(result):
    for el in result:
        print(el)


def start():
    arr1, arr2 = read_data()

    result = find_common_elements(arr1, arr2)

    print_result(result)


start()
