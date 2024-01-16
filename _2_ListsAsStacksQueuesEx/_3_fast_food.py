def read_data():
    data = {'total': int(input()), 'orders': []}

    orders = input().split(" ")
    for order in orders:
        data['orders'].append(int(order))

    return data


def find_max_order(data):
    max_v = float('-inf')
    for order in data['orders']:
        if order > max_v:
            max_v = order

    data['max_v'] = max_v
    return data


def process_data(data):
    data = find_max_order(data)
    return process_orders(data)


def process_orders(data):
    orders = data['orders']
    total_quantity = data['total']
    i = 0
    while i < len(orders):
        if total_quantity > orders[i]:
            total_quantity -= orders[i]
            orders.pop(i)
        else:
            return data
    return data


def print_orders_left(rest):
    result = ""
    for order in rest['orders']:
        result += str(order) + " "
    print("Orders left: " + result.rstrip())


def print_result(rest):
    print(rest['max_v'])
    if len(rest['orders']) > 0:
        print_orders_left(rest)
    else:
        print("Orders complete")


def start():
    data = read_data()
    rest = process_data(data)
    print_result(rest)


start()
