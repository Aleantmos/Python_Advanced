def read_numbers():
    numbers_str = input().split(" ")
    numbers = []
    for num in numbers_str:
        numbers.append(int(num))

    target = int(input())

    return numbers, target


def collect_pairs(sorted_numbers, target):
    l, r = 0, len(sorted_numbers) - 1
    pairs = []

    while l < r:
        left_num = sorted_numbers[l]
        right_num = sorted_numbers[r]
        curr_sum = left_num + right_num

        if curr_sum > target:
            r -= 1
        elif curr_sum < target:
            l += 1
        else:
            pairs.append((right_num, left_num))
            l += 1
            r -= 1

    return pairs


def find_pair_sums_equal_target(numbers, target):
    # sort in ascending
    sorted_numbers = sorted(numbers)

    # collect pairs
    pairs_found = collect_pairs(sorted_numbers, target)

    return pairs_found


def print_result(result):
    for pair in result:
        print(pair)


def read_data():
    numbers, target = read_numbers()

    result = find_pair_sums_equal_target(numbers, target)

    print_result(result)


def start():
    read_data()


start()
