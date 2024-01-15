people = []
water_quantity = 0


def read_data():
    data = []
    line = input()

    while line != "":
        data.append(line)
        line = input()

    return data


def extract_initial_info(data):
    global water_quantity
    for i, element in enumerate(data):
        curr = data.pop(0)

        if element == 'Start':
            return

        if i == 0:
            water_quantity = int(curr)
        else:
            people.append(curr)

    return data


def process_water_consumption(modified):
    global water_quantity
    for element in modified:
        split = element.split(" ")
        if len(split) == 2:
            refill = int(split[1])
            water_quantity += refill
        elif element == 'End':
            return
        else:
            person = people.pop(0)
            quantity = int(element)
            if water_quantity >= quantity:
                water_quantity -= quantity
                print(f"{person} got water")
            else:
                print(f"{person} must wait")


def print_remaining_quantity():
    print(f"{water_quantity} liters left")


def start():
    data = read_data()
    modified = extract_initial_info(data)
    process_water_consumption(modified)
    print_remaining_quantity()


start()
