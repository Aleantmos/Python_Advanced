def read_matrix():
    rows = int(input())
    matrix = []
    for _ in range(rows):
        row = list(map(int, input().split(", ")))
        matrix.append(row)

    return matrix


def flatten_matrix(matrix):
    elements = []
    for row in matrix:
        for el in row:
            elements.append(el)

    return elements


def main():
    matrix = read_matrix()
    result = flatten_matrix(matrix)
    print(result)


main()
