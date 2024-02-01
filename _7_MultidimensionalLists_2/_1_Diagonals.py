def read_matrix():
    rows = int(input())
    matrix = []
    for _ in range(rows):
        row = list(map(int, input().split(", ")))
        matrix.append(row)

    return matrix


def get_diagonal_sums(matrix):
    primary = 0
    primary_collection = []

    secondary = 0
    secondary_collection = []

    length = len(matrix)
    for i, row in enumerate(matrix):
        primary += matrix[i][i]
        primary_collection.append(matrix[i][i])

        secondary += matrix[i][length - i - 1]
        secondary_collection.append(matrix[i][length - i - 1])

    return primary, primary_collection, secondary, secondary_collection


def print_diagonal(param, collection, sum_diagonal):
    elements = ", ".join(str(el) for el in collection)
    print(f"{param} diagonal: {elements}. Sum: {sum_diagonal}")


def print_result(primary, primary_collection, secondary, secondary_collection):
    print_diagonal("Primary", primary_collection, primary)
    print_diagonal("Secondary", secondary_collection, secondary)


def start():
    matrix = read_matrix()

    primary, primary_collection, secondary, secondary_collection = get_diagonal_sums(matrix)

    print_result(primary, primary_collection, secondary, secondary_collection)


start()
