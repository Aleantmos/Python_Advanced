def func_executor(*args):
    results = []
    for func, arg in args:
        result = func(*arg)

        results.append(f"{func.__name__} - {result}")

    return results


def sum_numbers(num1, num2):
    return num1 + num2


def multiply_numbers(num1, num2):
    return num1 * num2


print(func_executor(
    (sum_numbers, (1, 2)),
    (multiply_numbers, (2, 4))
))
