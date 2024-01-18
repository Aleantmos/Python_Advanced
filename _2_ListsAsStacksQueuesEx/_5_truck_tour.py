def read_data():
    input_count = int(input())
    data = []
    i = 0
    while i < input_count:
        petrol, distance = map(int, input().split(" "))
        data.append((petrol, distance))
        i += 1
    return data


def can_complete_circle(start_index, data):
    tank = 0
    n = len(data)
    for i in range(n):
        petrol, distance = data[(start_index + i) % n]
        tank += petrol
        if tank < distance:
            return False

        tank -= distance
    return True


def find_complete_circle_start(data):
    for start_index in range(len(data)):
        if can_complete_circle(start_index, data):
            return start_index
    return -1


def start():
    data = read_data()
    index = find_complete_circle_start(data)
    if index == -1:
        print("No such point")
    else:
        print(index)


start()
