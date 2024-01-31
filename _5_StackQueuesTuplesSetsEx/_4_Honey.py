def read_data():
    bees = get_int_arr()
    nectar = get_int_arr()
    symbols = input().split(" ")

    if bees is None or nectar is None:
        return False

    return bees, nectar, symbols


def get_int_arr():
    arr = []
    tokens = input().split(" ")

    for token in tokens:
        try:
            arr.append(int(token))
        except ValueError:
            print(f"{token} is not a number")
            return None

    return arr


def calculate_honey(curr_bee, curr_nectar, curr_symbol):
    if curr_symbol == "-":
        result = curr_bee - curr_nectar
        return result
    elif curr_symbol == "+":
        return curr_bee + curr_nectar
    elif curr_symbol == "*":
        return curr_bee * curr_nectar
    elif curr_symbol == "/":
        if curr_nectar != 0:
            return curr_bee / curr_nectar


def process_data(bees, nectar, symbols):
    total_honey = 0
    while bees and nectar:
        curr_nectar = nectar.pop()

        if curr_nectar >= bees[0]:
            curr_symbol = symbols.pop(0)
            curr_bee = bees.pop(0)
            total_honey += calculate_honey(curr_bee, curr_nectar, curr_symbol)

    return total_honey, bees, nectar


def print_result(total_honey, bees, nectar):
    print(f"Total honey made:{total_honey}")

    if bees:
        bee_result = get_printable_arr_result(bees)
        print(f"Bees left: {bee_result}")

    if nectar:
        nectar_result = get_printable_arr_result(nectar)
        print(f"Nectar left: {nectar_result}")


def get_printable_arr_result(bees):
    return ", ".join(str(el) for el in bees)


def start():
    data = read_data()

    if data is not False:
        bees, nectar, symbols = data
        total_honey, bees, nectar = process_data(bees, nectar, symbols)
        print_result(total_honey, bees, nectar)


start()
