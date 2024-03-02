n = int(input())


def print_rhombus(n):
    def print_upper():
        for i in range(1, n + 1):
            spaces = n - i
            print(' ' * spaces + '* ' * i)

    def print_lower():

        for i in range(n - 1, 0, -1):
            spaces = n - i
            print(' ' * spaces + '* ' * i)

    print_upper()
    print_lower()


print_rhombus(n)
