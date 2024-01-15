from collections import deque

people = []


def read_input():
    global people
    people = input().split(" ")
    return int(input())


def process_game(toss):
    queue = deque(people)

    while len(queue) > 1:
        for curr in range(toss - 1):
            queue.append(queue.popleft())

        print(f"Removed {queue.popleft()}")

    print(f"Last is {queue[0]}")


def start():
    toss = read_input()
    process_game(toss)


start()
