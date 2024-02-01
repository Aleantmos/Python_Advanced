def read_matrix():
    rows = int(input())
    matrix = []
    for _ in range(rows):
        row = list(map(int, input().split(" ")))
        matrix.append(row)

    return matrix


def get_diagonal_sums(matrix):
    primary = 0

    secondary = 0

    length = len(matrix)
    for i, row in enumerate(matrix):
        primary += matrix[i][i]

        secondary += matrix[i][length - i - 1]

    return primary, secondary


def get_diagonal_diff(matrix):
    primary, secondary = get_diagonal_sums(matrix)
    return abs(primary - secondary)


def start():
    matrix = read_matrix()

    result = get_diagonal_diff(matrix)

    print(result)


start()
