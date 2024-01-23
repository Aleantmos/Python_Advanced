
class Input:
    def __init__(self, command, value):
        self.command = command
        self.value = value


def read_data():
    count = int(input())
    lines = []
    for i in range(count):
        line = input().split(", ")
        lines.append(Input(line[0], line[1]))

    return lines


def process_data(data):
    # car-numbers container
    parked = set()

    for curr_car in data:
        car_number = curr_car.value

        if curr_car.command == "IN":
            parked.add(car_number)
        else:
            parked.remove(car_number)

    return parked


def print_result(cars):
    if len(cars) == 0:
        print("Parking lot is empty")
    else:
        for car_number in cars:
            print(car_number)


def start():
    # collect input in an array of objects
    data = read_data()

    cars_left = process_data(data)

    # check cars left and print if any
    print_result(cars_left)


start()

