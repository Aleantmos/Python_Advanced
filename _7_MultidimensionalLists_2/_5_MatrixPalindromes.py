def read_dimensions():
    return map(int, input().split(" "))


def get_elements(i, cols):
    line = []
    for j in range(cols):
        el1 = el3 = chr(97 + i)
        el2 = chr(97 + j + i)
        line.append(f"{el1}{el2}{el3}")
    return line


def get_matrix(dim):
    rows, cols = dim
    matrix = []
    for i in range(rows):
        matrix.append(get_elements(i, cols))
    return matrix


def print_matrix(matrix):
    for row in matrix:
        print(" ".join(row))


def start():
    dim = read_dimensions()

    matrix = get_matrix(dim)

    print_matrix(matrix)


start()
