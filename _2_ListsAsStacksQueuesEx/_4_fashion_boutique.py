def read_data():
    data = {'clothes': [], 'capacity': 0}

    clothes_str = input().split(" ")
    for piece in clothes_str:
        data['clothes'].append(int(piece))

    data['capacity'] = int(input())

    return data


def process_data(data):
    total_racks = 0
    cap = data['capacity']

    clothes = data['clothes']
    rack = 0
    i = len(clothes) - 1
    while i >= 0:
        rack += clothes[i]
        if rack > cap:
            rack = 0
            total_racks += 1
            i += 1
        elif rack == cap:
            rack = 0
            total_racks += 1

        i -= 1

    if rack > 0:
        total_racks += 1

    return total_racks


def start():
    data = read_data()
    result = process_data(data)
    print(result)


start()
