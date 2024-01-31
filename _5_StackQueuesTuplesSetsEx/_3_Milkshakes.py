def get_array():
    try:
        tokens = input().split(", ")
        arr = parse_to_int(tokens)
        return arr
    except ValueError:
        return None


def parse_to_int(tokens):
    arr = []
    for el in tokens:
        try:
            arr.append(int(el))
        except ValueError:
            print(f"{el} not a number")
            return None
    return arr


def read_data():
    # arr of ints
    chocolate = get_array()

    # arr of ints
    milk = get_array()

    return chocolate, milk


def process_data(chocolate, milk):
    milkshakes_made = 0

    while milkshakes_made != 5 and (len(milk) > 0 and len(chocolate) > 0):
        milkshakes_made = make_milkshake(chocolate, milk, milkshakes_made)

    return milkshakes_made, chocolate, milk


def make_milkshake(chocolate, milk, milkshakes_made):
    last_choco = chocolate.pop()
    first_milkshake = milk.pop(0)
    if last_choco == first_milkshake:
        milkshakes_made += 1

    else:
        first_milkshake -= 5
        if first_milkshake > 0:
            chocolate.append(first_milkshake)
    return milkshakes_made


def print_arr(param, arr):
    if len(arr) == 0:
        print(f'{param}: empty')
    else:
        result_arr = ", ".join(str(el) for el in arr)
        print(f"{param}: {result_arr}")


def print_remaining(chocolate, milk):
    print_arr("Chocolate", chocolate)
    print_arr("Milk", milk)


def print_result(milkshake_count, chocolate, milk):
    if milkshake_count < 5:
        print("Not enough milkshakes")
    else:
        print("Great! You made all the chocolate milkshakes needed!")

    print_remaining(chocolate, milk)


def start():
    chocolate, milkshake = read_data()

    if chocolate and milkshake:
        milkshake_count, chocolate, milk = process_data(chocolate, milkshake)
        print_result(milkshake_count, chocolate, milk)


start()
