def find_odds(nums):
    odds = []
    for el in nums:
        if el % 2 == 1:
            odds.append(el)
    return odds


def even_odd(*args):
    numbers = args[:-1]
    command = args[-1]
    result = []
    if command == "even":
        result = find_evens(numbers)
    elif command == "odd":
        result = find_odds(numbers)

    return result


def find_evens(nums):
    evens = []
    for el in nums:
        if el % 2 == 0:
            evens.append(el)
    return evens


print(even_odd(1, 2, 3, 4, 5, 6, "even"))

print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))
