def read_input():
    count = int(input())
    usernames = set()
    for i in range(count):
        usernames.add(input())

    return usernames


def print_result(usernames):
    for username in usernames:
        print(username)


def start():
    usernames = read_input()

    print_result(usernames)


start()
