def read_data():
    return input().split(" ")


def reverse(nums):
    return nums[::-1]


def print_result(result):
    str_result = " ".join(result)
    print(str_result)


def start():
    nums = read_data()
    result = reverse(nums)
    print_result(result)


start()
