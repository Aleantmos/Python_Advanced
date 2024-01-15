def print_queue(queue):
    while len(queue) > 0:
        element = queue.pop(0)
        print(element)


def read_data():
    curr = input()
    data = []
    while curr != "":
        data.append(curr)
        curr = input()

    return data


def print_remaining_count(queue):
    print(len(queue))


def process_data(data):
    queue = []
    for element in data:
        if element == 'Paid':
            print_queue(queue)
            continue
        elif element == "End":
            print_remaining_count(queue)
            return
        queue.append(element)


def start():
    data = read_data()
    process_data(data)


start()
