def get_guest_list():
    count = int(input())
    guest_list = set()
    for i in range(count):
        guest_list.add(input())

    return guest_list


def get_guests():
    guests = []

    line = input()
    while line != "END":
        guests.append(line)
        line = input()

    return guests


def read_data():
    # collect guest_list in set
    guest_list = get_guest_list()

    # collect guests coming in array
    guests = get_guests()
    return guest_list, guests


def validate_guests_with_guest_list(guest_list, guests):
    for guest in guests:
        guest_list.remove(guest)

    return guest_list


def custom_sort_key(s):
    return (0, s) if s[0].isdigit() else (1, s)


def print_remaining(not_arrived):
    # sort with first element as digit first
    sorted_non_arrivals = sorted(not_arrived, key=custom_sort_key)

    for guest in sorted_non_arrivals:
        print(guest)


def start():
    guest_list, guests = read_data()

    # remove arrived guests from list
    not_arrived = validate_guests_with_guest_list(guest_list, guests)

    # print remaining elements
    print_remaining(not_arrived)


start()
