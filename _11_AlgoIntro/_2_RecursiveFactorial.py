def get_factorial(num):
    if num == 0:
        return 1
    amount = num * get_factorial(num - 1)

    return amount


input_num = int(input())
print(get_factorial(input_num))
